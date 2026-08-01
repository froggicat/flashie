# Spec Companion — Learning-First Build Plan

Read this file *after* `project.md`. `project.md` says what we're building; this file says how we'll build it, in what order, and — crucially — *why* each tool was picked.

Speed of delivery is not the goal. **Understanding is the goal.** By the end of this project, I should be able to explain how my app works end to end without waving hands at any piece.

---

## Locked decisions

Each decision below was arrived at by walking through the popular boring choice, comparing it against 1–2 alternatives with real trade-offs, and checking that I could explain in my own words why the pick fits *this project at this stage*.

### 1. Language — **Python**

Chosen because I already know it. This project isn't "learn Python", it's "learn what happens *around* a Python program to turn it into a real deployed web app". Every hour spent fighting language syntax is an hour not spent on routing, databases, or deployment.

*When it would stop being right:* rarely. Language is the least likely thing to force a rewrite — Python has web frameworks for every ambition level. I'd only leave Python if I needed a language-specific runtime (e.g. Rust for very high performance).

### 2. Backend framework — **Flask**

Chosen because it exposes HTTP directly, has a tiny surface area (a "hello world" is 5 lines), ships with the Jinja template engine, and is the default teaching framework — so every tutorial online defaults to it.

*Considered:* Django (too many built-in conventions to learn on top of the actual concepts; hides HTTP), FastAPI (great for JSON APIs, but wrong shape for a server-rendered HTML app).

*When it would stop being right:* when the app has 50+ routes and I want an admin panel + ORM (Django), or when the frontend becomes a separate SPA and Flask is just an API layer (FastAPI).

### 3. Database — **SQLite**

Chosen because it's zero-setup (part of the Python standard library), the whole database lives in one file on disk, and it's genuinely a good production choice for a single-user app like this. The SQL I learn is portable.

*Considered:* PostgreSQL (industrial-strength but requires a separate server process, adding install/config friction while learning), MongoDB (wrong shape — my data is inherently relational).

*When it would stop being right:* when there are many concurrent writers, or when the app scales past a single VM and needs a database that lives on a separate machine.

### 4. Frontend approach — **Server-rendered HTML (Jinja) + plain CSS + vanilla JavaScript. No build step, no framework.**

Chosen because it has no build step (no npm, no bundler), keeps the mental model tiny (one HTTP request → one HTML response), and lets me use the JS I already know without learning a component framework first. View-source shows exactly what got sent.

*Considered:* React/Vue/Svelte (would double the project — two toolchains, two mental models, and none of the added complexity teaches web fundamentals), htmx (elegant, but one more concept on top of Jinja for v1; natural next step if v2 needs partial page updates).

*When it would stop being right:* htmx as soon as I'm reloading whole pages just to update one section. React only if the UI becomes genuinely rich-interactive (drag-and-drop, real-time canvas, complex client-side state).

### 5. Hosting — **Fly.io + Docker**

Chosen because Fly's free tier includes persistent volumes (which SQLite needs to survive restarts), it deploys from git, and Docker is a career-long skill I'll use on every future project. Requires a payment method on file; using a virtual/prepaid card and setting billing alerts keeps that safe.

*Considered:* Render (no persistent disk on free tier — would force us off SQLite), PythonAnywhere (free without a card, but no Docker learning), Vercel (aimed at frontend/serverless — poor fit for a Flask app with a persistent SQLite file).

*When it would stop being right:* when I'm running multiple services that need proper orchestration, when traffic warrants dedicated infra, or when I want a fully managed platform and don't mind paying.

---

## Build plan — 9 sections, each ending in a concrete deliverable

Each section builds on the last. Each ends with something visibly working. I do not skip sections. If I get stuck mid-section, I ask for help *inside that section* — I do not jump ahead.

### Section 1 — Foundations & first server

**What I'll learn:** git basics (init, commit, push), GitHub, virtual environments (`venv`), `pip`, `requirements.txt`, the minimum Flask app.

**Deliverable:** `flask run` on my laptop → open `localhost:5000` → see a page that says "Spec Companion". The whole project is a GitHub repo with clean, meaningful commits.

**Why first:** everything else assumes a working local Python + Flask + git setup. If any of those are shaky, every future section is harder than it needs to be.

**Tasks** (each ends in something visibly working):

- [x] **1.1 — Turn this folder into a git repo & commit the planning docs.** Visible: `git log --oneline` shows one commit; `git status` clean. *Done 2026-08-01: commit `8eb21de` on `main` ("initial commit! very exciting"), tree clean.*
- [x] **1.2 — Create & activate a Python virtual environment.** Visible: shell prompt shows `(.venv)`; `which python` points inside `.venv`. *Done 2026-08-01: `.venv/` created with `python3 -m venv .venv`; `which python` → `~/flashcard-app/.venv/bin/python`. Toured `bin/`, `lib/`, `pyvenv.cfg`; parked `include/` + `lib64`.*
- [x] **1.3 — Install Flask & pin it in `requirements.txt`.** Visible: `requirements.txt` exists with pinned versions; `pip list` shows Flask; committed. *Done 2026-08-01: `pip install flask` installed 7 packages (Flask + 6 transitive deps); `pip freeze > requirements.txt` captured them all with `==` pins; committed as `dbe1281`.*
- [x] **1.4 — Write `app.py` — a minimum Flask app with one route returning "Spec Companion".** Visible: file exists, imports without error. *Done 2026-08-01: 4-line minimum app (import → instance → `@app.route("/")` → `home()` returning "Spec Companion"). `python -c "import app"` returned silence.*
- [ ] **1.5 — Run `flask run` and see "Spec Companion" at `localhost:5000` in a browser.** Visible: the page renders; committed.
- [ ] **1.6 — Create a GitHub repo and push.** Visible: the repo loads on github.com and shows the commits.

