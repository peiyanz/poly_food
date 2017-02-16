from flask import Flask, render_template, request, jsonify
from constant import TOKEN, APP_SECRETE
from flask_debugtoolbar import DebugToolbarExtension
import json
# from yelp_api import rectangle
from yelp_api_v3 import api_call
from data import rest_in_poly
from math import sin, cos, sqrt, atan2, radians


app = Flask(__name__)

app.secret_key = APP_SECRETE

@app.route("/", methods=['GET'])
def home():
    """Home Page"""

    return render_template("map4.html", token=TOKEN)

@app.route("/", methods=['POST'])
def dis_restaurants():
    """Display the restaurants within the polygon region"""
#Old Way of doing it
    # data = json.loads(request.form.get("data"))
    # # print data
    # polyY = [float(lat.get('lat')) for lat in data]
    # polyX = [float(lng.get('lng')) for lng in data]
    # drawpoints = []
    # with open('location.csv') as f:
    #     for line in f:
    #         line = line.rstrip().split(',')
    #         x = float(line[1])
    #         y = float(line[0])
    #         if pointInPolygon(len(polyY), polyY, polyX, x, y ):
    #             drawpoints.append([x,y])

    # return jsonify({"result":drawpoints})

#New way of doing it

    data = json.loads(request.form.get("data"))
    offset = json.loads(request.form.get("offset"))
    polyY = [float(lat.get('lat')) for lat in data]
    polyX = [float(lng.get('lng')) for lng in data]
    # polySides = len(polyY)

    l2 = min(polyX)
    l1 = min(polyY)
    l4 = max(polyX)
    l3 = max(polyY)
    # print "point one"
    # print (l1, l2)
    # print "point two"
    # print (l3,l4)

    longitude = (l2+l4)/2
    latitude = (l1+l3)/2
# (lon2 - lon1) * cos( 0.5*(lat2+lat1) )
# y = lat2 - lat1
    

# approximate radius of earth in km
    R = 6373.0
    # 37.7774552846754, -122.4076447741966)
    # (37.78516819634882, -122.39234039009025)
    lat1 = radians(l1)
    lon1 = radians(l2)
    lat2 = radians(l3)
    lon2 = radians(l4)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c*1000

    # print("Result:", distance)


    radius = int(distance/2)
    # radius = int(great_cicle((l1,l2),(l3,l4)).meters)
    if radius > 40000: #maximum range of the polygon
        radius = 39999
    # print longitude
    # print latitude
    # print radius

    # rest_info = rectangle(l1,l2,l3,l4, offset)
    rest_info = api_call(latitude, longitude, radius, offset)

    if rest_info.empty:
        return jsonify({"result":"No result"})
    else:
        info_json = rest_in_poly(polyY, polyX, rest_info)

    # info_json = rest_in_poly(polyY, polyX) #another test
        return jsonify({"result":info_json})
    # return

    

        

if __name__ == "__main__":
    app.debug = True
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=5000, host='127.0.0.1')

