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
- [x] **1.5 — Run `flask run` and see "Spec Companion" at `localhost:5000` in a browser.** Visible: the page renders; committed. *Done 2026-08-01: dev server started, `/` returned "Spec Companion" (200), `/study` returned 404. Commits `788b805` (learning docs) + `1e53d3e` (app.py).*
- [x] **1.6 — Create a GitHub repo and push.** Visible: the repo loads on github.com and shows the commits. *Done 2026-08-01 solo (first fully-independent task): `github.com/froggicat/flashcard-app` created, `origin` wired via SSH, 5 commits pushed, `main` tracks `origin/main`.*

**Section 1 complete 2026-08-01.** Deliverable met: `flask run` on laptop → `localhost:5000` shows "Spec Companion"; whole project is a GitHub repo with clean, meaningful commits.

### Section 2 — Your first data-driven page

**What I'll learn:** Jinja templates, `render_template`, the standard Flask folder structure (`templates/`, `static/`), how a Python data structure becomes HTML in a response.

**Deliverable:** a page at `/` that renders a hardcoded Python list of spec points as a nested HTML tree. No database yet — the data lives in a Python variable — but the templating is real.

**Why now:** learning templating in isolation, before adding the complexity of a database, keeps the concepts separate in my head.

**Tasks** (each ends in something visibly working):

