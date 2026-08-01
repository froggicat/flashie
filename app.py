from flask import Flask

app = Flask(__name__)


@app.route("TODO(you): the URL path this route handles — see plan.md §1.5 deliverable")
def home():
    return "TODO(you): the exact string the browser should see — same source"
