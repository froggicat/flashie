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
| Splitting my own code across multiple files & importing from them | seed | — | — | — |
| Pure functions (no side effects, testable in isolation) | seed | — | — | — |
| Reading an error message / stack trace | seed | — | — | — |

## 2. Structural — how a project is *shaped*

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Files & folders in a repo (project layout as a design decision) | seed | — | — | — |
| Dependency — someone else's code my project uses | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Core components / Environment & dependencies. |
| Package manager (`pip`) | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.3: ran `pip install flask` (installed 7 packages: Flask + 6 transitive deps) and `pip freeze > requirements.txt` inside the active venv. |
| Virtual environment (`venv`) — isolation per project | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.2: created `.venv/` with `python3 -m venv .venv`, activated it, and confirmed `which python` → `~/flashcard-app/.venv/bin/python`. Correctly predicted `pip` without activation lands in system Python. Gap: first framing of *why* `.venv/` is gitignored was "privacy" — corrected to "huge + machine-specific + regenerable from `requirements.txt`". Upgrade to `understood` requires teaching that back cleanly in a later session. |
| `requirements.txt` — pinned deps, one-command reinstall | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.3: authored a 7-line pinned file via `pip freeze > requirements.txt`, committed it, and can articulate why `==` pinning + capturing transitive deps means reproducible envs. Upgrade to `understood` requires actually reproducing the env from it on a fresh machine (task 1.6 or later). |
| Transitive dependencies (installing X pulls in what X needs) | introduced | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.3: predicted "~5 packages" for `pip install flask`; actual = 7 (Flask + Werkzeug, Jinja2, MarkupSafe, itsdangerous, click, blinker). Walked through what each is for. |
| Version pinning (`==` vs `>=` vs `~=`) | introduced | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.3: `requirements.txt` uses `==` for exact-version reproducibility. Alternatives (`>=`, `~=`) named and parked. |
| Installing pinned versions on a fresh machine | seed | — | — | — |
| Flask project conventions (`templates/`, `static/`) | seed | — | — | Referenced in plan.md §Section 2–3 as upcoming. |
| Python module vs package | seed | — | — | — |

## 3. Backend, HTTP & Flask

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Frontend vs backend distinction | introduced | 2026-08-01 | 2026-08-01 | Explicit contrast drawn in project.md §Backend and §Frontend. |
| Long-running server vs one-shot script | introduced | 2026-08-01 | 2026-08-01 | project.md: "A Python script runs, finishes, exits. A server stays up…" |
| HTTP as browser↔server language | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Backend. |
| Framework as a concept (handles boring parts) | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Backend. |
| Flask specifically (why it, not Django/FastAPI) | introduced | 2026-08-01 | 2026-08-01 | plan.md §2 walks through alternatives. |
| URL routes mapped to Python functions | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Backend. |
| The Flask app object and `flask run` | seed | — | — | Coming in plan.md §Section 1 deliverable. |
| HTTP methods — GET vs POST | seed | — | — | Coming in plan.md §Section 5. |
| Query parameters (`?spec_point=<id>`) | seed | — | — | Coming in plan.md §Section 6. |
| Reading POSTed form data (`request.form`) | seed | — | — | Coming in plan.md §Section 5. |
| HTTP status codes (200, 302, 404, 500) | seed | — | — | Coming in plan.md §Section 8 (smoke tests assert 200). |

## 4. Database — SQLite & SQL

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| Database — what it's *for* (durable, structured storage) | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Database. |
| SQL as the language for talking to a database | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Database. |
| SQLite specifically (single file, no server, why it fits) | introduced | 2026-08-01 | 2026-08-01 | project.md §Database + plan.md §3 walk-through. |
| Table / row / column | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Database. |
| Schema — the shape of the tables | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Database. |
| Foreign keys (a card belongs to one spec point) | seed | — | — | Coming in plan.md §Section 4. |
| Self-referential trees (`parent_id`) | seed | — | — | Coming in plan.md §Section 4. |
| `CREATE TABLE` | seed | — | — | Coming in plan.md §Section 4. |
| `INSERT INTO` | seed | — | — | Coming in plan.md §Section 5. |
| `SELECT ... WHERE` | seed | — | — | Coming in plan.md §Section 6. |
| Aggregation SQL (`COUNT`, `GROUP BY`, `MAX`) | seed | — | — | Coming in plan.md §Section 7. |
| Seeding a DB from a JSON file (`import_spec.py`) | seed | — | — | Coming in plan.md §Section 4. |
| Persistence — why data survives across restarts (and what breaks it) | introduced | 2026-08-01 | 2026-08-01 | project.md §Deployment explains why volume matters for SQLite. |

