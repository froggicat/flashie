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

cursor.execute("ALTER TABLE REVIEWS ADD COLUMN reviewed_at TEXT")

connection.commit()

cursor.execute("SELECT sql FROM sqlite_master WHERE name='reviews'")
print(cursor.fetchone())

connection.close()
