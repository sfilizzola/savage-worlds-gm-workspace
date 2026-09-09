# No Further Action Campaign Index Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an agent-first, human-readable router and compact inventory for the No Further Action campaign without creating a duplicate source of canon.

**Architecture:** A new campaign-root `INDEX.md` owns navigation, task routes, status summaries, and compact inventories. `CAMPAIGN.md` remains authoritative for campaign configuration and planned adventure structure; `world/WORLD.md` remains the persistent-entity hub. Each existing hub receives one thin cross-link.

**Tech Stack:** Markdown, relative links, shell-based link and inventory verification.

---

### Task 1: Assemble authoritative inventory data

**Files:**
- Read: `campaigns/no-further-action/CAMPAIGN.md`
- Read: `campaigns/no-further-action/world/WORLD.md`
- Read: `campaigns/no-further-action/world/lore/timeline.md`
- Read: `campaigns/no-further-action/neblina-sobre-o-lago/session-recap.md`
- Read: `campaigns/no-further-action/vozes-sem-corpo/ADVENTURE.md`
- Read: `campaigns/no-further-action/characters/README.md`
- Read: `rules/house-rules.md`

- [ ] **Step 1: Extract all twelve adventure rows**

Record slug, status, era/calendar, folder state, key artifacts, and one-line purpose directly from `CAMPAIGN.md` and the filesystem.

- [ ] **Step 2: Extract campaign entity inventories**

Record every location, recurring NPC, and lore file linked by `world/WORLD.md`. Read each entity's canon-status field to assign a navigation state tag without inventing canon.

- [ ] **Step 3: Extract child-owned entities**

Record adventure-local NPCs and locations from `vozes-sem-corpo/`, retaining child ownership and preparation status.

- [ ] **Step 4: Confirm current state**

Verify that night 1 is the latest played session, night 2 is drafted preparation, and Frank Loman remains missing in established play.

### Task 2: Write the campaign index

**Files:**
- Create: `campaigns/no-further-action/INDEX.md`

- [ ] **Step 1: Write authority and current-state blocks**

Add the router-not-canon statement, required reading order, current-state snapshot, canon/preparation ladder, and the prominent warning against treating `vozes-sem-corpo` outcomes as history.

- [ ] **Step 2: Write the task router and file legend**

Add ordered minimal file routes for orientation, history, table running, adventure authoring, NPC portrayal, arc secrets, 1998 planning, radio, post-session promotion, and character/print work. Define each campaign and child file type.

- [ ] **Step 3: Write the adventure inventory**

Represent all twelve jobs exactly once. Link existing files and mark concept-only rows as having no folder.

- [ ] **Step 4: Write compact entity inventories**

Add linked one-line entries for recurring NPCs, locations, lore, PC support, house rules, and radio. Separate child-owned people/places and off-screen names from campaign entity files.

- [ ] **Step 5: Write gates and maintenance contract**

Include 1986→1998, rank-rebuild, Whitley-history, KCRK-authorship, faction-location, and world-scope warnings. Define exactly when the index must and need not change.

### Task 3: Add thin cross-links

**Files:**
- Modify: `campaigns/no-further-action/CAMPAIGN.md`
- Modify: `campaigns/no-further-action/world/WORLD.md`

- [ ] **Step 1: Link from CAMPAIGN**

Near the introductory paragraph, add one sentence pointing agents and GMs to `INDEX.md` for task routing, status, and inventories.

- [ ] **Step 2: Link from WORLD**

Near the introductory paragraph, add one sentence pointing to `../INDEX.md` for campaign-level routes and canon tiers.

### Task 4: Verify navigation and boundaries

**Files:**
- Verify: `campaigns/no-further-action/INDEX.md`
- Verify: `campaigns/no-further-action/CAMPAIGN.md`
- Verify: `campaigns/no-further-action/world/WORLD.md`

- [ ] **Step 1: Verify Markdown links**

Run a local script that extracts non-URL Markdown links from `INDEX.md`, removes anchors, resolves each path relative to the index, and fails if any target is absent.

Expected: every relative target exists.

- [ ] **Step 2: Verify adventure coverage**

Compare backticked campaign slugs in the index adventure inventory against the twelve slugs in `CAMPAIGN.md`.

Expected: twelve unique matching slugs; no missing or additional job.

- [ ] **Step 3: Verify world inventory coverage**

Compare linked NPC and location basenames in the index against links in `world/WORLD.md`.

Expected: every persistent entity appears once in the compact inventory.

- [ ] **Step 4: Verify canon language**

Search the index for Frank, `vozes-sem-corpo`, history, preparation, and played-state language. Compare against the recap and timeline.

Expected: Frank remains missing; night 2 outcomes are explicitly preparation.

- [ ] **Step 5: Inspect the final diff**

Run `rtk git diff` and `rtk git status`.

Expected: only the design document, implementation plan, campaign index, and two thin cross-link edits are ours. The pre-existing untracked `.obsidian/` directory remains untouched.
