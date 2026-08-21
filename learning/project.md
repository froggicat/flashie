# Flashie (v2)

Personal → multi-user flashcard app. Cards live under a shared exam spec tree.
Each account only sees its own cards, reviews, and coverage.

## Stack
- Python + Flask + Jinja + SQLite
- Plain CSS + vanilla JS (no React for now)
- Host: PythonAnywhere for early v2 (v1 phone app stays on PA until we choose to replace it)

## In scope for v2
- User signup / login / logout (sessions, hashed passwords)
- Shared `spec_points`; private `cards` + `reviews` per user
- Study + coverage scoped to the logged-in user
- Clean, responsive UI (after auth works)

## Out of scope for now
- React / SPA rewrite
- Deck sharing marketplace
- Paid hosting / Postgres (until SQLite or PA free becomes painful)

## Branches
- `main` / tag `v1-personal` — frozen single-user app
- `v2-multi-user` — all product work (this branch)