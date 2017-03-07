import json

from flask import Flask, render_template, request, jsonify
from constant import TOKEN, APP_SECRETE
from flask_debugtoolbar import DebugToolbarExtension
from yelp_api_v3 import call_yelp
from data import is_in_polygon
from math import sin, cos, sqrt, atan2, radians
from sqlalchemy import create_engine
import pandas as pd
from collections import OrderedDict
from KMean_Cluster import kmean_clusters


app = Flask(__name__) 

app.secret_key = APP_SECRETE

@app.route("/", methods=['GET'])
def home():
    """Home Page for display the map."""

    return render_template("map.html", token=TOKEN)


@app.route("/", methods=['POST'])
def dis_restaurants():
    """Display the restaurants within the polygon region"""

    # grab data from Ajax request
    # store offset number in order to use for calling yelp api later
    data = json.loads(request.form.get("data")) 
    offset = json.loads(request.form.get("offset")) 

    # all the polygon corner points' latitude and longitude
    polyY = [float(lat.get('lat')) for lat in data] 
    polyX = [float(lng.get('lng')) for lng in data] 

    # find the largest smallest lat, lng from the polygon corner points
    l1 = min(polyY)
    l2 = min(polyX)
    l3 = max(polyY)
    l4 = max(polyX)
    
    # find the center point
    longitude = (l2+l4)/2
    latitude = (l1+l3)/2

    # approximate radius of earth in km
    # find the center point and radius of the circle 
    # that contains the farest two points.
    r = 6373.0
    lat1 = radians(l1)
    lon1 = radians(l2)
    lat2 = radians(l3)
    lon2 = radians(l4)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = r * c*1000
    radius = int(distance/2)

    # maximum range of the polygon
    # limitation due to Yelp API: radius less than 40000 meters (25 miles)
    if radius > 40000: 
        radius = 39999

    # Send the center point and radius of the circle that covers the polygon
    # Also offset is used offset results in yelp api (due to limitation on
    # only returning 50 resutls/call)
    api_points = call_yelp(latitude, longitude, radius, offset)
    if api_points.empty: 
        return jsonify({"result":"No result"})
    else:
        info = is_in_polygon(polyY, polyX, api_points)
        top_count = info['review_count'].quantile(q=0.98)
        # select the top 7 categories
        top_cat = info.groupby(['my_category']).size().sort_values(ascending=False).head(7).index.tolist()
        data_top_cat = info[info['my_category'].isin(top_cat)].groupby(['price','my_category']).size()
        dict1 = data_top_cat.to_dict()
        l1,l2,l3,l4 = {}, {}, {}, {}
        for j in top_cat:
            l1[j] = 0
            l2[j] = 0
            l3[j] = 0
            l4[j] = 0
        for i in dict1:
            if str(i[0]) == '$':
                l1[i[1]] = dict1[i]
            elif str(i[0]) == '$$':
                l2[i[1]] = dict1[i]
            elif str(i[0]) == '$$$':
                l3[i[1]] = dict1[i]
            elif str(i[0]) == '$$$$':
                l4[i[1]] = dict1[i]
            # else:
            #     print i
        ord_l1 = OrderedDict((cat, l1[cat]) for cat in top_cat)
        ord_l2 = OrderedDict((cat, l2[cat]) for cat in top_cat)
        ord_l3 = OrderedDict((cat, l3[cat]) for cat in top_cat)
        ord_l4 = OrderedDict((cat, l4[cat]) for cat in top_cat)
        final = [['$',ord_l1],['$$',ord_l2],['$$$',ord_l3],['$$$$',ord_l4]]

        cat1 = info[info['my_category'] == top_cat[0]].to_json(orient = "records")
        cat2 = info[info['my_category'] == top_cat[1]].to_json(orient = "records")
        cat3 = info[info['my_category'] == top_cat[2]].to_json(orient = "records")
        cat4 = info[info['my_category'] == top_cat[3]].to_json(orient = "records")
        cat5 = info[info['my_category'] == top_cat[4]].to_json(orient = "records")
        cat6 = info[info['my_category'] == top_cat[5]].to_json(orient = "records")
        cat7 = info[info['my_category'] == top_cat[6]].to_json(orient = "records")
        cat8 = info[~info['my_category'].isin(top_cat)].to_json(orient = "records")

    return jsonify({"result":[cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8], 
                    "visualization": final,"top_categoy": top_cat, 
                    "top_count": top_count})


