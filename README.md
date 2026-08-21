# Spec Companion

A personal flashcard app for A-level revision. Every card is attached to a point in an official exam specification, so you can see what you’ve covered and what still has gaps.

Built as a single-user Flask app I can use from a phone, a Chromebook, or a laptop. Not a shared deck marketplace — just a revision tool tied to the spec.

## Why

Generic flashcard decks are rarely aligned to the exam board spec. Homemade Anki decks take ages to organise. Spec Companion keeps cards under the spec tree itself, then shows coverage at a glance: how many cards each point has, how many are due, and when it was last reviewed.

## What it does

- **Spec tree** (`/`) — nested exam-spec topics, expand/collapse, click through to a point
- **Add cards** (`/spec/<id>`) — front and back, stored against that spec point
- **Study** (`/study?spec_point=<id>`) — one due card at a time; Space (or tap) to flip; rate 1–5
- **Coverage** (`/coverage`) — card count, due count, last reviewed; empty points highlighted
- **HTTP basic auth** — one password from an environment variable, so a public URL stays private

Scheduling is deliberately simple: `next_due_at = now + rating² days`. Rating 3 comes back in 9 days; rating 5 in 25.

The current spec file (`specs/physics.json`) is a nested JSON tree — edit it, then re-seed the database. Right now it holds Computer Science cyber-security topics for real revision use.

## Stack

| Piece | Choice |
|---|---|
| Backend | Python + Flask |
| Database | SQLite (`db.sqlite`) |
| Templates | Jinja2 |
| Frontend | Server-rendered HTML, one CSS file, vanilla JS |
| Tests | pytest |
| Auth | HTTP basic auth via `APP_PASSWORD` |

No frontend build step, no extra frameworks.

## Run locally

Python 3.12+ recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create the database (tables are not created automatically on first run). In a Python shell or DB Browser for SQLite:

```sql
CREATE TABLE spec_points (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES spec_points(id)
);

CREATE TABLE cards (
    id INTEGER PRIMARY KEY,
    spec_point_id INTEGER NOT NULL,
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    FOREIGN KEY (spec_point_id) REFERENCES spec_points(id)
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    card_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    next_due_at TEXT NOT NULL,
    reviewed_at TEXT,
    FOREIGN KEY (card_id) REFERENCES cards(id)
);
```

Then seed the spec tree and start the app:

```bash
python import_spec.py

export APP_PASSWORD='choose-a-password'
flask run
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000). The browser will prompt for a username and password — username can be anything; the password must match `APP_PASSWORD`.

`db.sqlite` and `.env` are gitignored so cards and the password stay off GitHub.

### Docker

```bash
docker build -t flashie .
docker run --rm -p 5000:5000 -e APP_PASSWORD='choose-a-password' flashie
```

You’ll still need a seeded `db.sqlite` in the image or mounted in, or the spec tree will be empty.

## Tests

```bash
source .venv/bin/activate
export APP_PASSWORD='test'
pytest
```

Scheduler unit tests plus smoke tests for `/`, `/coverage`, `/study`, and `/spec/<id>`.

## Project layout

```
app.py              Flask routes (home, spec, study, coverage, auth)
db.py               SQLite connection + rebuild of the spec tree
scheduler.py        next_due_at(rating, now)
import_spec.py      loads specs/physics.json into spec_points
specs/physics.json  nested spec tree
templates/          Jinja pages
static/             CSS + tree/study JavaScript
tests/              pytest
```

## Status

v1 is usable end-to-end: spec → cards → study → coverage, with auth and a phone-readable layout. Hosted on PythonAnywhere for everyday revision.

Not in this version (on purpose): real SM-2/FSRS, LaTeX, images, multi-subject, user accounts, or sharing decks.
