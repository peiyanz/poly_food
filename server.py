from flask import Flask, render_template, request, jsonify
from constant import TOKEN, APP_SECRETE
from flask_debugtoolbar import DebugToolbarExtension
import json
from yelp_api import rectangle
from data import rest_in_poly


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

    rest_info = rectangle(l1,l2,l3,l4, offset)
    info_json = rest_in_poly(polyY, polyX, rest_info)
    # info_json = rest_in_poly(polyY, polyX) #another test
    return jsonify({"result":info_json})
    # return

if __name__ == "__main__":
    app.debug = True
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=5000, host='127.0.0.1')

