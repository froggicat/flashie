# v2 build order

Do these in order. Each small step ends in something you can see working.
You write most of the code; use the agent to explain, review, and unstick — not to dump finished features.

**Rules**
- Stay on branch `v2-multi-user`. Don’t redeploy PythonAnywhere until you mean to replace v1.
- Prefer understanding over speed. If a step is confusing, stop and ask before stacking more changes.
- Commit when a chunk of steps feels stable (you don’t need a commit per checkbox).

---

## 1. Schema — users own cards and reviews

**Goal:** the database knows *who* a card/review belongs to. Spec tree stays shared.

### 1.1 — Sketch the `users` table
- [ ] On paper or in a comment, list columns you want: at least `id`, `email` (unique), `password_hash`, `created_at`.
- [ ] Write one sentence: why cards need a `user_id` but `spec_points` do not.
- **Visible:** you can explain the design out loud before touching SQL.

### 1.2 — Create `users` in the DB
- [ ] Add a small script (e.g. `migrate.py`) or extend `explore_db.py` that `CREATE TABLE`s `users` if missing.
- [ ] Run it against local `db.sqlite`.
- **Visible:** query `sqlite_master` (or a quick Python `SELECT`) and see `users` listed.

### 1.3 — Add `user_id` to `cards`
- [ ] `ALTER TABLE cards ADD COLUMN user_id INTEGER REFERENCES users(id);` (SQLite-friendly approach; note existing rows will have `NULL` user_id for now).
- [ ] Confirm with `PRAGMA table_info(cards);`.
- **Visible:** `user_id` appears as a column; old cards still load in the app.

### 1.4 — Add `user_id` to `reviews`
- [ ] Same idea for `reviews`.
- **Visible:** `PRAGMA table_info(reviews);` shows `user_id`.

### 1.5 — Create a legacy user and attach old data
- [ ] INSERT one user (e.g. your email + a temporary hash or placeholder — real hashing comes in §2).
- [ ] `UPDATE cards SET user_id = ?` and `UPDATE reviews SET user_id = ?` for that user’s id where `user_id IS NULL`.
- **Visible:** every card/review row has a non-NULL `user_id`; app still behaves like v1 locally.

### 1.6 — Document the new schema
- [ ] Update `README.md` schema section to match reality.
- **Visible:** README matches what `PRAGMA table_info` shows.

---

## 2. Auth — real login, then lock data to the session

**Goal:** replace shared `APP_PASSWORD` basic auth with per-user register/login. Every card/review query is scoped to the logged-in user.

### 2.1 — Secret key for sessions
- [ ] Set `app.secret_key` from an environment variable (e.g. `SECRET_KEY`), with a clear error if missing in production-minded setups.
- [ ] Run locally with the env var set; confirm the app still starts.
- **Visible:** Flask runs; you know sessions need a secret.

### 2.2 — Password hashing helpers
- [ ] In a small module or in `app.py`, try `generate_password_hash` / `check_password_hash` (Werkzeug) in the REPL or a tiny script with a fake password.
- **Visible:** hash looks nothing like the password; check returns True/False correctly.

### 2.3 — Register page (GET form)
- [ ] Route + template: email + password fields, no DB write yet (or write only after you’re happy with the form).
- **Visible:** `/register` shows a form.

### 2.4 — Register (POST → INSERT user)
- [ ] On submit: hash password, INSERT into `users`, handle “email already taken”.
- [ ] Redirect to login (or auto-login — pick one and stick to it).
- **Visible:** new row in `users`; duplicate email fails gracefully.

### 2.5 — Login page + session
- [ ] `/login` form; on success set `session["user_id"]` (and maybe email for display).
- [ ] `/logout` clears the session.
- **Visible:** log in → session set; log out → session gone (check with a tiny debug print or a “logged in as …” line).

### 2.6 — Require login for app pages
- [ ] Helper like `current_user_id()` / `login_required` pattern (decorator or `before_request` that skips only `/login`, `/register`, static).
- [ ] Remove HTTP basic auth (`before_request` password check + `APP_PASSWORD` gate).
- **Visible:** logged out user hitting `/` goes to login; logged in user sees the app. No browser basic-auth dialog.

### 2.7 — Scope writes by `user_id`
- [ ] INSERT card includes `user_id` from the session.
- [ ] INSERT review includes `user_id` from the session (and/or rely on card ownership checks).
- **Visible:** new cards in the DB have your user id.

### 2.8 — Scope reads by `user_id`
- [ ] Spec page card list: `WHERE spec_point_id = ? AND user_id = ?`.
- [ ] Study due-card query: only that user’s cards/reviews.
- [ ] Coverage aggregates: only that user’s cards/reviews.
- **Visible:** second test user (register another account) does **not** see the first user’s cards; coverage differs per account.

### 2.9 — Nav links for auth
- [ ] In `base.html`: Login / Register when logged out; email + Logout when logged in.
- **Visible:** you can move between states without typing URLs.

---

## 3. UI — make it pleasant on phone and desktop

**Goal:** sleek, responsive, usable — still Jinja + CSS + vanilla JS (no React yet).

### 3.1 — Design tokens
- [ ] In `style.css`, define CSS variables for background, text, accent, spacing, radii, fonts (pick a real font via Google Fonts or similar — avoid generic “AI purple” defaults if you can).
- **Visible:** change one variable and several elements update.

### 3.2 — Base layout + nav
- [ ] Restyle `base.html` shell: header, nav, main content width, readable type scale.
- **Visible:** every page shares a coherent chrome.

### 3.3 — Study: tap to flip
- [ ] Click/tap on the card toggles the back (keep Space as a bonus on desktop).
- [ ] Optional: a visible “Show answer” control for phones.
- **Visible:** flip works on phone with no keyboard.

### 3.4 — Study: thumb-friendly ratings
- [ ] Big rating buttons; spacing that works one-handed.
- **Visible:** rate a card on phone without mis-taps.

### 3.5 — Spec tree + forms
- [ ] Restyle tree, card list, add-card form so they feel intentional (not browser defaults).
- **Visible:** adding a card feels like a product, not a homework form.

### 3.6 — Coverage as a dashboard
- [ ] Clear hierarchy: what to revise next; zero-card rows still obvious; links easy to hit.
- **Visible:** you can answer “what should I do next?” in one glance.

### 3.7 — Empty states
- [ ] New user with no cards sees helpful copy + a path to add the first card (not a blank void).
- **Visible:** register a fresh account and the empty experience makes sense.

### 3.8 — Auth pages polish
- [ ] Login/register match the same design system.
- **Visible:** no “ugly form, pretty app” split.

---

## 4. Later (optional) — only when something forces it

Don’t start these until Phases 1–3 are actually usable.

### 4.1 — React learning track (optional)
- [ ] Pick **one** surface (e.g. study session) that hurts as server-rendered HTML.
- [ ] Flask JSON API for that surface only; small React app for it.
- **Visible:** that one page is React; the rest stay Jinja.

### 4.2 — Postgres + new host (optional)
- [ ] When SQLite locking or PA free limits hurt real users, move DB/host.
- [ ] Rewrite Docker only if the new host needs it (recover old files from `v1-personal` if useful).
- **Visible:** app runs on the new host with migrations that preserve user data.

---

## Already done on this branch
- [x] Spec file renamed to `specs/specification.json` (+ `import_spec.py` / README)
- [x] Removed unused Docker files (recoverable from `v1-personal`)
- [x] Replaced long v1 learning docs with short `project.md` + this plan
- [x] Branch `v2-multi-user` created; `main` / `v1-personal` frozen
