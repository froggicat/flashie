from flask import Flask, render_template, request, redirect, url_for, Response
from db import load_spec_tree, get_connection
from scheduler import next_due_at
from datetime import datetime
import os

app = Flask(__name__)


@app.before_request
def real_auth_check():
    password=os.environ.get("APP_PASSWORD")
    auth=request.authorization
    if auth and auth.password==password:
        return
    else:
        return Response("Wrong password.", 401, {"WWW-Authenticate": 'Basic realm="Spec Companion"'})

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


@app.route("/study", methods=["GET","POST"])
def study():
    conn = get_connection()
    cursor = conn.cursor()

    # .get returns None if the browser didn't send that key.
    raw_id = request.args.get("spec_point")

    if request.method == "POST":
        card_id = int(request.form["card_id"])
        spec_point = request.form["spec_point"]
        rating = int(request.form["rating"])
        reviewed_at = datetime.now().isoformat()

        cursor.execute(
            "INSERT INTO reviews (card_id, rating, next_due_at, reviewed_at) VALUES (?, ?, ?, ?)",
            (card_id, rating, next_due_at(rating, datetime.now()), reviewed_at),
        )

        conn.commit()
        conn.close()
        return redirect(url_for("study", spec_point=spec_point))

    if raw_id == None:
        return "Pick a spec point: /study?spec_point=<id>"

    raw_id = int(raw_id)

    cursor.execute("SELECT title FROM spec_points WHERE id = ?", (raw_id,))
    output = cursor.fetchone()
    if output == None:
        conn.close()
        return "No specification point with that ID"

    cursor.execute("""
        SELECT id, front, back FROM cards
        WHERE spec_point_id = ?
        AND id NOT IN (SELECT card_id FROM reviews WHERE next_due_at > ?)
        LIMIT 1""",
        (raw_id, datetime.now().isoformat()),
    )
    card = cursor.fetchone()
    conn.close()

    if card == None:
        #fix properly !!
        return render_template("home.html")
    else:
        return render_template("study.html", title=output["title"], card=card, spec_point_id=raw_id)


@app.route("/coverage")
def coverage():
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now().isoformat()

    cursor.execute("""
        SELECT
            sp.id,
            sp.title,
            COUNT(c.id) AS card_count,
            (
                SELECT COUNT(*)
                FROM cards
                WHERE spec_point_id = sp.id
                AND id NOT IN (
                    SELECT card_id FROM reviews WHERE next_due_at > ?
                )
            ) AS due_count,
            (
                SELECT MAX(r.reviewed_at)
                FROM reviews AS r
                JOIN cards AS c2 ON c2.id = r.card_id
                WHERE c2.spec_point_id = sp.id
            ) AS last_reviewed
        FROM spec_points AS sp
        LEFT JOIN cards AS c ON c.spec_point_id = sp.id
        GROUP BY sp.id
        ORDER BY sp.id
    """, (now,))

    rows = cursor.fetchall()
    conn.close()

    return render_template("coverage.html", rows=rows)
