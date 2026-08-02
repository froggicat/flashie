from flask import Flask, render_template

app = Flask(__name__)

# TODO(you): fill this list with 3–5 real spec-point titles from a subject
# you're revising (history topics, biology, maths — anything). Just strings.
SPEC_POINTS = [
    # your entries go here
    "Particles and radiation",
    "Waves",
    "Mechanics and materials",
    "Electricity",
]


@app.route("/")
def home():
    # TODO(you): pass SPEC_POINTS into the template as a keyword argument
    # named `spec_points` (add it as a second argument to render_template).
    return render_template("home.html", spec_points=SPEC_POINTS)