### Section 2 — Your first data-driven page

**What I'll learn:** Jinja templates, `render_template`, the standard Flask folder structure (`templates/`, `static/`), how a Python data structure becomes HTML in a response.

**Deliverable:** a page at `/` that renders a hardcoded Python list of spec points as a nested HTML tree. No database yet — the data lives in a Python variable — but the templating is real.

**Why now:** learning templating in isolation, before adding the complexity of a database, keeps the concepts separate in my head.

### Section 3 — Styling and small interactivity

**What I'll learn:** how Flask serves static files, layout with plain CSS, a `base.html` template that other pages extend, one `style.css`, vanilla JS event listeners (expand/collapse the spec tree).

**Deliverable:** the spec tree from Section 2 is now readable and clickable — I can expand/collapse subtrees. It doesn't look like a 1998 web page.

**Why now:** the app is still small, so I can build up CSS and JS incrementally rather than trying to retro-fit them onto a bigger app later.

### Section 4 — The database, wired in properly

**What I'll learn:** designing a schema, `CREATE TABLE`, foreign keys, self-referential trees (`parent_id`), running SQL from Python via the `sqlite3` module, seeding data from JSON.

**Deliverable:** `db.sqlite` exists, populated from `specs/<subject>.json` via a `import_spec.py` script. The Section 3 page now reads from SQLite — but looks and behaves identically to the user. I can open the DB in DB Browser for SQLite and explain every table, column, and row.

**Why now:** the swap from "data in a Python list" to "data in SQLite" is small and self-contained. Doing this before adding new features means I'm never *both* learning the database *and* building a new feature at the same time.

### Section 5 — Core feature: adding cards

**What I'll learn:** HTML forms, GET vs POST, `request.form`, `INSERT` statements, foreign keys in action (a card belongs to exactly one spec point).

**Deliverable:** I can click any spec point, see a form, add a card (front + back), and see it listed under that spec point on refresh. I end this section having hand-authored ~10 real cards for my chosen subject.

**Why now:** this is the first real feature. It's small — form + POST + INSERT + list — but it exercises the full stack for the first time.

### Section 6 — Core feature: study mode + scheduler

**What I'll learn:** query parameters (`?spec_point=<id>`), selecting rows in Python from a database query, writing to a `reviews` table, a pure-function scheduler in its own `scheduler.py` module, keyboard event handlers in JS.

**Deliverable:** I use `/study?spec_point=<id>` for a real 20-minute revision session. One card at a time. Space to flip. 1–5 to rate. Each rating writes a `reviews` row and sets `next_due_at`.

**Why now:** this is the *point* of the app. Doing it after cards exist means I have real cards to study with, not lorem-ipsum test cards.

### Section 7 — Core feature: coverage dashboard

**What I'll learn:** aggregation SQL (`COUNT`, `GROUP BY`, `MAX`), building a summary view from multiple tables, template loops with conditional styling (highlight zero-card spec points).

**Deliverable:** open `/coverage` and see, for every spec point in my chosen subject: total cards, cards due today, when it was last reviewed, zero-card points highlighted. I can look at it and instantly answer "what should I revise next?"

**Why now:** this closes the loop the app promises — spec-aligned coverage. Without it, the app is just Anki-with-extra-steps.

### Section 8 — Tests

**What I'll learn:** what `pytest` is, why pure functions are easier to test than side-effect-heavy code, unit tests (for the scheduler) vs route smoke tests (for the Flask endpoints), running tests locally with one command.

**Deliverable:** `pytest` runs green. At minimum: unit tests for the scheduler function (a handful of input/output cases) and smoke tests for each route (returns 200, expected content in the response).

**Why now (and not earlier):** I now have three features worth testing and one pure function (the scheduler) that is *ideal* for demonstrating unit tests. Testing before this would be testing very little.

### Section 9 — Auth + deployment

**What I'll learn:** HTTP basic auth via Flask's `before_request` hook, environment variables and secrets management, Dockerfile basics (base image, install layer, copy code, entrypoint), `fly.toml`, mounted volumes, `flyctl deploy`, one CSS media query for mobile.

**Deliverable:** I open the deployed URL from my phone during a free period at school. Log in once with my password. Add a card. Study it. Every part of the app is now running on Fly.io, not my laptop.

**Why last:** deployment is where every previous section's decisions come home to roost. Doing it earlier means every bug is *both* an app bug *and* an infra bug, which is confusing while learning.

---

## After Section 9

Straight from `project.md`: **stop building for a week.** No code changes during that week. Use the deployed app for one week of real revision. Keep an `IDEAS.md` of frictions I actually hit — not what I *think* would be nice. Then pick the *single* next feature from the parking lot in `project.md`.

## How to use this file in future sessions

- If I'm partway through a section, the section header is my current "you are here" marker.
- If I want to change a locked decision, I *say so explicitly* and update this file first — I don't quietly drift.
- Every section's deliverable is a checkpoint I should be able to demo. If I can't demo it, the section isn't done.
- End-of-project self-test: can I explain, out loud, what happens between typing a URL in my phone browser and seeing a card on screen? If yes, I've achieved the goal. If not, I revisit the specific section that covers the piece I'm hazy on.
