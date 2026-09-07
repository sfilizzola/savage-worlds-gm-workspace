# Campaign Folder Structure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add campaign parent templates and documentation while preserving flat standalone adventures and the existing Operation Hinterland layout.

**Architecture:** Standalone adventures remain under `adventures/<slug>/`. Linked play lives under `campaigns/<campaign-slug>/`, where `CAMPAIGN.md`, campaign-local `world/`, and canonical `characters/` sit beside ordinary child adventure folders identified by `ADVENTURE.md`. Existing printers continue accepting explicit file paths. Documentation and path wording change; the RUN printer’s default output directory is based on the input filename (`RUN.md` → parent `print/`), not on living under `adventures/`. That one behavior change, with a test, is required so campaign nights match standalone.

**Tech Stack:** Markdown templates and documentation, Git, ripgrep, existing Python printer test suites.

---

### Task 1: Add the campaign template and root

**Files:**
- Create: `campaigns/README.md`
- Create: `templates/campaign/CAMPAIGN.md`
- Create: `templates/campaign/characters/README.md`
- Create: `templates/campaign/world/WORLD.md`
- Create: `templates/campaign/world/locations/README.md`
- Create: `templates/campaign/world/factions/README.md`
- Create: `templates/campaign/world/npcs/README.md`
- Create: `templates/campaign/world/lore/README.md`

- [ ] **Step 1: Create `campaigns/README.md`**

Document that `campaigns/<slug>/` owns table-wide context, campaign characters, and child adventure folders. State that child adventures sit directly beside `world/` and `characters/`, and that standalone one-shots remain under `adventures/`.

- [ ] **Step 2: Create `templates/campaign/CAMPAIGN.md`**

Add complete YAML front matter with:

```yaml
---
title: "<Campaign title>"
status: concept
language: en
format: short-arc
system: "SWADE Fifth Printing (2023)"
rank: "Novice"
players: "4-6"
pc_mode: both
setting_modules: []
supernatural_level: none
historical_accuracy:
  requirement: not-applicable
  scope: "<What must be accurate, or why this is not applicable>"
  sources: []
house_rules: none
---
```

Add allowed-value guidance and the required sections: one-sentence throughline, GM intent, campaign predetermined truths, party index, adventure index, canon boundaries, and child-adventure exceptions.

- [ ] **Step 3: Create campaign character guidance**

In `templates/campaign/characters/README.md`, make campaign `.md` sheets and `characters/print/chars.json` canonical. Include:

```text
python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json
```

State that child adventures link to these sheets and may contain night hooks in `characters.md`, but never duplicate full mechanical sheets.

- [ ] **Step 4: Create campaign world stubs**

Mirror the current root `world/` responsibilities. `templates/campaign/world/WORLD.md` must distinguish this table’s canon from setting-wide root `world/`. The four child READMEs must respectively describe persistent locations, factions, recurring NPCs, and lore/timelines, with no sample canon.

- [ ] **Step 5: Verify the new skeleton**

Run:

```bash
rtk find 'templates/campaign|campaigns/README.md'
```

Expected: all eight template files and `campaigns/README.md` are listed; no real `campaigns/<slug>/` exists.

### Task 2: Update workspace policy and navigation

**Files:**
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `GM.md`
- Modify: `adventures/README.md`
- Modify: `world/WORLD.md`

- [ ] **Step 1: Update the root start-here and repository map**

In `README.md`, describe both starts:

```text
Standalone: templates/adventure/ → adventures/<adventure-slug>/
Linked play: templates/campaign/ → campaigns/<campaign-slug>/, then add child adventures
```

Add `campaigns/` to the repository map and clarify that `adventures/` now means standalone units.

- [ ] **Step 2: Add the campaign read requirement**

In `AGENTS.md`, add a rule after the target-adventure read:

```text
When the target adventure is under `campaigns/`, also read that campaign's `CAMPAIGN.md`.
```

Do not change the mechanics, quality, or printer policies.

- [ ] **Step 3: Add a concise organization policy to `GM.md`**

