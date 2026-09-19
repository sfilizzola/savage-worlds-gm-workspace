# RPG Workspace Instructions

Before performing any RPG authoring, editing, rules verification, or session-preparation task:

1. Read and follow `GM.md`.
2. Treat `GM.md` as the authoritative operating policy for this workspace.
3. Read `rules/RULES.md` before writing mechanics.
4. Read the target adventure's `ADVENTURE.md` before modifying it.
5. When the target adventure is under `campaigns/`, also read that campaign's `CAMPAIGN.md`.
6. Do not treat preparation as established canon or session history.
7. When generating or substantially revising an adventure, fill and score `QUALITY.md` from `templates/adventure/QUALITY.md` before compiling `RUN.md`.
8. When compiling `RUN.md`, follow `templates/adventure/SKELETON.md` (including **Table flow (one home)**). Do not omit required blocks.
9. Pregen A4 print uses `tools/print-sheets/` (sheet printer, not a generator). Do not put a sheet renderer inside an adventure.
10. Table print of `RUN.md` uses `tools/print-run/`. Do not put a RUN renderer inside an adventure.

## Shared navigation

These navigation instructions apply to Codex, Claude Code, and Cursor.
`GM.md` remains the authoritative operating policy.

After the required policy reads, use the narrowest route below.
Paths are relative to the repository root unless stated otherwise.

| Task | Read and work here |
|---|---|
| Find an adventure or campaign | `README.md` workspace inventory |
| Resume a standalone adventure | Its `ADVENTURE.md` → Resume work → linked files |
| Resume a campaign | Its `INDEX.md`, or `CAMPAIGN.md` when no index exists → Resume work → linked files |
| Edit a campaign child | Campaign entry point → `CAMPAIGN.md` → child `ADVENTURE.md` → relevant modular sources |
| Establish what happened in play | Relevant session recap → affected canon files and timeline |
| Edit an NPC or location | Existing owning file; use the campaign index to locate persistent entities |
| Verify mechanics | `rules/RULES.md` → target configuration and active house rules → SWADE reference cache → PDF for uncovered cases |
| Print the core GM SWADE card | `rules/gm-quick-ref.md` → `rules/print/gm-quick-ref.pdf` |
| Compile RUN.md | Target configuration and reviewed modular sources → `QUALITY.md` → `templates/adventure/SKELETON.md` |
| Print RUN.md | `tools/print-run/README.md` |
| Edit or print a PC sheet | Owning `characters/README.md` and Markdown sheet → print extracts → `tools/print-sheets/README.md` |
| Change workspace tools | `tools/README.md` → relevant tool README and implementation |
| Investigate an earlier workspace design decision | Relevant `docs/` specification or plan; verify against current policy and files |

Search within the selected adventure or campaign first. Expand to shared
sources when the task requires them. Historical plans explain decisions;
they do not establish current implementation or session history.

## Resume work

Keep one authoring handoff per playable unit:

- Standalone adventure: `ADVENTURE.md`.
- Campaign: `INDEX.md`, falling back to `CAMPAIGN.md` when no index exists.
- Campaign child work: identify the child in the campaign handoff.

Read the handoff when resuming work. The current user request takes
precedence over a recorded next action. Confirm handoff claims against
their linked files before relying on them.

After substantial work finishes or pauses, update the handoff with:

- Current task.
- Last completed.
- Next concrete action.
- Files to open.
- Open GM questions.
- Derived outputs needing refresh.

Record completed actions and known pending work accurately. Mark unknown
state explicitly. Do not infer a prior task from file dates or invent
GM decisions. A next action records intent; it does not expand authorization.

Keep the handoff concise and replace superseded entries. Link to owning
files instead of copying lore, mechanics, quality scores, or session events.
Session events belong in recaps; the handoff records authoring progress.
