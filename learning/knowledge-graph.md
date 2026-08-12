# Knowledge Graph — What I Actually Know

Living record of every concept this project teaches me. **Updated after every lesson.** This file decides what I get quizzed on. If it isn't in here, it doesn't exist as knowledge yet.

Read alongside `project.md` (what we're building) and `plan.md` (build order + locked decisions). This file is the third leg: what's actually in my head.

---

## Status ladder

Statuses only ever **upgrade**, and only on **evidence of something I actually said or did.**

| Status | Meaning | How I upgrade *from* it |
|---|---|---|
| **seed** | Not yet taught. Just a placeholder so it doesn't get skipped. | Explain it to me once → `introduced`. |
| **introduced** | Explained once — in `project.md`, `plan.md`, or a lesson. | Use it (even with help) in real code → `practicing`. |
| **practicing** | I've used it, usually with help (agent, snippet, tutorial). Might not be able to teach it. | Explain in my own words *and* pass a short quiz → `understood`. |
| **understood** | I can explain it out loud, unprompted, correctly. Passed a quiz. | Nothing above this. Just keep it fresh. |

## Quiz & review rules

- I am **not** re-quizzed on any concept that is `understood` **and** was reviewed within the last **30 days**.
- Anything `understood` but stale (>30 days since last review) is a candidate for a spot-check.
- `practicing` concepts are prime quiz targets — they're the boundary where knowledge is fragile.
- New concept encountered mid-lesson? Add a row as `seed` (or `introduced` if it just got explained) *the same session*. Don't defer.

## Seeding rules used for this initial state

- Anything walked through and checked while writing `project.md` / `plan.md` starts as `introduced`, not `seed`.
- Anything I brought in from prior projects (HTML/CSS/JS basics) starts as `practicing`, not `understood` — until I've been quizzed I can't claim it's teachable knowledge.
- **Exception (declared 2026-08-01):** low-level Python (variables, types, conditionals, loops, functions, lists/dicts, stdlib `import`) is `understood` on Amalia's explicit say-so. Exempt from quiz. This exception does *not* extend to Python-in-a-multi-file-project, pure functions, or reading stack traces — those stay `seed`.
- **Exception (declared 2026-08-01):** git `init`, `status`, `add`, `commit`, `log`, and `clone` are `understood` on Amalia's explicit say-so (1 year of prior use). Exempt from quiz. This exception does *not* extend to `diff`, `push`, `pull`, `remote`, `branch`, `merge`, `.gitignore`, or advanced workflow (`rebase -i`, cherry-pick, reflog, submodules, hooks) — those remain quiz-eligible and upgrade only on project evidence.
- Everything else this project will teach starts as `seed`.

## Date conventions

- `Introduced` — first time it was explained to me. `prior` = pre-dates this project. `—` = not yet.
- `Last reviewed` — most recent status change *or* re-test. `—` = not yet.
- Dates are ISO (`YYYY-MM-DD`).

---

## 1. Low-level — the language building blocks

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Variables & basic types (str, int, bool, None) | understood | prior | 2026-08-01 | Amalia confirmed on 2026-08-01: "I already definitely know these." Exempt from quiz. |
| Conditionals (`if` / `elif` / `else`) | understood | prior | 2026-08-01 | Amalia confirmed on 2026-08-01: "I already definitely know these." Exempt from quiz. |
| Loops (`for` / `while`) | understood | prior | 2026-08-01 | Amalia confirmed on 2026-08-01: "I already definitely know these." Exempt from quiz. |
| Functions (`def`, arguments, `return`) | understood | prior | 2026-08-01 | Amalia confirmed on 2026-08-01: "I already definitely know these." Exempt from quiz. |
| Lists and dicts | understood | prior | 2026-08-01 | Amalia confirmed on 2026-08-01: "I already definitely know these." Exempt from quiz. |
| `import` from the standard library | understood | prior | 2026-08-01 | Amalia confirmed on 2026-08-01: "I already definitely know these." Exempt from quiz. |
| Splitting my own code across multiple files & importing from them | understood | 2026-08-02 | 2026-08-08 | Prior `specs`/`db` evidence. 2026-08-08 task 6.5: authored `scheduler.py` and `from scheduler import next_due_at` in `app.py` — same multi-file pattern, new module. |
| Pure functions (no side effects, testable in isolation) | understood | 2026-08-08 | 2026-08-11 | Prior scheduler. 2026-08-11 task 8.1 quiz: why pure is easier to test than study POST — answered in own words: small scope isolates bugs to *your* logic vs SQL/HTTP logistics (correct). |
| Reading an error message / stack trace | practicing | 2026-08-02 | 2026-08-12 | Prior. 2026-08-12 task 8.2: read pytest collection `ModuleNotFoundError` + `pytest.ini: no section header defined`; distinguished “can’t import” from “assert failed”. |
| Recursion (a function/macro calling itself, terminating on a base case) | understood | 2026-08-02 | 2026-08-05 | Jinja `render_tree` in §2. 2026-08-05 task 4.4: wrote recursive Python `insert_node` that INSERTs then calls itself for each child; base case = empty `children` (corrected from "parent_id is None"). Non-templating context — graduates to `understood`. |

## 2. Structural — how a project is *shaped*

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Files & folders in a repo (project layout as a design decision) | seed | — | — | — |
| Dependency — someone else's code my project uses | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Core components / Environment & dependencies. |
| Package manager (`pip`) | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.3: ran `pip install flask` (installed 7 packages: Flask + 6 transitive deps) and `pip freeze > requirements.txt` inside the active venv. |
| Virtual environment (`venv`) — isolation per project | practicing | 2026-08-01 | 2026-08-11 | Prior create/activate. 2026-08-11 task 8.1: after folder rename, `.venv/bin/pip` shebang still said `flashcard-app` → install went global; recreated with `python3 -m venv .venv` + `pip install -r requirements.txt`; new shebang → `flashie`. Comment still leans “boring paths” more than “regenerable shopping list” — keep practicing. |
| `requirements.txt` — pinned deps, one-command reinstall | understood | 2026-08-01 | 2026-08-11 | 2026-08-11 task 8.1: deleted `.venv`, reinstalled from pins — Flask + pytest both importable under `/home/amalia/flashie/.venv/...`. That *is* reproducing the env from the file. |
| Transitive dependencies (installing X pulls in what X needs) | practicing | 2026-08-01 | 2026-08-11 | Prior Flask tree. 2026-08-11 task 8.1: pinned `pluggy` as one of pytest’s pulled-in deps alongside `pytest==9.1.1`. |
| Version pinning (`==` vs `>=` vs `~=`) | practicing | 2026-08-01 | 2026-08-11 | 2026-08-11 task 8.1: wrote `pluggy=1.6.0`; `pip install -r` rejected it (`=` not valid; hint `==`). Fixed to `pluggy==1.6.0`. |
| Installing pinned versions on a fresh machine | practicing | 2026-08-11 | 2026-08-11 | 2026-08-11 task 8.1: full recreate of `.venv` from `requirements.txt` after rename broke the old env. |
| Shebang (`#!`) on scripts — which interpreter runs this file | practicing | 2026-08-11 | 2026-08-11 | 2026-08-11 task 8.1: read `.venv/bin/pip` line 1; predicted post-recreate path would say `flashie` (correct). Clarified: not “activation” — OS picks that Python binary. |
| Flask project conventions (`templates/`, `static/`) | practicing | 2026-08-02 | 2026-08-04 | 2026-08-02 task 2.1: created `templates/`. 2026-08-04 task 3.1: created `static/` + `style.css`; quiz — renaming `templates/` breaks lookup (answered correctly: 404/`TemplateNotFound`). Both folder names are Flask contracts. |
| Python module vs package | introduced | 2026-08-02 | 2026-08-02 | 2026-08-02 task 2.5: taught that a module is a `.py` file and a package is a folder of modules; `from specs import ...` looks for `specs.py` (module); `from specs.py import ...` would fail because Python would interpret `specs` as a package name (folder) and look for `.py` *inside* it. Only modules used so far; packages coming when the project grows. |

## 3. Backend, HTTP & Flask

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Frontend vs backend distinction | introduced | 2026-08-01 | 2026-08-01 | Explicit contrast drawn in project.md §Backend and §Frontend. |
| Long-running server vs one-shot script | practicing | 2026-08-01 | 2026-08-08 | Prior evidence. 2026-08-08 task 6.1: predicted 404 for no server; corrected — no process on `:5000` is connection refused / unable to connect; 404 only when a server answers “path unknown.” |
| HTTP as browser↔server language | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Backend. |
| Framework as a concept (handles boring parts) | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Backend. |
| Flask specifically (why it, not Django/FastAPI) | introduced | 2026-08-01 | 2026-08-01 | plan.md §2 walks through alternatives. |
| URL routes mapped to Python functions | practicing | 2026-08-01 | 2026-08-12 | Prior routes. 2026-08-12 task 8.4: smoke-tested `/` via test client — route runs without `flask run`. |
| Path parameters (`/spec/<int:id>`) — URL piece → function argument | practicing | 2026-08-07 | 2026-08-09 | Prior. 2026-08-09 task 7.6: coverage title links use path param `/spec/<id>`; contrasted with study’s query filter. |
| The Flask app object and `flask run` | practicing | 2026-08-01 | 2026-08-02 | 2026-08-01 task 1.5: ran `flask run`, bound `127.0.0.1:5000`, observed 200/404. 2026-08-02 task 2.2: switched to `flask run --debug` after learning that plain `flask run` caches compiled templates in memory (so template edits don't take effect until a restart). Debug mode gives template auto-reload, Python auto-reload, and the interactive Werkzeug 500 page. `flask run --debug` is the daily dev command from here. |
| Decorators (`@` syntax attaching behaviour to a function) | introduced | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.4: used `@app.route("/")` on `home()`. Mental model given: "the `@` line above a function attaches that function to a URL"; decorator internals deferred. |
| HTTP methods — GET vs POST | practicing | 2026-08-07 | 2026-08-08 | Prior PRG on spec_point. 2026-08-08 task 6.4: study route accepts POST, INSERTs review, redirects with `url_for("study", spec_point=…)` so query param survives. |
| Reading POSTed form data (`request.form`) | practicing | 2026-08-07 | 2026-08-08 | 2026-08-08 task 6.4: read `card_id` / `rating` / `spec_point` from rating form (hidden fields + submit button `name="rating"`). |
| Query parameters (`?spec_point=<id>`) | practicing | 2026-08-08 | 2026-08-12 | Prior. 2026-08-12 task 8.5: quiz — `spec_point=16` on study URL is query param not path (correct); smoked `client.get("/study?spec_point=16")`. |
| HTTP status codes (200, 302, 404, 500) | practicing | 2026-08-01 | 2026-08-12 | Prior. 2026-08-12 task 8.6 quiz: 200 can still be wrong page content (correct); smokes now assert body text too. |

## 4. Database — SQLite & SQL

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Database — what it's *for* (durable, structured storage) | practicing | 2026-08-01 | 2026-08-05 | 2026-08-05 task 4.1: created `db.sqlite` on disk via `sqlite3`; data survives as a file independent of the Python process. |
| SQL as the language for talking to a database | practicing | 2026-08-01 | 2026-08-05 | 2026-08-05 task 4.1: wrote `CREATE TABLE`, `INSERT INTO`, `SELECT *` as strings executed through Python. |
| SQLite specifically (single file, no server, why it fits) | practicing | 2026-08-01 | 2026-08-05 | 2026-08-05 task 4.1: `sqlite3.connect("db.sqlite")` created the file; no separate DB server. |
| Table / row / column | practicing | 2026-08-01 | 2026-08-05 | 2026-08-05 task 4.1: first mix-up (row↔column swapped) corrected — table = sheet, column = field kind, row = one record. Saw `[(1, 'hello sqlite')]` as one row with two columns. |
| Schema — the shape of the tables | practicing | 2026-08-01 | 2026-08-09 | Prior. 2026-08-09 task 7.4: added `reviewed_at` to `reviews` via ALTER; can distinguish `next_due_at` (scheduler) from `reviewed_at` (when rated). |
| Foreign keys (a card belongs to one spec point) | practicing | 2026-08-05 | 2026-08-09 | Prior isolation. 2026-08-09 task 7.2: explained `ON c.spec_point_id = sp.id` as gluing card FK to spec PK across a JOIN. |
| Self-referential trees (`parent_id`) | practicing | 2026-08-05 | 2026-08-05 | Schema + seed in 4.2–4.4; task 4.6: rebuilt nested tree from flat `parent_id` rows in Python (`nodes_by_id` + link pass). Articulated that `node` is the step-1 dict, not the SQL row. |
| `CREATE TABLE` | practicing | 2026-08-05 | 2026-08-09 | Prior tables. 2026-08-09 task 7.4: `ALTER TABLE reviews ADD COLUMN reviewed_at TEXT` — add column without rebuilding; existing rows stay NULL. |
| `INSERT INTO` | practicing | 2026-08-05 | 2026-08-09 | Prior. 2026-08-09 task 7.4: extended study INSERT to four columns including `reviewed_at` (authored correctly). |
| `SELECT ... WHERE` | practicing | 2026-08-05 | 2026-08-09 | Prior. 2026-08-09 task 7.3: coverage `due_count` subquery reuses study’s `NOT IN (SELECT card_id FROM reviews WHERE next_due_at > ?)`; quiz — never-reviewed card is due (no future `next_due_at`) (correct). Predicted Electricity 10 cards / 0 due (correct). |
| `LIMIT` (cap how many rows a SELECT returns) | practicing | 2026-08-08 | 2026-08-08 | 6.2 first-card. 2026-08-08 task 6.6: still `LIMIT 1`, but only among *due* cards — same card stops repeating once it has a future `next_due_at`. |
| `JOIN` / `LEFT JOIN` (combine rows from two tables) | practicing | 2026-08-09 | 2026-08-09 | 2026-08-09 task 7.2: coverage query `LEFT JOIN cards … ON c.spec_point_id = sp.id`; explained ON as FK glue; LEFT keeps zero-card points. |
| Aggregation SQL (`COUNT`, `GROUP BY`, `MAX`) | practicing | 2026-08-09 | 2026-08-09 | 7.2–7.3 COUNTs. 2026-08-09 task 7.4: `MAX(r.reviewed_at)` per spec point via subquery; articulated that MAX = latest review time for that topic; old rows NULL until new ratings. |
| Seeding a DB from a JSON file (`import_spec.py`) | practicing | 2026-08-05 | 2026-08-05 | Task 4.4: recursive INSERT from JSON; 16 rows. |
| Persistence — why data survives across restarts (and what breaks it) | practicing | 2026-08-01 | 2026-08-07 | File + commit earlier. 2026-08-07 task 5.6: cleared cards with `DELETE`, then re-authored 10 via the UI — data lives in `db.sqlite` independent of the Flask process. |
| `sqlite3` module (Python ↔ SQLite) | practicing | 2026-08-05 | 2026-08-05 | Full loop in scripts; task 4.6: `Row` factory + `load_spec_tree` used from Flask `home()`. |
| Rebuilding a nested structure from flat parent_id rows | practicing | 2026-08-05 | 2026-08-05 | 2026-08-05 task 4.6: two-pass algorithm in `db.py`; page identical to in-memory tree — “thats crazy - its all the same.” |

## 5. Frontend — HTML, CSS, JS, templates

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| HTML — page structure | practicing | prior | 2026-08-07 | Prior projects. 2026-08-07 task 5.3: authored `<form method="post">` with named `<input>`s + submit on `spec_point.html`. |
| CSS — selectors and basic layout | practicing | prior | 2026-08-09 | Prior. 2026-08-09 task 7.5: authored `.no-cards { color: cyan; }` so zero-card coverage rows stand out. |
| CSS specificity (more specific selector wins) | practicing | 2026-08-04 | 2026-08-04 | 2026-08-04 task 3.5: observed `.spec-item > ul` beat `.is-open`; fixed with `.spec-item > ul.is-open`. |
| CSS `::before` / `content` (generated caret text) | practicing | 2026-08-04 | 2026-08-04 | 2026-08-04 task 3.6: added `▶`/`▼` via `::before` + `content`; learned you don't nest `::before::before`. |
| JavaScript in the browser — basic syntax | practicing | prior | 2026-08-08 | Tree + study. 2026-08-08 task 6.6: `else if` (not Python `elif`); `e.key` for `"1"`–`"5"` vs `e.code` for Space. |
| Template as a concept (HTML with placeholders filled server-side) | understood | 2026-08-01 | 2026-08-04 | Prior §2 evidence. 2026-08-04 task 3.3: re-stated unprompted that view-source shows only the resulting plain HTML, not Jinja tags — same mental model, now with inheritance in the mix. |
| Jinja — Flask's template language | practicing | 2026-08-01 | 2026-08-09 | Prior macros/extends/for/if. 2026-08-09 task 7.5: conditional `class="no-cards"` when `card_count == 0`; quiz — class tracks total cards not due (correct). |
| `render_template` in a Flask route | practicing | 2026-08-02 | 2026-08-09 | Prior pages. 2026-08-09 task 7.1: fourth page — `render_template("coverage.html", rows=rows)` after `fetchall`. |
| Template inheritance (`base.html` + `{% extends %}`) | practicing | 2026-08-04 | 2026-08-04 | 2026-08-04 task 3.3: authored `base.html` with `title` + `content` blocks; rewrote `home.html` as `{% extends "base.html" %}` filling only `content`. Verified the child supplies the visible page body. Quiz: view-source won't show `{% extends %}` / `{% block %}` — answered correctly (Jinja runs server-side). |
| Static files served by Flask (CSS/JS) | practicing | 2026-08-04 | 2026-08-04 | Task 3.1: CSS. Task 3.5: same pattern for `tree.js` via `url_for`; script placed after `{% block content %}` so buttons exist when it runs. |
| `url_for` — Flask builds a URL from an endpoint name | practicing | 2026-08-04 | 2026-08-09 | Prior. 2026-08-09 task 7.6: coverage `url_for('spec_point'…)` + `url_for('study', spec_point=…)`; missing `{{ }}` made the browser request `/url_for(...` as a path (404). |
| Vanilla-JS keyboard event listeners (`keydown`) | practicing | 2026-08-08 | 2026-08-08 | 6.3 Space flip. 2026-08-08 task 6.6: keys `"1"`–`"5"` trigger rating button `.click()`; learned JS uses `else if` not `elif`, and `e.key` for digit characters. |
| CSS media query for mobile | seed | — | — | Coming in plan.md §Section 9. |
| Why "no build step" is a real choice (vs React/Vue/bundler) | introduced | 2026-08-01 | 2026-08-01 | plan.md §Section 4 (Frontend approach) argues this. |

## 6. Auth & secrets

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Authentication as a concept (proving I am who I claim) | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Authentication. |
| HTTP basic auth (browser prompt, cached per device) | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Authentication. |
| Environment variable — value stored outside my code | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Authentication. |
| Secrets *must not* be committed to git | introduced | 2026-08-01 | 2026-08-01 | project.md §Authentication ties env vars directly to git safety. |
| Flask `before_request` hook for site-wide auth | seed | — | — | Coming in plan.md §Section 9. |

## 7. Deployment & infra

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Deployment — always-on, fixed URL | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Deployment. |
| Hosting provider (rents me a slice of a data centre) | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Deployment. |
| Fly.io specifically (and why not Render / Vercel / PythonAnywhere) | introduced | 2026-08-01 | 2026-08-01 | plan.md §Section 5 (Hosting) walks through alternatives. |
| Docker — the container idea, why it exists | introduced | 2026-08-01 | 2026-08-01 | project.md §Deployment defines container / image / Dockerfile. |
| Dockerfile — the *recipe* | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Deployment. |
| Image vs container (built package vs running instance) | introduced | 2026-08-01 | 2026-08-01 | Distinction drawn in project.md §Deployment. |
| Volume — persistent disk that survives restarts | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Deployment. |
| `fly.toml` — Fly-specific config | seed | — | — | Coming in plan.md §Section 9. |
| `flyctl deploy` — pushing code to Fly | seed | — | — | Coming in plan.md §Section 9. |

## 8. Engineering practice — git, tests, debugging, env

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Source control — what it *is*, why to always use it | understood | 2026-08-01 | 2026-08-01 | Extension of the 2026-08-01 git say-so exception (1 year of git+GitHub use). Exempt from quiz. |
| `git` — the specific tool | understood | 2026-08-01 | 2026-08-01 | Say-so exception (2026-08-01). Corroborated in task 1.1: ran `git init`, `git add`, `git commit`, `git log` end-to-end without help. |
| Repository — files + full change history | understood | 2026-08-01 | 2026-08-01 | Say-so exception (2026-08-01). Corroborated: `/home/amalia/learning/.git/` now exists; HEAD at commit `8eb21de` on `main`. |
| Commit — one saved snapshot with a message | understood | 2026-08-01 | 2026-08-01 | Say-so exception (2026-08-01). Corroborated: authored commit `8eb21de` ("initial commit! very exciting") on 2026-08-01. |
| Writing a *meaningful* commit message | understood | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.3: commit `dbe1281` — "activated venv and make requirements.txt to keep track of exact versions of dependencies" — clear what + genuine why. 2026-08-01 tasks 1.4/1.5: commits `788b805` and `1e53d3e` describe what but not why; concept still `understood` (ladder only goes up) but next commits should re-include a purpose clause. |
| GitHub — remote host for the repo | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.6 (done solo): created `github.com/froggicat/flashcard-app`, wired `origin` remote via SSH, pushed 5 commits. Local `main` now tracks `origin/main`. |
| `git status` / `git diff` / `git log` in daily use | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01: ran `git status` (accurately predicted 5 untracked, no ignored) and `git log --oneline` (pasted output). `git diff` not yet exercised. |
| Pushing to a remote (`git push`) | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.6 (done solo): pushed all 5 commits from local `main` to `origin/main`; upstream tracking established (`git branch -vv` shows `[origin/main]`). |
| `git remote` — pointing a local repo at a hosted one | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.6 (done solo): added `origin` = `git@github.com:froggicat/flashcard-app.git`. Verified with `git remote -v`. |
| SSH-based git auth (vs HTTPS + PAT) | practicing | prior | 2026-08-01 | Key set up during prior Odin Project frontend work, so pre-dates this project. Corroborated 2026-08-01 task 1.6: pushed successfully via `git@github.com:froggicat/flashcard-app.git`. Not yet quizzed → stays `practicing` per seeding rules for prior-project skills. |
| Branching & merging | seed | — | — | — |
| `.gitignore` — files git should never see | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01: authored `/home/amalia/learning/.gitignore` from scratch, including `.env` and DB entries. Hit and self-corrected the "pattern must literally match on-disk filename" gotcha (`db.sqlite3` vs `db.sqlite`). |
| Testing — why it exists, when it pays off | practicing | 2026-08-01 | 2026-08-12 | §8 complete: unit + smoke + content checks; one `pytest` command exercises scheduler and all main routes. |
| `pytest` — the tool | practicing | 2026-08-11 | 2026-08-12 | 2026-08-12 task 8.6: final suite 7 passed (4 route smokes + 3 scheduler units). |
| Unit test vs route smoke test | practicing | 2026-08-12 | 2026-08-12 | Own-words distinction; both kinds green in one run. |
| Flask test client (`app.test_client()`) | practicing | 2026-08-12 | 2026-08-12 | 8.5 smokes. 2026-08-12 task 8.6: `response.get_data(as_text=True)` content asserts on each route. |
| `assert` in tests (expected vs actual) | practicing | 2026-08-12 | 2026-08-12 | 8.6: status + substring asserts (“Spec Companion”, “Coverage”, “Studying”, “Electricity”). |
| `pytest.ini` / `pythonpath` (make project imports work) | practicing | 2026-08-12 | 2026-08-12 | 2026-08-12 task 8.2: `ModuleNotFoundError: scheduler` until `[pytest]` + `pythonpath = .`; tried `"/flashie"` first (absolute path + missing section). |
| Local dev loop (edit → run → observe) | practicing | prior | 2026-08-07 | 2026-08-07 §5: full loop on cards feature — form → POST → see list; wiped/rebuilt card content through the running app. |
| Debugging loop (reproduce → isolate → hypothesise → fix) | practicing | 2026-08-02 | 2026-08-02 | 2026-08-02 task 2.2: ran the loop twice, mostly independently. (1) "server logs 200 but page unchanged" mystery — reproduced (multiple refreshes, all 200), isolated (server-sent HTML via view-source was the *old* file), hypothesised (template caching in non-debug Flask — agent-assisted), fixed (`flask run --debug`). (2) `TemplateSyntaxError` from a `{{ }}` inside an HTML comment — reproduced (the 500 page), isolated (line 8 in traceback + Werkzeug debug page), hypothesised & fixed *solo* (removed the offending comment). |
| Print-debugging & reading logs | practicing | prior | — | Prior Python work. Not yet quizzed. |

## 9. AI-era practice & design intuition

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Writing a plan *before* coding | introduced | 2026-08-01 | 2026-08-01 | plan.md itself exists as evidence + argues for the practice. |
| Comparing 1–2 real alternatives with trade-offs | introduced | 2026-08-01 | 2026-08-01 | plan.md §Locked decisions models this pattern for each tech choice. |
| "When would this decision stop being right?" thinking | introduced | 2026-08-01 | 2026-08-01 | plan.md §Locked decisions ends each choice with this. |
| Choosing the boring / small-surface-area default | introduced | 2026-08-01 | 2026-08-01 | plan.md §Flask & §Frontend argue this explicitly. |
| Context / memory file — the "read this first" spec | introduced | 2026-08-01 | 2026-08-01 | project.md is one; its own §For future sessions instructs re-reading it. |
| Re-reading `project.md` at the start of every session | introduced | 2026-08-01 | 2026-08-01 | project.md §For future sessions demands this. |
| Knowledge graph as a self-tracking artefact | introduced | 2026-08-01 | 2026-08-01 | This file exists and is the source of truth for what I know. |
| File map as a "no mystery boxes" rule | introduced | 2026-08-01 | 2026-08-01 | `file-map.md` exists alongside this file. |
| Parking-lot discipline (v1 in, v2+ parked but written down) | introduced | 2026-08-01 | 2026-08-01 | project.md §Parking lot enforces this. |
| MVP scope enforcement — "if you add X, what comes out?" | introduced | 2026-08-01 | 2026-08-01 | project.md §For future sessions instructs this trade check. |
| Definition-of-done for a milestone (visibly working) | introduced | 2026-08-01 | 2026-08-01 | project.md §Definition of "done" + plan.md's per-section deliverables. |
| Not adding features preemptively (friction-first) | introduced | 2026-08-01 | 2026-08-01 | project.md §Traps I've committed to avoiding. |
| Keeping an `IDEAS.md` during a real use-week | introduced | 2026-08-01 | 2026-08-01 | project.md §Definition of "done" + plan.md §After Section 9. |
| Reviewing an AI-generated diff *before* accepting | seed | — | — | Will hit this the first time an agent proposes real code. |
| Correcting / rejecting an AI suggestion out loud | seed | — | — | Will hit this whenever I disagree with a proposed change. |
| Agent memory files (Cursor rules, `AGENTS.md`, etc.) | seed | — | — | Will formalise when the first cross-session rule becomes obvious. |
| Turning off autocomplete / AI helpers when they short-circuit learning | practicing | 2026-08-02 | 2026-08-02 | 2026-08-02 task 2.3: noticed unprompted mid-task that tab-complete was doing the thinking ("i was relying to heavily on that to actually understand the code i was writing") and disabled it. Named the pattern and took the action — the two halves of the same skill. Heuristic to keep: *if the tool would finish the code correctly when I don't understand it, the tool is short-circuiting my learning.* |

---

## When to look at this file

- **Start of a lesson:** scan the section we're about to touch. Anything `seed` about to be taught? Mark it `introduced` at the *end* of the lesson, not the start.
- **End of a lesson:** every concept touched gets its status re-evaluated. Upgrade only on evidence. Update `Last reviewed` and rewrite `Evidence`.
- **Before a quiz:** sample from `practicing` first, then stale `understood` (>30 days), then recently `introduced`. Never quiz `seed` — nothing to test yet.
- **When something new comes up:** add a row *now*, in the same session, in the right section. Never leave an unnamed concept floating.
