# Adventure RUN Skeleton - Approved Design

## Purpose

Give every compiled `RUN.md` a shared table-writing shape taken from published Savage Worlds one-shots (1shotadventures house style and Pinnacle Test Drive *Blood on the Range*), without turning modular prep into a scene script.

## Decision

**A, with a short contract file.** Modular sources stay the maintainable prep. `templates/adventure/SKELETON.md` is the generation and compile contract. `templates/adventure/RUN.md` is rewritten to match that contract. Existing played or drafted adventures (including Operation Hinterland) are out of scope until a later pass.

## Architecture

- `ADVENTURE.md`, `plot.md`, `locations.md`, `characters.md`, `encounters.md`, `secrets.md` remain source files.
- Those sources gain only the fields compile needs: quoted lines, Trait / fail / success / raise, and a GM Note where a secret exists.
- `templates/adventure/SKELETON.md` lists required blocks, notation, situation order, and the stat-block layout. Do not copy it into an adventure directory.
- Compiling `RUN.md` must satisfy `SKELETON.md`. Missing required blocks fail the compile; do not omit them.
- `QUALITY.md` still scores objective, agency, pacing, and climax. It gains warning-sign checks that quotes, GM Notes, and at-hand stats appear beside the situations that need them.
- `GM.md`, `AGENTS.md`, `HOW_TO_USE.md`, and adventure READMEs point at the skeleton for compile only.

## What the table document must contain

Document-level order is unchanged in intent: header, terms, notation, opening mood, first 15 minutes, mission, current situation, pacing and five-beat dashboards, climax situation, story points, clocks, failure-forward, safety, quick references, secrets, end states, checklist.

Each story-point situation uses this block order: mood, live situation, quoted lines, Trait / fail / success / raise, GM Note, pressure, failure changes, reachable next points, at-hand stats, boxed recurring rules.

Story points remain reachable situations, not a visit order.

## Out of scope

- Rewriting Operation Hinterland or any other existing adventure `RUN.md`.
- Replacing modular files with a single published-style source document.
- Changing the 120-point quality scoring weights.
- Reproducing long copyrighted rules or adventure text.