## 5. Frontend — HTML, CSS, JS, templates

| Concept | Status | Introduced | Last reviewed | Evidence |
|---|---|---|---|---|
| HTML — page structure | practicing | prior | — | Prior projects (project.md background). Not yet quizzed. |
| CSS — selectors and basic layout | practicing | prior | — | Prior projects. Not yet quizzed. |
| JavaScript in the browser — basic syntax | practicing | prior | — | Prior projects. Not yet quizzed. |
| Template as a concept (HTML with placeholders filled server-side) | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Frontend. |
| Jinja — Flask's template language | introduced | 2026-08-01 | 2026-08-01 | Named in project.md §Frontend, chosen in plan.md §Section 2. |
| `render_template` in a Flask route | seed | — | — | Coming in plan.md §Section 2. |
| Template inheritance (`base.html` + `{% extends %}`) | seed | — | — | Coming in plan.md §Section 3. |
| Static files served by Flask (CSS/JS) | seed | — | — | Coming in plan.md §Section 3. |
| Vanilla-JS keyboard event listeners (`keydown`) | seed | — | — | Coming in plan.md §Section 6 (space to flip, 1–5 to rate). |
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
| Writing a *meaningful* commit message | understood | 2026-08-01 | 2026-08-01 | 2026-08-01 task 1.3: commit `dbe1281` — "activated venv and make requirements.txt to keep track of exact versions of dependencies". Clear what + genuine why (purpose of the file, not restatement). Minor nits (typo, "activated venv" isn't a git action) noted but concept is solid. |
| GitHub — remote host for the repo | introduced | 2026-08-01 | 2026-08-01 | Defined in project.md §Source control. First hands-on evidence lands in task 1.6. |
| `git status` / `git diff` / `git log` in daily use | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01: ran `git status` (accurately predicted 5 untracked, no ignored) and `git log --oneline` (pasted output). `git diff` not yet exercised. |
| Pushing to a remote (`git push`) | seed | — | — | Coming in task 1.6. |
| Branching & merging | seed | — | — | — |
| `.gitignore` — files git should never see | practicing | 2026-08-01 | 2026-08-01 | 2026-08-01: authored `/home/amalia/learning/.gitignore` from scratch, including `.env` and DB entries. Hit and self-corrected the "pattern must literally match on-disk filename" gotcha (`db.sqlite3` vs `db.sqlite`). |
| Testing — why it exists, when it pays off | introduced | 2026-08-01 | 2026-08-01 | plan.md §Section 8 explains rationale ("why pure functions are easier to test"). |
| `pytest` — the tool | seed | — | — | Coming in plan.md §Section 8. |
| Unit test vs route smoke test | seed | — | — | Coming in plan.md §Section 8. |
| Local dev loop (edit → run → observe) | practicing | prior | — | project.md background: preferred workflow is iterating in code. Not yet quizzed. |
| Debugging loop (reproduce → isolate → hypothesise → fix) | seed | — | — | — |
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

---

## When to look at this file

- **Start of a lesson:** scan the section we're about to touch. Anything `seed` about to be taught? Mark it `introduced` at the *end* of the lesson, not the start.
- **End of a lesson:** every concept touched gets its status re-evaluated. Upgrade only on evidence. Update `Last reviewed` and rewrite `Evidence`.
- **Before a quiz:** sample from `practicing` first, then stale `understood` (>30 days), then recently `introduced`. Never quiz `seed` — nothing to test yet.
- **When something new comes up:** add a row *now*, in the same session, in the right section. Never leave an unnamed concept floating.
