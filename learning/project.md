# Spec Companion — Project Context

**Read this file first at the start of every future session.** It captures who I am, what we're building, and what is / isn't in scope for the first shippable version.

---

## About me

- **Name:** Amalia
- **Currently:** A-level student — Maths, Further Maths, Physics, Computer Science
- **Coding background:** Python, JavaScript, HTML, CSS
- **Experience level:** Several small, disconnected projects. No experience with:
  - Web frameworks
  - Databases (beyond trivial SQLite reads)
  - Deployment / hosting
  - Projects larger than a single file
- **Preferred workflow:** Working directly in code — create, debug, iterate. Not a fan of long design docs before writing anything.
- **Goal for this project:** Learn to code "for real" by building something I will genuinely use for revision. Success = I use it for a full week of real revision. Not = shipped to the world.

## Why this project

During GCSEs I burned out trying to revise. Anki decks I made myself took too long, and other people's decks weren't aligned to the exam spec. I ended up drilling past papers and watching YouTube for gaps, but ran out of practice questions before the exams. The gap I keep hitting: **flashcard tools that aren't tied to the official spec**, so I can't tell what I've covered vs what I haven't.

I like handwriting my notes in class and rewriting them neatly afterwards — writing is how I process. So this tool does **not** try to be a note app. It's about spec-aligned flashcards and coverage.

## The idea in one paragraph

A personal, single-user web app where every flashcard is attached to a specific point in an official A-level exam specification. I create cards, study them, and see coverage of the spec at a glance. It runs on the internet at a URL only I can access, so I can use it from my phone on the train, on a Chromebook at school, and on my laptop at home.

## Tech stack (v1)

- **Backend:** Python + Flask
- **Database:** SQLite (single file on disk)
- **Templating:** Jinja2 (comes with Flask)
- **Frontend:** Server-rendered HTML + vanilla JS (no React, no build step)
- **Styling:** Plain CSS, one file
- **Deployment:** PythonAnywhere free tier (persistent home directory for SQLite; no card). Docker practiced locally; not required for v1 host.
- **Auth:** HTTP basic auth, one password from an environment variable

No frameworks or libraries beyond this list without a very good reason.

---

## In the MVP

The smallest version that is *actually* useful end-to-end. If any of these are missing, the tool doesn't earn its place in my revision routine.

1. **Flask + SQLite web app**, running locally with `flask run`.
2. **Three tables**: `spec_points` (self-referential tree), `cards` (FK to spec_point), `reviews` (FK to card, rating 1–5, next_due_at).
3. **One subject only** for v1 — Physics or Computer Science (decide when starting).
4. **Spec loaded from a hand-written JSON file** at `specs/<subject>.json`. No PDF parsing.
5. **Spec view** at `/`: renders the spec as a nested tree, click any point to see its cards.
6. **Add card** form under any spec point: front + back, plain text only.
7. **Study mode** at `/study?spec_point=<id>`: cards one at a time, keyboard-driven. Space to flip. 1–5 to rate.
8. **Dumb scheduler**: `next_due_at = now + rating² days`. One function, ~5 lines. That's the whole thing.
9. **Coverage view** at `/coverage`: for each spec point show # cards, # due today, last reviewed. Highlight spec points with zero cards.
10. **Deployed to the internet** at a stable URL (Fly.io recommended). SQLite persists via a mounted volume.
11. **HTTP basic auth**: one hardcoded password from an env var. Prompts on every device once.
12. **Mobile-readable**: works in a phone browser. Not a native app. Not a PWA.

That's it. Everything below this line is explicitly out of scope for v1.

## Parking lot (v2+)

Everything else that has come up or will come up. Written down so it can stop nagging me.

### Content & authoring
- PDF ingestion of official specs (AQA / OCR / Edexcel)
- HTML scraping of exam-board spec pages
- Bulk card import (paste many rows, CSV/TSV)
- LaTeX / KaTeX rendering for maths and physics equations
- Image attachments on cards (diagrams)
- Multi-subject support — all four A-levels in one instance
- Tags / labels on cards ("definition", "formula", "past-paper wording")
- Cloze deletion cards (`{{c1::hidden}}`)
- Card edit / delete history
- Linking past-paper questions to spec points

