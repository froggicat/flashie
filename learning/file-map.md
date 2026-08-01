# File Map — Every File & Folder, Explained

One line each. **Nothing in this repo is a mystery box.** If a file exists and isn't in this table, I'm not allowed to keep working until it is.

Read alongside `knowledge-graph.md` (what I know) and `project.md` / `plan.md` (what we're building and how). This file is the "what is this file *for*?" layer.

---

## Status legend

| Status | Meaning |
|---|---|
| **known** | I've explained (in my own words) what it is *and* why it exists. I could delete it and predict what would break. |
| **parked** | Honest one-liner for now, but I can't yet defend every detail. **Must** name the section / milestone where I'll come back to it. |
| **generated** | Machine-made. **Never edit by hand.** Must name the tool that produces it and the command that regenerates it. |

## Update rules

- Every new file or folder gets a row **the same session** it appears. Never later.
- If I don't understand a file, it's `parked` — never left blank, never quietly ignored. `parked` rows must include a "revisit in §X" note.
- `generated` rows must name the tool and the exact command that produces the file.
- If a file's purpose changes, the row changes with it — status can flip back down (e.g. `known` → `parked` if I refactor into something I no longer fully grasp).
- Deletions matter too — remove the row *and* leave a one-line note in that session's commit message so I know when it went.

## Path conventions

- Paths are shown relative to the repo root.
- Trailing `/` marks a folder.
- Grouped by folder; folders themselves get a row first, then their contents indented by 2 spaces in the `Path` column.

---

## Repo root — git plumbing and (soon) code

The repo root holds git internals, the `.gitignore` fence, and — from `plan.md` §Section 1.4 onward — application code (`app.py`, `requirements.txt`, `templates/`, `static/`, etc.). Planning docs live in `learning/` (below) so they stay visibly separate from code.

| Path | Status | What it is and why it exists |
|---|---|---|
| `.git/` | parked | Git's internal database for this repo — every commit, every branch, every object lives here. Machine-managed; **never edit by hand**. Created by `git init`. Revisit in task 1.6 (push) when we open `refs/` and see what `HEAD` actually points at. |
| `.gitignore` | known | Fence of files git must pretend don't exist: `.venv/`, `__pycache__/`, `*.pyc`, `db.sqlite`, `.env`, OS junk, editor state. Manually maintained; edit whenever a new class of generated/private file starts appearing. |

---

## The learning/ folder — planning, tracking, self-knowledge. Not shipped code.

Nothing in `learning/` runs. Nothing in here gets packaged or deployed. It exists so future-me (and any agent I work with) can pick up exactly where present-me left off. Read every one of these files at the start of every session before touching code.

| Path | Status | What it is and why it exists |
|---|---|---|
| `learning/` | known | The meta-layer of the project: spec, plan, and self-tracking. Kept in its own folder so it never gets confused with code. |
| &nbsp;&nbsp;`learning/project.md` | known | The "read this first" spec — who I am, what we're building, MVP scope, parking lot, the seven components, and the milestone build order. Source of truth for *what*. |
| &nbsp;&nbsp;`learning/plan.md` | known | Section-by-section build plan with locked tech decisions and the trade-offs each one was picked over. Source of truth for *how* and *in what order*. |
| &nbsp;&nbsp;`learning/knowledge-graph.md` | known | Living record of every concept this project teaches me, with a status ladder (seed → introduced → practicing → understood). Decides what I get quizzed on. |
| &nbsp;&nbsp;`learning/file-map.md` | known | This file. One row per path in the repo so nothing is a mystery box. |

---

## Everything else

Nothing else exists in the repo yet. As soon as a new file or folder appears, it gets a row here, in a new section, in the same session it's created.

Expected upcoming (added on first sight, not now):

- `.venv/` — Python virtual environment (task 1.2). Will land as `parked` on creation, then we'll walk the 4–6 pieces inside that actually matter.
- `requirements.txt` — pinned Python dependencies (task 1.3).
- `app.py` — Flask entry point (task 1.4).
- `templates/` — Jinja templates (`plan.md` §Section 2 onward).
- `static/` — CSS and vanilla JS served directly (`plan.md` §Section 3 onward).
- `specs/` — hand-written JSON spec files (`plan.md` §Section 2 onward).
- `tests/` — `pytest` suite (`plan.md` §Section 8 onward).
- `Dockerfile`, `fly.toml` — infra (`plan.md` §Section 9).
- `.env` — local secrets file (`plan.md` §Section 9). Will exist on disk but *never* on GitHub thanks to `.gitignore`.

Each of those goes from being a placeholder here to a real row the moment its first file lands on disk.
