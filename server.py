from flask import Flask, render_template, request, jsonify
from constant import TOKEN, APP_SECRETE
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.secret_key = APP_SECRETE

@app.route("/", methods=['GET'])
def home():
    """Home Page"""

    return render_template("map4.html", token=TOKEN)

@app.route("/", methods=['POST'])
def dis_restaurants():
    """Display the restaurants within the polygon region"""
    print "expecting array of array"
    # raise Exception 
    print request.form.get('features')
    # raise Exception 
    return jsonify({"result":"the result"})
    # polygon_points = re /quest.form.get("")


if __name__ == "__main__":
    app.debug = True
    # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(port=5000, host='0.0.0.0')

