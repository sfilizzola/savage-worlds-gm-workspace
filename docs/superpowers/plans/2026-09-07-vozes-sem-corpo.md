# Vozes sem Corpo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the second *No Further Action* adventure as a complete English-language, table-ready child adventure.

**Architecture:** Keep stable truths, flexible story points, locations, opposition, secrets, and PC hooks in focused modular Markdown files. Score the copied quality gate before compiling a self-contained `RUN.md`, then update campaign indexes from “weeks later” to the next morning without promoting unused preparation to history.

**Tech Stack:** Markdown adventure sources, Savage Worlds Adventure Edition Fifth Printing (2023), campaign house rules HR-NFA-001 and HR-NFA-002, Python `tools/print-run` renderer.

---

### Task 1: Author authoritative adventure sources

**Files:**
- Create: `campaigns/no-further-action/vozes-sem-corpo/ADVENTURE.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/plot.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/locations.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/secrets.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/characters.md`

- [ ] Write complete configuration, next-morning starting state, objectives, stakes, scope budget, radio brief, and pre-compilation gate.
- [ ] Define flexible story points and the three-clue audit for each essential revelation.
- [ ] Keep every Mood block player-perceivable and every failure consequential but non-blocking.
- [ ] Check that ClearWave and the consortium are absent from player-facing proof.

### Task 2: Author people and opposition

**Files:**
- Create: `campaigns/no-further-action/vozes-sem-corpo/npcs/ray-holtz.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/npcs/cal-briggs.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/npcs/helen-loman.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/encounters.md`

- [ ] Give each named person limited knowledge, an immediate objective, a fear, and distinct speech.
- [ ] Keep Ray and Cal adventure-local unless play makes either recur.
- [ ] Build the compound climax for one Novice Wild Card; use two Extras rather than an opposing Wild Card.
- [ ] Verify all combat statistics and rules reminders against active authority or mark uncertainty explicitly.

### Task 3: Score and compile

**Files:**
- Create: `campaigns/no-further-action/vozes-sem-corpo/QUALITY.md`
- Create: `campaigns/no-further-action/vozes-sem-corpo/RUN.md`

- [ ] Score the five-beat adventure against every quality rank.
- [ ] Pass all three coherence checks and write the logic summary.
- [ ] Compile every required `templates/adventure/SKELETON.md` block in document order.
- [ ] Keep each payload in one home inside `RUN.md`; include speech, statistics, rules, failure-forward reference, end states, and safety.

### Task 4: Correct campaign continuity

**Files:**
- Modify: `campaigns/no-further-action/CAMPAIGN.md`
- Modify: `campaigns/no-further-action/world/lore/timeline.md`
- Modify: `campaigns/no-further-action/world/lore/revelation-ladder.md`

- [ ] Change night 2 from weeks later / working February to the morning after night 1.
- [ ] Index the new folder as drafting while keeping all prepared outcomes non-canon.
- [ ] Preserve the campaign rule that night 3 is months later and unrelated.

### Task 5: Verify the deliverable

- [ ] Run `python3 tools/print-run/test_print_run.py`; expect all printer tests to pass.
- [ ] Run `python3 tools/print-run/render.py campaigns/no-further-action/vozes-sem-corpo/RUN.md`; expect HTML output under the adventure's `print/`.
- [ ] Search authored files for placeholders and prohibited leakage (`TBD`, `TODO`, `<...>`, `ClearWave`, `consortium`).
- [ ] Inspect `git diff --check`, repository status, and the complete diff before reporting completion.
