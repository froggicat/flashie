# v2 build order

Do these in order. Don’t redeploy PythonAnywhere from this branch until we mean to.

1. **Schema** — `users` table; `user_id` on cards/reviews; migrate existing rows to one legacy user
2. **Auth** — register/login/logout; drop HTTP basic auth; scope queries by `user_id`
3. **UI** — design system, mobile study (tap to flip), real nav, empty states
4. **Later (optional)** — React for one rich surface; Postgres + new host if needed

## Repo cleanup done on this branch
- Spec file: `specs/specification.json`
- Removed unused Docker files (still recoverable from `v1-personal`)
- Replaced long v1 learning docs with these two short files