### Study experience
- Real SRS algorithm (SM-2, later FSRS)
- Cram mode (ignore scheduling, drill everything)
- Session summary at the end (right/wrong, weakest points)
- Aggressive re-review of missed cards inside a session
- Timed study sessions

### Insights & tracking
- Confidence trend graph per spec point over time
- Exam-date-aware suggested schedule ("40 days to Physics paper 1")
- Weekly study time totals
- CSV / JSON export

### Infra & UX
- PWA install / offline mode
- Custom domain
- Multiple deployments / staging environment
- CI/CD

### AI-assisted (deliberately last)
- LLM-drafted card fronts/backs — I approve or edit before saving, never auto-saved
- LLM-generated variants of past-paper questions (fixes the "ran out of questions" burnout trap)
- Auto-tagging pasted content to spec points

### Explicitly never
- User accounts / signup / login system
- Sharing decks with other students
- A marketplace of decks
- Any real-time / multiplayer feature
- Any feature that requires other users to show up for it to be useful

## Traps I've committed to avoiding

- No accounts, no marketplaces, no sharing. It's for me.
- No real-time / multiplayer.
- No feature that needs other users to be useful.
- No framework I don't strictly need. Flask + vanilla JS is the ceiling for v1.
- No premature abstraction. Concrete first, general later.
- No feature added preemptively. Every new feature must come from a real friction I hit while using v1.

## Definition of "done" for v1

I have used the deployed app for **at least one full week of real revision**. After that week, I re-read the parking lot with fresh eyes and pick the **single** next feature to build. I do not add features preemptively, and I do not batch multiple parking-lot items into "v2".

## Core components (what I need to learn end-to-end)

Seven distinct pieces make this project work. Every future feature sits on top of one of these. If a session is confusing, it's usually because I don't yet understand which of these seven it touches.

### 1. Source control — git + GitHub

- **Source control:** a system that tracks every change to my code, so I can go back to any earlier version.
- **git:** the specific tool.
- **Repository ("repo"):** my project's files + its full change history.
- **Commit:** one saved snapshot, with a short message describing what changed.
- **GitHub:** a website that hosts the repo online (backup + shareable copy).

*Why this project needs it:* I will break things — I need to roll back. Fly.io deploys straight from a git repo. It's the single most-used engineering habit; starting on day 1 means I never have to unlearn "save and hope."

### 2. Environment & dependencies — venv + pip + requirements.txt

- **Dependency:** someone else's code my project uses (Flask itself is one).
- **Package manager:** the tool that installs dependencies. Python's is `pip`.
- **Virtual environment ("venv"):** an isolated folder holding one project's dependencies, so different projects don't clash over versions.
- **`requirements.txt`:** a plain-text list of exact dependencies + versions. One command reinstalls them all.

*Why this project needs it:* Fly.io reads `requirements.txt` to build my app in the cloud. On a fresh laptop, one command puts me back in business.

### 3. Backend — Flask + HTTP

- **Backend:** the code that runs *on the server*, not in the user's browser. (Frontend faces the user; backend runs server-side.)
- **Server:** a program that stays running, listening for incoming requests.
- **HTTP:** the shared "language" between browsers and servers. Requests look like `GET /coverage`; responses come back as HTML.
- **Route:** a URL path (`/study`) mapped to a function in my code that decides what to return.
- **Framework:** a library that handles the boring universal parts (parsing HTTP, matching URLs) so I only write the interesting parts. Flask is one.

*Why this project needs it:* A Python script runs, finishes, exits. A server *stays up* and responds to whatever request comes in next. That's why my phone, laptop, and Chromebook can all see the same cards.

*Key distinction to hold onto:* the backend doesn't *store* data itself — it receives requests, applies logic, and delegates storage to the database. Backend = switchboard. Database = filing cabinet.

