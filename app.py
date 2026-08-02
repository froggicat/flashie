from flask import Flask, render_template
from specs import SPEC_POINTS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", spec_points=SPEC_POINTS)
