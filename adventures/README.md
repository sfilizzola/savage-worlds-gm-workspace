# Adventures

Each subdirectory is a self-contained one-shot, arc, or campaign unit. Copy `templates/adventure/` to start, except `SKELETON.md`, which stays in `templates/adventure/` as the compile contract. Complexity should emerge from need: a small one-shot may use only `ADVENTURE.md`, `characters.md`, `locations.md`, `QUALITY.md`, and `RUN.md`; a larger work may add the other templates plus `handouts/`, `maps/`, `sources/`, and `sessions/`.

## Required lifecycle

1. **Configure:** complete every required field in `ADVENTURE.md`.
2. **Design:** establish truths, objectives, stakes, story points, pressures, and end states.
3. **Shape:** map the five beats, fill Coherence (prep), and score `QUALITY.md` (120-point checklist). Repair objective, agency, pacing, climax, and any failed coherence row before adding material.
4. **Stress-test:** remove single points of failure and provide meaningful failure consequences.
5. **Verify:** check mechanics against active authority and history against declared sources.
6. **Compile:** build `RUN.md` against `templates/adventure/SKELETON.md`, with runtime material at the point of use, including a first-15-minutes block, five-beat dashboard, climax situation, quoted lines, GM Notes, and at-hand stats.
7. **Play:** treat situations as live state, not a script.
8. **Record:** capture actual events separately from unused preparation.
9. **Reconcile:** update canon and ongoing state only from what was established.

## Suggested directory

```text
adventures/<slug>/
├── ADVENTURE.md
├── QUALITY.md      # scored five-beat map, Coherence (prep), and 120-point checklist
├── plot.md
├── characters.md
├── characters/     # optional pregen .md sheets + print/
├── locations.md
├── encounters.md
├── secrets.md
├── RUN.md
├── handouts/       # optional
├── maps/           # optional
├── sources/        # optional adventure-specific background
└── sessions/       # recaps and ongoing state
```

Pregen A4 print uses the workspace sheet printer at `tools/print-sheets/`, not an adventure-local generator. Call letters and other handout builders stay with the adventure.

