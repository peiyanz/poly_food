from flask import Flask, render_template
from constant import TOKEN, APP_SECRETE


app = Flask(__name__)

app.secret_key = APP_SECRETE

@app.route("/")
def home():
    """Home Page"""

    return render_template("map4.html", token=TOKEN)

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')