- [x] **2.1 — First real template.** Swap `home()`'s string return for `render_template("home.html")` and put a real HTML page at `templates/home.html`. Visible: `/` still greets you, but *view-source* shows a full HTML document (`<html>…</html>`), not plain text. *Done 2026-08-02: added `render_template` to Flask import, swapped return. Learned by failure first — hit `/` with no template → 500 + `jinja2.exceptions.TemplateNotFound: home.html` at 18:01:54. Created `templates/home.html` (DOCTYPE + html/head/body/title/h1) → same URL returned 200 at 18:07:28. Articulated import-time vs request-time distinction unprompted.*
- [x] **2.2 — Render a flat Python list.** Add a hardcoded Python list of spec-point titles in `app.py`; pass it into the template; render as a `<ul>`. Introduces `{{ }}` and `{% for %}`. Visible: browser shows a bulleted list of the titles. *Done 2026-08-02 in three cycles: (A) add `SPEC_POINTS` list + `spec_points=SPEC_POINTS` kwarg — page unchanged (template didn't reference the var). (B) add `<p>{{ spec_points }}</p>` — page shows Python list repr `['Particles and radiation', 'Waves', 'Mechanics and materials', 'Electricity']`. (C) replace with `<ul>` + `{% for spec_point in spec_points %}<li>{{ spec_point }}</li>{% endfor %}` — proper bulleted list. En-route debug detours: template caching in non-debug Flask (fix: `flask run --debug`) and Jinja parser reading `{{ }}` inside HTML comments (fix: use `{# #}` instead).*
- [x] **2.3 — Nest one level.** Turn each spec point into `{"title": ..., "children": [...]}`; render a two-level `<ul>`. Introduces `{% if %}`. Visible: parents with children show a nested list underneath. *Done 2026-08-02 in two cycles: (A) reshaped `SPEC_POINTS` to list-of-dicts with `title`+`children` (Electricity intentionally childless), swapped `<li>{{ spec_point }}</li>` for `<li>{{ spec_point.title }}</li>`. Predicted incorrectly ("4 parents + children under each") then self-corrected instantly by re-applying the explicit-only-rendering principle. (B) added a nested `<ul>` inside each `<li>`, guarded by `{% if spec_point.children %}` and populated by an inner `{% for child in spec_point.children %}`. Predicted both cases right — nested list for the 3 filled parents, nothing (not even `<ul></ul>`) for Electricity. Bonus real-world observation: nested `<ul>` uses hollow-circle bullets by default (browser CSS list-style-type). Meta-move: turned off tab-complete mid-task to force real understanding.*
- [x] **2.4 — Make the tree template recursive.** Use a Jinja macro (or self-include) so any depth works. Add a 3-level example to prove it. Visible: a 3-deep spec point renders correctly using the same template block. *Done 2026-08-02 in two cycles: (A) restructured `SPEC_POINTS` so children are dicts with the same shape as parents (self-similar tree), added Alpha/Beta/Gamma as grandchildren of Radioactivity. Predicted correctly that grandchildren wouldn't appear (template still hardcoded to 2 levels). (B) refactored the entire `<ul>` block into a Jinja `{% macro render_tree(nodes) %}` that self-calls `{{ render_tree(node.children) }}` when a node has children; invoked once with `{{ render_tree(spec_points) }}` at the top. Predicted all three test cases correctly, including the deepest one: a hypothetical 4th nesting level would need zero template changes because "its recursive and just continues".*
- [x] **2.5 — Extract the spec data into `specs.py`.** Move the hardcoded list out of `app.py` and import it back in. Teaches multi-file Python. Visible: `app.py` is short again; `from specs import SPEC` at the top; page still renders identically. *Done 2026-08-02 unaided (Amalia explicitly asked for less scaffolding to build more herself). Authored `specs.py` from scratch (20-line `SPEC_POINTS` moved cleanly), added `from specs import SPEC_POINTS` to `app.py`, deleted the local definition — `app.py` down from 37 → 9 lines. Verified `__pycache__/specs.cpython-312.pyc` appeared on first import. Articulated the refactor rationale unprompted: separation of routing (app.py) from data (specs.py) = more readable & modular. Behaviour identical, structure improved — the definition of a refactor.*

**Section 2 complete 2026-08-02.** Deliverable met: `/` renders a hardcoded tree of spec points as a nested HTML list, arbitrarily deep, from a Python data structure — templating is real (Jinja `{{ }}`, `{% for %}`, `{% if %}`, recursive `{% macro %}`); no database yet; data lives in its own module.

### Section 3 — Styling and small interactivity

**What I'll learn:** how Flask serves static files, layout with plain CSS, a `base.html` template that other pages extend, one `style.css`, vanilla JS event listeners (expand/collapse the spec tree).

**Deliverable:** the spec tree from Section 2 is now readable and clickable — I can expand/collapse subtrees. It doesn't look like a 1998 web page.

**Why now:** the app is still small, so I can build up CSS and JS incrementally rather than trying to retro-fit them onto a bigger app later.

**Tasks** (each ends in something visibly working):

- [x] **3.1 — Wire up static CSS.** Create `static/style.css` and link it from `home.html` the Flask way (`url_for('static', …)`). Put one obviously-visible rule in the CSS (e.g. page background or heading colour). Visible: refresh `/` → the page no longer looks like plain browser defaults. *Done 2026-08-04: authored `static/style.css` (`body { background-color: pink; }`); first linked with relative `href="static/style.css"`; diagnosed blank page as "server not running" (nothing on :5000) after predicting connection refused correctly; switched to `{{ url_for('static', filename='style.css') }}` — stayed pink. Quiz: renaming `templates/` → 404/`TemplateNotFound` (correct).*
- [x] **3.2 — Make the tree readable.** Style the nested lists — spacing, indent, type hierarchy — so scanning parents vs children is easy. Visible: the spec tree is clearly nested and pleasant to read, still no interactivity. *Done 2026-08-04: replaced pink smoke-test with `#f2d8e7` body + Arial stack + margin; `h1` at `xx-large`; added `class="spec-item"` on each `<li>` in the macro and styled `.spec-item` margins. Quiz: `li` rules hit every nesting level (correct). Predicted correctly that static CSS needs only a browser refresh, not a Flask restart.*
- [x] **3.3 — Extract `base.html`.** Move the shared HTML shell into `templates/base.html`; make `home.html` `{% extends "base.html" %}` and fill a `{% block content %}`. Visible: page looks identical; view-source still a full document; `home.html` only owns the page-specific bits. *Done 2026-08-04: authored `base.html` (default title block + `url_for` CSS link + empty `content` block); `home.html` is now extends + `content` only (h1 + recursive macro). Verified child content appears. Quiz: view-source does *not* show Jinja tags (correct — server-side). Mis-predicted missing `<link>` → 500; actual = 200 unstyled — dug into 500-vs-missing-asset gap.*
- [x] **3.4 — Prepare the tree for toggling.** Update the recursive macro so each parent has a clickable control and its child `<ul>` can be shown/hidden (start collapsed). Visible: only top-level titles show; children are hidden until we add JS. *Done 2026-08-04: macro uses `{% if node.children %}` → `<button class="tree-toggle">` + recursive call, `{% else %}` → plain title (fixed Jinja `endif`/`else`/`endelse` tangle + `node . title` spacing). CSS `.spec-item > ul { display: none; }` hides nested lists only. Quiz selector B correct. Predicted C (top-level only) and saw it — clarified that *is* 3.4 done; nested HTML still in the response, just not painted.*
- [x] **3.5 — Expand/collapse with vanilla JS.** Add `static/tree.js`, load it from the template, wire click listeners that toggle a CSS class on the child list. Visible: click a parent → its subtree expands/collapses. *Done 2026-08-04: authored `tree.js` (`querySelectorAll` + `click` + `nextElementSibling` + `classList.toggle("is-open")`); linked via `url_for` before `</body>` in `base.html`; CSS show-rule first too weak (`.is-open` lost to `.spec-item > ul`), fixed to `.spec-item > ul.is-open` — specificity lesson. Quiz: URL helper is `url_for` (not "Jinja").*
- [x] **3.6 — Click affordances.** Add a caret (or equivalent) and hover/cursor styles so collapsed vs expanded is obvious without reading the code. Visible: deliverable met — readable, clickable tree that doesn't look like 1998. *Done 2026-08-04: de-defaulted `.tree-toggle` (no border/bg, `cursor: pointer`, purple hover); `::before` carets `▶`/`▼`; JS toggles `is-open` on button + ul. Hit `::before::before` typo (invalid) → fixed to `.tree-toggle.is-open::before`; caret flip confirmed. Also hid default bullets with `li { list-style: none; }`.*

**Section 3 complete 2026-08-04.** Deliverable met: spec tree is readable and clickable (expand/collapse with carets); styled via `static/style.css`; shared shell in `base.html`; interactivity in `static/tree.js`.

### Section 4 — The database, wired in properly

**What I'll learn:** designing a schema, `CREATE TABLE`, foreign keys, self-referential trees (`parent_id`), running SQL from Python via the `sqlite3` module, seeding data from JSON.

**Deliverable:** `db.sqlite` exists, populated from `specs/<subject>.json` via a `import_spec.py` script. The Section 3 page now reads from SQLite — but looks and behaves identically to the user. I can open the DB in DB Browser for SQLite and explain every table, column, and row.

**Why now:** the swap from "data in a Python list" to "data in SQLite" is small and self-contained. Doing this before adding new features means I'm never *both* learning the database *and* building a new feature at the same time.

**Tasks** (each ends in something visibly working):

- [x] **4.1 — First contact with SQLite.** From a short Python snippet (or the REPL), use the stdlib `sqlite3` module to create `db.sqlite` on disk and run a trivial `CREATE TABLE` + `INSERT` + `SELECT`. Visible: `db.sqlite` appears in the project folder; a query prints a row back. *Done 2026-08-05: authored `explore_db.py` (connect → cursor → CREATE `notes` → parameterized INSERT → commit → SELECT + print → close). First run looked like a no-op (forgot to save); after save, printed `[(1, 'hello sqlite')]`. Quiz: tightened table/row/column (row = one record, column = one field kind). Learned `execute` params are a tuple, not kwargs.*
- [x] **4.2 — Real schema: `spec_points`.** Design and `CREATE TABLE` the self-referential tree (`id`, `title`, `parent_id` FK to itself). Drop the toy table from 4.1. Visible: empty `spec_points` table exists; I can explain every column. *Done 2026-08-05: `DROP TABLE IF EXISTS notes`; `CREATE TABLE spec_points(id, title NOT NULL, parent_id, FOREIGN KEY → spec_points(id))`; `PRAGMA foreign_keys=ON`; printed `spec_points` in `sqlite_master`. Quiz: Alpha's grandparent chain — Radioactivity's parent is id 1 (correct).*
- [x] **4.3 — Spec as JSON.** Hand-write `specs/physics.json` matching the current tree (same data as today's `specs.py`). Visible: JSON file opens and mirrors the nested titles. *(Watch the name clash: `specs.py` module vs `specs/` folder — we handle it explicitly this task.)* *Done 2026-08-05: renamed `specs.py` → `spec_tree.py`, updated `app.py` import; authored `specs/physics.json` (4 top-level topics). Hit empty-on-disk until save; `json.load` then printed `4`. Clash verified: `from specs import …` fails, `spec_tree` works.*
- [x] **4.4 — Seed script `import_spec.py`.** Read the JSON, `INSERT` every node with the right `parent_id`. Visible: open the DB (Python or DB Browser) → all spec points are rows, parents link correctly. *Done 2026-08-05: recursive `insert_node`; learned tuple = values not quoted names; `lastrowid` property; 16 rows seeded; Alpha → parent_id 3 (Radioactivity). Base-case clarification: empty `children`, not `parent_id is None`.*
- [x] **4.5 — Create empty `cards` + `reviews` tables.** Full three-table schema from `project.md`, ready for §5/§6. Visible: `\tables` (or equivalent) shows all three; cards/reviews have zero rows. *Done 2026-08-05: `CREATE TABLE IF NOT EXISTS cards` (FK → spec_points) + `reviews` (FK → cards); fixed `sqlite_master` typo + split COUNTs; printed three tables and `(0,)` `(0,)`. Quiz: cards before reviews because reviews FK to cards (correct). spec_points data preserved.*
- [x] **4.6 — Home page reads from SQLite.** Rebuild the nested tree in Python from `spec_points` rows; `home()` uses that instead of `SPEC_POINTS`. Visible: `/` looks and behaves identically; `specs.py` can go. *Done 2026-08-05: authored `db.py` (`get_connection` + `load_spec_tree` with two-pass rebuild); `app.py` calls `load_spec_tree()`. Page identical ("thats crazy - its all the same"). `spec_tree.py` still on disk unused — safe to delete.*

**Section 4 complete 2026-08-05.** Deliverable met: `db.sqlite` holds `spec_points` (seeded from `specs/physics.json` via `import_spec.py`) plus empty `cards`/`reviews`; `/` renders the nested tree from SQLite and behaves like Section 3.

### Section 5 — Core feature: adding cards

**What I'll learn:** HTML forms, GET vs POST, `request.form`, `INSERT` statements, foreign keys in action (a card belongs to exactly one spec point).

**Deliverable:** I can click any spec point, see a form, add a card (front + back), and see it listed under that spec point on refresh. I end this section having hand-authored ~10 real cards for my chosen subject.

**Why now:** this is the first real feature. It's small — form + POST + INSERT + list — but it exercises the full stack for the first time.

**Tasks** (each ends in something visibly working):

- [x] **5.1 — Spec point has a URL.** Put each node's `id` into the tree from `load_spec_tree`; make titles link to `/spec/<id>`; stub route shows that point's title. Visible: click a topic → new URL + title on the page. *Done 2026-08-07: `id` on each tree node; `url_for('spec_point', id=…)` in macro (learned BuildError/500 when endpoint missing vs 404 after click); stub `@app.route("/spec/<int:id>")` + parameterized `SELECT title … WHERE id = ?` → `/spec/3` returns `Radioactivity`.*
- [x] **5.2 — List cards for a point.** Query `cards` for that `spec_point_id`; render a simple list (empty is fine). Visible: `/spec/<id>` shows a Cards section. *Done 2026-08-07: `templates/spec_point.html` (extends base, `{{ title }}` + `{% for card in cards %}`); route SELECTs title then `front, back FROM cards WHERE spec_point_id = ?`, passes both to template. `/spec/3` → Radioactivity + empty list (table still empty — predicted correctly).*
- [x] **5.3 — Add-card form.** HTML `<form method="POST">` with front + back fields on the spec page. Visible: form appears under the title. *Done 2026-08-07: `spec_point.html` form with `name="front"` / `name="back"` + submit. Predicted “won’t do anything” on submit → actual **405 Method Not Allowed** (POST sent; route is GET-only until 5.4).*
- [x] **5.4 — POST → INSERT → redirect.** Same route accepts POST, reads `request.form`, inserts a row, redirects to GET. Visible: submit → card shows in the list; refresh doesn't duplicate. *Done 2026-08-07: `methods=["GET","POST"]`; POST branch reads `request.form["front"/"back"]`, parameterized INSERT + commit, `redirect(url_for("spec_point", id=id))` (PRG). Verified 302 then list updates; refresh doesn't re-POST.*
- [x] **5.5 — Prove the FK/`WHERE`.** Add a card under point A; open point B — B does not show A's cards. Visible: each point only lists its own cards. *Done 2026-08-07: predicted correctly — `/spec/16` empty while `/spec/3` lists Radioactivity's cards; Electricity card wouldn't appear under Radioactivity. Verified: all 3 DB rows have `spec_point_id=3`; Electricity page empty `<ul>`.*
- [x] **5.6 — Hand-author ~10 real cards.** Use the UI for your subject. Visible: real study content in the DB; section deliverable met. *Done 2026-08-07: cleared `cards`, authored 10 GCSE Electricity cards via the form (current, p.d., meters, Ohm's law, series/parallel, etc.).*

**Section 5 complete 2026-08-07.** Deliverable met: click a spec point → form → add card (front + back) → listed under that point; ~10 real cards in SQLite for Electricity.

### Section 6 — Core feature: study mode + scheduler

**What I'll learn:** query parameters (`?spec_point=<id>`), selecting rows in Python from a database query, writing to a `reviews` table, a pure-function scheduler in its own `scheduler.py` module, keyboard event handlers in JS.

**Deliverable:** I use `/study?spec_point=<id>` for a real 20-minute revision session. One card at a time. Space to flip. 1–5 to rate. Each rating writes a `reviews` row and sets `next_due_at`.

**Why now:** this is the *point* of the app. Doing it after cards exist means I have real cards to study with, not lorem-ipsum test cards.

**Tasks** (each ends in something visibly working):

- [x] **6.1 — Study URL with a query param.** Add `/study` that reads `?spec_point=<id>` and shows that point's title (stub page). Visible: open `/study?spec_point=16` → see "Electricity" (or whatever that id is). *Done 2026-08-08: `request.args.get("spec_point")`; missing → message; bad id → message; `/study?spec_point=16` → `Electricity`. Corrected quiz (path vs query = URL job, not “DB vs list”); dug into 404≠no server and `fetchone()` → `None` vs crash; fixed `return f"{row}"` → `output["title"]`.*
- [x] **6.2 — Show one card's front.** Query cards for that spec point; pick one; render only the front on the study page. Visible: a real card front appears (back still hidden). *Done 2026-08-08: `SELECT … LIMIT 1` + `fetchone`; `study.html` shows `card.front` only; Electricity → first card front; Particles (id 1) → no-cards message. Predicted both correctly (including non-random first row).*
- [x] **6.3 — Flip to reveal the back.** Vanilla JS hides the back until Space (or a click) reveals it. Visible: press Space → back appears. *Done 2026-08-08: authored `study.js` (`keydown` + `e.code === "Space"` + `preventDefault` + `classList.toggle("is-flipped")`); CSS hide/show via `#back` / `#back.is-flipped`; debugged `getElementById("#back")` (null) → `getElementById("back")`; learned `border-style` required for borders to paint. Quiz: listen on `document` so focus isn’t required on the card (correct).*
- [x] **6.4 — Rate → write a `reviews` row.** Buttons (or form) POST a rating 1–5; server INSERTs into `reviews` with a placeholder `next_due_at`, then redirects back to study. Visible: rate a card → `reviews` has a new row; refresh doesn't re-POST. *Done 2026-08-08: form POSTs `card_id`/`rating`/`spec_point`; INSERT + `redirect(url_for("study", spec_point=…))` (PRG). Same card after redirect is expected (`LIMIT 1` always picks first row — next card is 6.6). Quiz: placeholder OK until scheduler (correct).*
- [x] **6.5 — Real scheduler in `scheduler.py`.** Pure function: `next_due_at = now + rating² days`. Use it on INSERT. Visible: rate 3 → `next_due_at` is ~9 days out (check in Python or DB Browser). *Done 2026-08-08: authored pure `next_due_at(rating, now)` with `timedelta` + `isoformat`; wired into study POST. Rate 3 → `2026-08-17…`; rate 5 → `2026-09-02…`. Quiz: `now` as arg for testability (correct). Fixed typo `noe` and `import datetime` vs `from datetime import datetime`.*
- [x] **6.6 — Keyboard + next card.** Space flips; 1–5 rates via keyboard; after rating, load the next due card (or "all done"). Visible: a real keyboard-driven mini-session; section deliverable met. *Done 2026-08-08: due-card SELECT with `NOT IN (… next_due_at > now)`; empty → "All done for now"; `study.js` Space flip + keys 1–5 click rating buttons. Verified next card after rate + keyboard rating.*

**Section 6 complete 2026-08-08.** Deliverable met: `/study?spec_point=<id>` runs a real session — one due card at a time, Space to flip, 1–5 to rate (keys or buttons), each rating writes a `reviews` row with `next_due_at = now + rating² days`, then the next due card (or all done).

### Section 7 — Core feature: coverage dashboard

**What I'll learn:** aggregation SQL (`COUNT`, `GROUP BY`, `MAX`), building a summary view from multiple tables, template loops with conditional styling (highlight zero-card spec points).

**Deliverable:** open `/coverage` and see, for every spec point in my chosen subject: total cards, cards due today, when it was last reviewed, zero-card points highlighted. I can look at it and instantly answer "what should I revise next?"

**Why now:** this closes the loop the app promises — spec-aligned coverage. Without it, the app is just Anki-with-extra-steps.

**Tasks** (each ends in something visibly working):

- [x] **7.1 — Stub `/coverage` page.** New route + template that lists every `spec_points` title (plain `SELECT`, no aggregates yet). Visible: open `/coverage` → see all 16 titles. *Done 2026-08-09: `SELECT id, title … ORDER BY id` + `fetchall`; `coverage.html` `{% for row in rows %}` with `row["title"]`. Predicted ul-of-titles correctly; verified 200 + 16 `<li>`s. Quiz: `fetchall` because many rows (correct).*
- [x] **7.2 — Card counts with aggregation.** For each spec point, show how many cards it has (`COUNT` + `GROUP BY`, keep zero-card points). Visible: Electricity shows `10`; empty points show `0`. *Done 2026-08-09: `LEFT JOIN` + `COUNT(c.id) AS card_count` + `GROUP BY sp.id`; template shows title + count. Verified Electricity `10`, Particles `0`. Slowed down on SQL meaning; articulated `ON` as gluing card `spec_point_id` to spec `id` (FK match).*
- [x] **7.3 — Due-today counts.** Per point, count cards that are due now (same “due” idea as study mode). Visible: after rating some Electricity cards, due count drops below total. *Done 2026-08-09: correlated subquery with study’s `NOT IN (… next_due_at > ?)`; template shows `card_count` + `due_count`. Predicted Electricity 10/0 correctly. Quiz: never-reviewed card is due because no `next_due_at` exists yet (correct).*
- [x] **7.4 — Last reviewed.** `reviews` has no reviewed-at yet — add one, write it on rate, show `MAX(...)` per point (or “never”). Visible: a recently rated point shows a timestamp; never-reviewed points say so. *Done 2026-08-09: `ALTER … ADD COLUMN reviewed_at`; study INSERT writes it; coverage `MAX(r.reviewed_at)` + template if/else → timestamp vs “never”. Quiz: old rows stay NULL (correct). Verified after forcing one due card + rating.*
- [x] **7.5 — Highlight zero-card points.** Template + CSS mark points with `0` cards so gaps jump out. Visible: non-Electricity rows stand out at a glance. *Done 2026-08-09: `{% if row["card_count"] == 0 %}class="no-cards"{% endif %}` + `.no-cards { color: cyan; }`. Quiz: Electricity (10 cards) should not get the class — it’s total cards not due (correct). Confirmed empty topics stand out.*
- [x] **7.6 — Make “what next?” obvious.** Light polish (readable layout, link into `/study?spec_point=…` and/or `/spec/<id>`). Visible: section deliverable met — you can open `/coverage` and decide what to revise next. *Done 2026-08-09: title → `url_for('spec_point', …)`; Study → `url_for('study', spec_point=…)`. Debugged stale/broken href that requested `/url_for(...` as a path (missing `{{ }}`); nested quotes clarified with `row['id']`. Quiz: study filter is query param on `/study` (correct).*

**Section 7 complete 2026-08-09.** Deliverable met: `/coverage` shows per-point card count, due count, last reviewed; zero-card points highlighted; links into spec + study so you can decide what to revise next.


### Section 8 — Tests

**What I'll learn:** what `pytest` is, why pure functions are easier to test than side-effect-heavy code, unit tests (for the scheduler) vs route smoke tests (for the Flask endpoints), running tests locally with one command.

**Deliverable:** `pytest` runs green. At minimum: unit tests for the scheduler function (a handful of input/output cases) and smoke tests for each route (returns 200, expected content in the response).

**Why now (and not earlier):** I now have three features worth testing and one pure function (the scheduler) that is *ideal* for demonstrating unit tests. Testing before this would be testing very little.

**Tasks** (each ends in something visibly working):

- [x] **8.1 — Install `pytest` & pin it.** Add pytest to the venv and `requirements.txt`. Visible: `pytest --version` prints a version; `requirements.txt` has a pinned `pytest==…` line. *Done 2026-08-11: first `pip install` landed in pyenv (broken `.venv/bin/pip` shebang still pointed at old `flashcard-app` path); dug into `#!` + `python -m pip`; pinned `pytest==9.1.1` + `pluggy==1.6.0` (caught single `=`); recreated `.venv` from `requirements.txt` → shebang now `/home/amalia/flashie/.venv/bin/python3`; `.venv/bin/pytest --version` → 9.1.1.*
- [x] **8.2 — First scheduler unit test.** Create `tests/test_scheduler.py` with one test that calls `next_due_at` with a fixed `now` and a known rating, and asserts the ISO date. Visible: `pytest` runs → 1 passed. *Done 2026-08-12: authored `test_rating_3_is_nine_days_later`; first assert quoted source text (fixed to `.isoformat()` call); collection hit `ModuleNotFoundError: scheduler` → added `pytest.ini` with `[pytest]` + `pythonpath = .` (after `/flashie` mis-path); `.pytest_cache/` gitignored. `.venv/bin/pytest -v` → 1 passed.*
- [x] **8.3 — More scheduler cases.** Add a few more input/output cases (e.g. rating 1 and 5). Visible: `pytest` → several passed, still all green. *Done 2026-08-12: added `test_rating_1_…` (→ Aug 9) and `test_rating_5_…` (→ Sep 2); quiz — one fail isolates that input (B, correct); Amalia ran `.venv/bin/pytest -v` herself → 3 passed in 0.02s.*
- [x] **8.4 — Flask test client, first smoke.** Use Flask’s test client to GET `/` and assert status 200. Visible: that smoke test passes without starting `flask run` by hand. *Done 2026-08-12: authored `tests/test_routes.py` with `app.test_client()` + `client.get("/")` + `status_code == 200`; quiz — unit vs smoke in own words (correct); pytest → 4 passed.*
- [x] **8.5 — Smoke the other routes.** Same idea for `/coverage`, `/study?spec_point=…`, `/spec/<id>`. Visible: each returns 200 (or a deliberate empty/message page you already handle). *Done 2026-08-12: authored three smokes in `test_routes.py`; quiz — `spec_point=16` is query param (correct); pytest → 7 passed.*
- [x] **8.6 — Assert expected content.** Strengthen smokes so responses contain something you recognize (e.g. a known title, “Coverage”, card front text). Visible: `pytest` all green in one command — section deliverable met. *Done 2026-08-12: content asserts — home “Spec Companion”, coverage “Coverage”, study “Studying”, spec “Electricity”; quiz — 200 can still be wrong content (correct); pytest → 7 passed.*

**Section 8 complete 2026-08-12.** Deliverable met: `pytest` green — scheduler unit tests (ratings 1/3/5) plus route smokes (`/`, `/coverage`, `/study?spec_point=…`, `/spec/<id>`) with status 200 and recognizable body text.

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
