from flask import Flask, render_template, request, jsonify
from constant import TOKEN, APP_SECRETE
from flask_debugtoolbar import DebugToolbarExtension
import json
from is_within_polygon import pointInPolygon

app = Flask(__name__)

app.secret_key = APP_SECRETE

@app.route("/", methods=['GET'])
def home():
    """Home Page"""

    return render_template("map4.html", token=TOKEN)

@app.route("/", methods=['POST'])
def dis_restaurants():
    """Display the restaurants within the polygon region"""

    data = json.loads(request.form.get("data"))
    polyY = [float(lat.get('lat')) for lat in data]
    polyX = [float(lng.get('lng')) for lng in data]
    drawpoints = []
    with open('location.csv') as f:
        for line in f:
            line = line.rstrip().split(',')
            x = float(line[1])
            y = float(line[0])
            print pointInPolygon(len(polyY), polyY, polyX, x, y )
            if pointInPolygon(len(polyY), polyY, polyX, x, y ):
                drawpoints.append((x,y))
        print drawpoints

    
    
    return jsonify({"result":"the result"})
    # polygon_points = re /quest.form.get("")


if __name__ == "__main__":
    app.debug = True
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=5000, host='0.0.0.0')