### 4. Database — SQLite + SQL

- **Database:** a program specialised in storing and retrieving structured data reliably.
- **Table:** a grid with named columns (my three: `spec_points`, `cards`, `reviews`).
- **Row:** one entry in a table.
- **SQL:** the language I use to talk to the database.
- **SQLite:** simplest possible database — the whole DB is one file on disk, no separate server to run.
- **Schema:** the shape of the tables (columns, types, relationships between tables).

*Why this project needs it:* Cards, reviews, `next_due_at` all need to survive restarts and be visible from every device. That's the database's whole job. Backend acts; database remembers.

### 5. Frontend — HTML + CSS + vanilla JS + Jinja templates

- **Frontend:** code that runs in the user's browser.
- **HTML:** page structure (headings, forms, lists).
- **CSS:** look (colours, spacing, layout).
- **JavaScript ("JS"):** interactivity in the browser (respond to a keypress).
- **Template:** an HTML file with placeholders my backend fills in before sending. Flask's template language is called Jinja.

*Why this project needs it:* I want an interface I can use one-handed on the train, not raw JSON. Templates let my Python code hand the browser filled-in HTML instead of building strings by hand in Python.

### 6. Authentication — HTTP basic auth + environment variables

- **Authentication:** proving to the system that I am who I say I am.
- **HTTP basic auth:** the simplest built-in kind. Browser pops up a username/password prompt on the first visit, remembers the answer, and sends it with every request. Server checks it.
- **Environment variable:** a value stored *outside* my code (in the operating system) that my code can read. Used for secrets, so they never end up committed to git.

*Why this project needs it:* The moment the app is public, anyone who guesses the URL can read *and edit* my revision data. ~5 lines of Flask + a password in an env var is enough for a personal tool.

### 7. Deployment — PythonAnywhere (+ Docker practiced locally)

- **Deployment:** running my code somewhere always-on and reachable at a fixed URL.
- **Hosting provider:** rents me a slice of a data centre. **PythonAnywhere** for v1 (free, no card; Flask + files on disk). Fly.io was the original pick until its free tier went away.
- **WSGI file:** the small Python file PA uses to load your Flask `app` object (their “how do I start your code?” hook).
- **Dockerfile / image / container:** still useful concepts (practiced in §9.4). Not how v1 is hosted on PA.
- **Persistence on PA:** your home directory keeps `db.sqlite` across reloads — same *job* a Fly volume would do, different mechanism.

*Why this project needs it:* "Usable from anywhere" requires hosting that isn’t your laptop. PA’s free tier fits a personal Flask + SQLite app without a payment method.

## Milestones (build order)

Each milestone ends with something visibly working. Do them in order. Do not skip ahead.

1. **See the spec** (day 1–2) — Flask app, one route `/`, renders `spec_points` as a nested tree from a hand-written `specs/<subject>.json`.
2. **Make cards** (day 3–5) — click a spec point, get a form, add a card, see it listed under that point.
3. **Study** (day 6–9) — `/study?spec_point=<id>` shows one card at a time, space to flip, 1–5 to rate, writes a `reviews` row with `next_due_at`.
4. **See coverage** (day 10–14) — `/coverage` page: card count, due count, last-reviewed per spec point; zero-card points highlighted.
5. **On the internet** (day 15–18) — HTTP basic auth via `APP_PASSWORD` env var, mobile CSS, deploy to PythonAnywhere (WSGI + static + SQLite in home dir). Dockerfile practiced locally; not required for PA.

After Milestone 5, **stop building and use it for one full week of real revision.** No code changes during that week. Keep an `IDEAS.md` of frictions I hit. Then pick the *single* next feature from the parking lot.

## For future sessions

- Start by reading this file.
- If I ask for a feature not in the MVP list, check the parking lot. If it's there, remind me it's parked and ask if I want to move it into the MVP (which means something has to come *out* to keep MVP small).
- If I ask for a feature not in either list, ask me which list it belongs in before doing anything.
