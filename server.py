from flask import Flask, render_template, request, jsonify
from constant import TOKEN, APP_SECRETE
from flask_debugtoolbar import DebugToolbarExtension
import json
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
    polyY = [float(lat.get('lat')) for lat in data]
    polyX = [float(lng.get('lng')) for lng in data]
    polySides = len(polyY)
    info_json = rest_in_poly(polySides, polyY, polyX)
    return jsonify({"result":info_json})

if __name__ == "__main__":
    app.debug = True
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=8080, host='0.0.0.0')

