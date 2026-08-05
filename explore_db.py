"""Task 4.5 — add empty cards + reviews tables (don't wipe spec_points!).
Run:  python explore_db.py
"""
import sqlite3

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""CREATE TABLE IF NOT EXISTS cards(
    id INTEGER PRIMARY KEY,
    spec_point_id INTEGER NOT NULL, 
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    FOREIGN KEY (spec_point_id) REFERENCES spec_points(id)
)""")
# TODO(you): CREATE TABLE reviews with at least:
#   id          INTEGER PRIMARY KEY
#   card_id     INTEGER NOT NULL, FK → cards(id)
#   rating      INTEGER NOT NULL
#   next_due_at TEXT NOT NULL
#   (TEXT for the timestamp is fine for v1 — ISO strings later)
# CREATE TABLE IF NOT EXISTS again.

cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY,
    card_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    next_due_at TEXT NOT NULL,
    FOREIGN KEY (card_id) REFERENCES cards(id)
    )
""")

connection.commit()

# TODO(you): print all table names from sqlite_master.
# Expect: spec_points, cards, reviews.
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
print(cursor.fetchall())
# TODO(you): print COUNT(*) from cards and from reviews — both should be 0.
cursor.execute("SELECT COUNT(*) FROM cards")
print(cursor.fetchone())
cursor.execute("SELECT COUNT(*) FROM reviews")
print(cursor.fetchone())

connection.close()
