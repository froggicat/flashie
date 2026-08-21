import json
import sqlite3

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

data = json.load(open("specs/specification.json"))


cursor.execute("PRAGMA foreign_keys = OFF")
cursor.execute("DELETE FROM spec_points")
cursor.execute("PRAGMA foreign_keys = ON")

def insert_node(node, parent_id):
    """Insert one node, then recursively insert its children."""
    cursor.execute(
        "INSERT INTO spec_points (title, parent_id) VALUES (?, ?)",
        (node["title"], parent_id),  # replace with the two real values
    )

    new_id = cursor.lastrowid

    for child in node["children"]:
        insert_node(child, new_id)

    
for node in data:
    insert_node(node, None)

connection.commit()

cursor.execute("SELECT id, title, parent_id FROM spec_points")
print(cursor.fetchall())

connection.close()
