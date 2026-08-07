import sqlite3

DB_PATH = "db.sqlite"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # rows act like dicts: row["title"]
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def load_spec_tree():
    """Return the same shape as SPEC_POINTS: list of {title, children}."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title, parent_id FROM spec_points
    """)
    rows = cursor.fetchall()

    conn.close()

    # --- rebuild nested tree from flat rows ---
    # Idea:
    # 1. Make a dict: nodes_by_id[id] = {"title": ..., "children": []}
    # 2. Walk every row again:
    #      - if parent_id is None → it's a root → append to roots list
    #      - else → append this node onto nodes_by_id[parent_id]["children"]
    # 3. Return roots

    nodes_by_id = {}
    roots = []

    #fill nodes_by_id from rows
    for row in rows:
        nodes_by_id[row["id"]] = {"id" : row["id"], "title" : row["title"], "children" : []}

    #link children / collect roots 
    for row in rows:
        node = nodes_by_id[row["id"]]
        if row["parent_id"] == None:
            roots.append(node)
        else:
            nodes_by_id[row["parent_id"]]["children"].append(node)

    return roots  # should match what SPEC_POINTS looked like
