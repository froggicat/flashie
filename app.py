from flask import Flask, render_template, request, redirect, url_for
from db import load_spec_tree, get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", spec_points=load_spec_tree())

@app.route("/spec/<int:id>", methods=["GET", "POST"])
def spec_point(id):
    if request.method == "POST":
        front = request.form["front"]
        back = request.form["back"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cards (spec_point_id, front, back) VALUES (?, ?, ?)",
            (id, front, back),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("spec_point", id=id))

    conn = get_connection()
    cursor = conn.cursor()

    # gets the title to display at the top
    cursor.execute('SELECT title FROM spec_points WHERE id = ?', (id,))
    row = cursor.fetchone()

    # gets the front and back of created cards for that specific spec point
    cursor.execute("""
        SELECT front, back FROM cards WHERE spec_point_id = ?
    """, (id,))
    cards = cursor.fetchall()
    conn.close()

    return render_template(
        "spec_point.html",
        title=row["title"],
        cards=cards,
    )
