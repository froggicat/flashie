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
- Grouped by folder; folders themselves get their own row first, then their contents indented by 2 spaces in the `Path` column.

---

## The learning/ folder — planning, tracking, self-knowledge. Not shipped code.

Nothing in `learning/` runs. Nothing in here gets packaged or deployed. It exists so future-me (and any agent I work with) can pick up exactly where present-me left off.

| Path | Status | What it is and why it exists |
|---|---|---|
| `learning/` | known | The meta-layer of the project: spec, plan, and self-tracking. Read every one of these files at the start of every session before touching code. |
| &nbsp;&nbsp;`learning/project.md` | known | The "read this first" spec — who I am, what we're building, MVP scope, parking lot, the seven components, and the milestone build order. Source of truth for *what*. |
| &nbsp;&nbsp;`learning/plan.md` | known | Section-by-section build plan with locked tech decisions and the trade-offs each one was picked over. Source of truth for *how* and *in what order*. |
| &nbsp;&nbsp;`learning/knowledge-graph.md` | known | Living record of every concept this project teaches me, with a status ladder (seed → introduced → practicing → understood). Decides what I get quizzed on. |
| &nbsp;&nbsp;`learning/file-map.md` | known | This file. One line per path in the repo so nothing is a mystery box. Started here because these four files are the only ones that exist so far. |

---

## Everything else

Nothing else exists in the repo yet. As soon as the first application file appears (in Section 1 of `plan.md` — the minimum Flask app), it gets a row here, in a new top-level section beneath this one, in the same session it's created.

Expected upcoming sections (added on first sight, not now):

- `/` (repo root) — for `requirements.txt`, `.gitignore`, `README.md`, and the Flask entry point once they exist.
- `templates/` — Jinja templates (from `plan.md` §Section 2 onward).
- `static/` — CSS and vanilla JS served directly (from `plan.md` §Section 3 onward).
- `specs/` — hand-written JSON spec files (from `plan.md` §Section 2 onward).
- `tests/` — `pytest` suite (from `plan.md` §Section 8 onward).
- Root-level infra files (`Dockerfile`, `fly.toml`) (from `plan.md` §Section 9).

Each of those goes from being a placeholder here to a real row the moment its first file lands on disk.