Under “One-shot, short campaign, or long campaign,” explain:

- standalone one-shots live at `adventures/<slug>/`;
- linked play lives at `campaigns/<slug>/`, with child adventures beside campaign `world/` and `characters/`;
- a campaign may be created first, or a standalone adventure may later be adopted;
- shared table state belongs to campaign `world/`, while root `world/` stays setting-wide.

- [ ] **Step 4: Narrow `adventures/README.md`**

Change it from “one-shot, arc, or campaign unit” to standalone adventures and unsplit single-folder units. Link to `campaigns/README.md` for linked play. Keep the existing adventure lifecycle and suggested directory.

- [ ] **Step 5: Clarify root world scope**

In `world/WORLD.md`, state that it is setting-wide canon shared across tables. Point campaign-specific evolving canon to `campaigns/<slug>/world/`.

- [ ] **Step 6: Verify policy wording**

Run:

```bash
rtk grep 'campaigns/<|CAMPAIGN.md|setting-wide' README.md AGENTS.md GM.md adventures/README.md world/WORLD.md
```

Expected: each responsibility and required read appears; no text claims all adventures must live directly under `adventures/`.

### Task 3: Document campaign-first, adoption, and continuation

**Files:**
- Modify: `HOW_TO_USE.md`

- [ ] **Step 1: Correct the opening and embedded `AGENTS.md` example**

Explain both playable roots in the introduction. Add the campaign read rule to the embedded instruction block so copied setup guidance matches root `AGENTS.md`.

- [ ] **Step 2: Add “Start a campaign or short arc”**

Before the standalone-adventure workflow, add exact instructions to:

1. copy `templates/campaign/` to `campaigns/<campaign-slug>/`;
2. complete `CAMPAIGN.md`;
3. create canonical party sheets under campaign `characters/`;
4. add table canon under campaign `world/` only as established;
5. copy `templates/adventure/` (excluding `SKELETON.md`) to `campaigns/<campaign-slug>/<adventure-slug>/`;
6. repeat shared configuration in the child `ADVENTURE.md`;
7. link the child in `CAMPAIGN.md`.

- [ ] **Step 3: Add “Adopt a standalone adventure”**

Include the approved checklist and concrete move:

```text
git mv adventures/<adventure-slug> campaigns/<campaign-slug>/<adventure-slug>
```

Require resolving duplicate party sheets in favor of campaign `characters/`, leaving hooks/links in the child, promoting only recurring facts to campaign `world/`, updating the adventure index, and repairing hardcoded old paths. Explicitly forbid leaving a duplicate stub under `adventures/`.

- [ ] **Step 4: Generalize character, source, and RUN paths**

Keep Operation Hinterland as the standalone example, and add campaign equivalents:

```text
campaigns/<campaign-slug>/characters/print/chars.json
campaigns/<campaign-slug>/<adventure-slug>/sources/
campaigns/<campaign-slug>/<adventure-slug>/RUN.md
```

- [ ] **Step 5: Rewrite “Continue a campaign or short arc”**

Require reading `CAMPAIGN.md`, campaign `world/`, root setting-wide `world/`, the child `ADVENTURE.md`, and latest child recap. State that the next session is a child adventure folder (new or existing), never a campaign-root `RUN.md`.

- [ ] **Step 6: Verify both workflows are complete**

Run:

```bash
rtk grep 'Start a campaign|Adopt a standalone|git mv adventures|campaigns/<campaign-slug>|Continue a campaign' HOW_TO_USE.md
```

Expected: campaign-first, adventure-first adoption, campaign character paths, child RUN paths, and continuation all appear.

### Task 4: Generalize printer and NPC path documentation

**Files:**
- Modify: `tools/README.md`
- Modify: `tools/print-run/README.md`
- Modify: `tools/print-sheets/README.md`
- Modify: `templates/adventure/characters.md`
- Modify: `templates/adventure/SKELETON.md`
- Modify: `.cursor/skills/npc-voice/SKILL.md`
- Modify: `tools/print-run/render.py` (wording plus `default_out_dir` for `RUN.md`)
- Modify: `tools/print-sheets/render.py`

