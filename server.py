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
    # print data
    polyY = [float(lat.get('lat')) for lat in data]
    polyX = [float(lng.get('lng')) for lng in data]
    drawpoints = []
    with open('location.csv') as f:
        for line in f:
            line = line.rstrip().split(',')
            x = float(line[1])
            y = float(line[0])
            if pointInPolygon(len(polyY), polyY, polyX, x, y ):
                drawpoints.append([x,y])
            # line = line.rstrip().split(',')
            # print line
            # x = float(line[2])
            # y = float(line[1])
            # if pointInPolygon(len(polyY), polyY, polyX, x, y ):
            #     business_id = line[0]
            #     name = line[6]
            #     rating = line[3]
            #     review_count = line[4]
            #     category = line[5]
            #     drawpoints.append({'business_id': business_id,
            #                        'name': name,
            #                        'latlng': [x,y],
            #                        'rating': rating,
            #                        'review_count': review_count,
            #                        'category': category})


    return jsonify({"result":drawpoints})



if __name__ == "__main__":
    app.debug = True
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=5000, host='0.0.0.0')

