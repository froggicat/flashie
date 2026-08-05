from flask import Flask, render_template
from db import load_spec_tree

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", spec_points=load_spec_tree())