- [ ] **Step 1: Generalize tool ownership wording**

In `tools/README.md`, state:

- standalone data: `adventures/<slug>/`;
- campaign night: `campaigns/<campaign-slug>/<adventure-slug>/`;
- campaign party: `campaigns/<campaign-slug>/characters/`;
- handouts stay with the owning adventure.

- [ ] **Step 2: Add parallel campaign printer examples**

In the printer READMEs and `templates/adventure/characters.md`, preserve the standalone examples and add:

```text
python3 tools/print-run/render.py campaigns/<campaign-slug>/<adventure-slug>/RUN.md --pdf
python3 tools/print-sheets/render.py campaigns/<campaign-slug>/characters/print/chars.json --pdf
```

Explain that output remains beside the input (`<adventure>/print/` for any `RUN.md`, standalone or campaign child, and the character print directory for sheets). The bare campaign command is enough; `--out-dir` is an optional override, not required for campaign nights.

- [ ] **Step 3: Generalize source comments and CLI help**

Change wording in `templates/adventure/SKELETON.md`, `tools/print-run/render.py`, and `tools/print-sheets/render.py` that implies a fixed `adventures/<slug>/` home. Use `<path-to-adventure>/RUN.md` and `<path-to-characters>/print/chars.json`.

User-approved correction: `default_out_dir` must treat an explicitly passed file named `RUN.md` as `<parent>/print/`, whether under `adventures/` or `campaigns/`. Other markdown filenames still default to the same directory. Add a test for `/repo/campaigns/demo/episode/RUN.md` → `/repo/campaigns/demo/episode/print`. This is the only printer behavior change; sheet printer path computation stays unchanged.

- [ ] **Step 4: Update npc-voice destination rules**

Replace fixed `adventures/<slug>/npcs/<name>.md` wording with:

- existing named NPC file: edit in place;
- campaign-recurring NPC: `campaigns/<campaign-slug>/world/npcs/<name>.md`;
- otherwise: `<adventure>/npcs/<name>.md`, regardless of playable root;
- never player sheets or repo-root `world/npcs/` unless the GM asks.

Apply this consistently in the write path, named-vs-extra table, and file mapping.

- [ ] **Step 5: Scan for live fixed-root assumptions**

Run:

```bash
rtk grep 'adventures/<slug>|adventures/<adventure-name>|Adventure data stays' README.md HOW_TO_USE.md AGENTS.md GM.md adventures world templates tools .cursor/skills/npc-voice
```

Expected: remaining matches are intentional standalone examples paired with campaign guidance, not universal claims.

### Task 5: Verify the documentation and RUN default-path change

**Files:**
- Verify: all files changed in Tasks 1–4
- Verify unchanged: `adventures/operation-hinterland/`

- [ ] **Step 1: Run printer regression tests**

Run:

```bash
rtk test python3 tools/print-run/test_print_run.py
rtk python3 -m py_compile tools/print-sheets/render.py
```

Expected: the RUN printer suite passes (including campaign `RUN.md` → `<adventure>/print/`) and the sheet printer compiles without syntax errors. The sheet printer has no test suite; do not create one for wording-only changes.

- [ ] **Step 2: Confirm no real campaign or Hinterland change**

Run:

```bash
rtk git diff -- adventures/operation-hinterland
rtk find 'campaigns/*/ADVENTURE.md'
```

Expected: Hinterland diff is empty; no real campaign adventure exists.

- [ ] **Step 3: Review the complete diff**

Run:

```bash
rtk git diff --check
rtk git diff
rtk git status
```

Expected: no whitespace errors; changes are limited to the approved campaign template, policies, path documentation, plan/spec correction, wording-only CLI comments/help, and the RUN printer `default_out_dir` + test for `RUN.md` → parent `print/`.

- [ ] **Step 4: Report completion without committing**

Summarize created and modified files, test results, and any intentional remaining standalone-only examples. Do not commit implementation changes unless the GM explicitly asks.