@app.route("/db.json", methods=['POST'])
def check_db():
    """Grab all the data points in database and check if any points
    is inside of the poygon."""

    data = json.loads(request.form.get("data"))
    polyY = [float(lat.get('lat')) for lat in data]
    polyX = [float(lng.get('lng')) for lng in data]

    engine = create_engine('postgresql://peiyan:peiyan@localhost:8000/peiyan')
    db_points = pd.read_sql_query('SELECT * FROM restaurant',con=engine)

    info = is_in_polygon(polyY, polyX, db_points)
    
    top_count = info['review_count'].quantile(q=0.98)

    top_cat = info.groupby(['my_category']).size().sort_values(ascending=False).head(7).index.tolist()
    data_top_cat = info[info['my_category'].isin(top_cat)].groupby(['price','my_category']).size()
    dict1 = data_top_cat.to_dict()
    l1,l2,l3,l4 = {}, {}, {}, {}
    for j in top_cat:
        l1[j] = 0
        l2[j] = 0
        l3[j] = 0
        l4[j] = 0
    for i in dict1:
        if str(i[0]) == '$':
            l1[i[1]] = dict1[i]
        elif str(i[0]) == '$$':
            l2[i[1]] = dict1[i]
        elif str(i[0]) == '$$$':
            l3[i[1]] = dict1[i]
        elif str(i[0]) == '$$$$':
            l4[i[1]] = dict1[i]

    ord_l1 = OrderedDict((cat, l1[cat]) for cat in top_cat)
    ord_l2 = OrderedDict((cat, l2[cat]) for cat in top_cat)
    ord_l3 = OrderedDict((cat, l3[cat]) for cat in top_cat)
    ord_l4 = OrderedDict((cat, l4[cat]) for cat in top_cat)
    final = [['$',ord_l1],['$$',ord_l2],['$$$',ord_l3],['$$$$',ord_l4]]

    if len(top_cat) < 7:
        return none

    cat1 = info[info['my_category'] == top_cat[0]].to_json(orient = "records")
    cat2 = info[info['my_category'] == top_cat[1]].to_json(orient = "records")
    cat3 = info[info['my_category'] == top_cat[2]].to_json(orient = "records")
    cat4 = info[info['my_category'] == top_cat[3]].to_json(orient = "records")
    cat5 = info[info['my_category'] == top_cat[4]].to_json(orient = "records")
    cat6 = info[info['my_category'] == top_cat[5]].to_json(orient = "records")
    cat7 = info[info['my_category'] == top_cat[6]].to_json(orient = "records")
    cat8 = info[~info['my_category'].isin(top_cat)].to_json(orient = "records")

    return jsonify({"result":[cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8], 
                    "visualization": final,"top_category": top_cat, 
                    "top_count": top_count})


@app.route('/kmean.json', methods=['POST'])
def kmean():
    """Visualize KMean Clusterings"""
    clusters = kmean_clusters()
    total_cluster = clusters.to_json(orient = "records")

    cluster_layers = []
    top_cats = []

    for z in range(0,4):
        c_layer = clusters[clusters['clustering'] == z]
        top_count = c_layer['review_count'].quantile(q=0.98)
        top_cat = c_layer.groupby(['my_category']).size().sort_values(ascending=False).head(7).index.tolist()
        data_top_cat = c_layer[c_layer['my_category'].isin(top_cat)].groupby(['price','my_category']).size()
        dict1 = data_top_cat.to_dict()
        l1,l2,l3,l4 = {}, {}, {}, {}
        for j in top_cat:
            l1[j] = 0
            l2[j] = 0
            l3[j] = 0
            l4[j] = 0
        for i in dict1:
            if str(i[0]) == '$':
                l1[i[1]] = dict1[i]
            elif str(i[0]) == '$$':
                l2[i[1]] = dict1[i]
            elif str(i[0]) == '$$$':
                l3[i[1]] = dict1[i]
            elif str(i[0]) == '$$$$':
                l4[i[1]] = dict1[i]
        
        final = [['$',l1],['$$',l2],['$$$',l3],['$$$$',l4]]
        top_cats.append(top_cat)
        cluster_layers.append(final)

    # clusters = clusters.to_json(orient = "records")

    return jsonify({'cluster': total_cluster,
                    'cluster_layer': cluster_layers,
                    'top_cat': top_cats})



if __name__ == "__main__":
    app.debug = False
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=5000, host='127.0.0.1')

