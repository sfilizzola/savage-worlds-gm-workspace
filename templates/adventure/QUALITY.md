# Adventure quality gate

Score this adventure before compiling `RUN.md`. Re-score after a major plot change. Copy this file into every generated adventure.

The five-beat shape is a pacing and completeness diagnostic. It is not a scene script and must not replace story points or flexible situations. Map beats onto reachable situations. Players may hit them in another order, skip an optional situation, or create an unplanned path.

A good adventure does **not** need every Savage Worlds subsystem. Use the mechanic the fiction needs. A forced Chase or Dramatic Task is worse than a straightforward scene that belongs there.

## Configuration

| Field | Value |
|---|---|
| Adventure | |
| Declared format | one-shot \| short-arc \| campaign |
| Declared runtime | |
| Scored date | |
| Scored by | |
| Total | /120 |
| Band | |

Bands:

- **100–120:** Strong and ready to compile as ready.
- **80–99:** Solid; repair the weakest one or two ranks before calling it ready.
- **60–79:** Playable, but likely linear, repetitive, or underdeveloped. Rework before a convention or first-time table.
- **Below 60:** Rework the objective, choices, escalation, and climax first. Do not compile as ready.

Ready also requires **Coherence (prep)** and **Grounding audit** to pass. A failed or missing block, or a missing logic summary after a Coherence pass, blocks compile regardless of this total.

## Five-beat map

| Beat | How this adventure delivers it | Story point(s) | One-shot note |
|---|---|---|---|
| 1. Explosive opening | Immediate trouble already in motion: ambush, robbery, attack, chase, discovery, or urgent mission. First 10–15 minutes of play. | | Required for a one-shot. |
| 2. Investigation and meaningful choices | Players gather information, choose allies, explore locations, or decide how to approach the threat. Multiple viable approaches. | | |
| 3. Escalation or reversal | The villain acts, an ally betrays them, the danger spreads, or the original objective becomes harder. | | One major complication, not a chain. |
| 4. Climactic set piece | A memorable location with opposition, environment, urgency, and at least one objective beyond defeating everyone. Prepare the situation; do not script the outcome. | | One large climax. |
| 5. Consequences and closure | Show what changed because of the heroes’ decisions. Rewards or advancement if the format uses them. A hook only if a sequel is intended. | | Complete ending even if further adventures are possible. |

## Coherence (prep)

Pass/fail. Does not change the 120-point total. Fail any row, or omit the logic summary after a pass, and do not compile `RUN.md` as ready.

Copy the one-sentence premise from `ADVENTURE.md`. That sentence is the contract. GM intent and the player-facing briefing are not. False intel is legal if the real problem is already in the starting state and the end states still answer the premise.

**Premise (contract):**

A row passes only if Evidence cites actual prep: premise, truths, starting state, essential story points, and end states, in `ADVENTURE.md` and/or `plot.md` as the adventure uses them. “It feels coherent” is not evidence. An adventure with no `plot.md` still fills this block from `ADVENTURE.md`. **Pass?** is `yes` or `no`, not a 0–5 score.

| Check | Pass? | Evidence |
|---|---|---|
| Beginning with problems | | The starting state already contains the premise’s problem. The job does not appear only as a later reveal, and the opening is not unrelated trouble the premise never named. |
| Causal reachability | | Each essential story point is reachable from predetermined truths plus player decisions. Nothing important exists only because the plot needs it. Order stays flexible. |
| Ending answers the premise | | End states succeed, partly succeed, or fail that same job. They do not answer a different mission or require a scripted last scene to count. |

**Fail if:**

- **Beginning:** the premise’s problem is not in the starting state; the job appears only after a later scene; or the opening is unrelated trouble the premise never named.
- **Reachability:** an essential story point exists only because the plot needs it; it cannot be reached from a truth plus a player decision; or the only way forward is one scripted path.
- **Ending:** end states resolve a different job than the premise, leave the premise’s job unaddressed, or require a scripted last scene to count.

**Not a fail:** false intel; optional dummy sites; player-chosen order; multiple independent vectors to the same essential piece; a climax situation that is “whichever second objective” rather than one unique room.

### Logic summary

Write this section **only if all three rows are `yes`**. If any row is `no`, record the break in Evidence, skip this section, and repair before compile.

Parallel pieces stay parallel. Write “after learning B” only when C actually depends on B. This is not a visit order.

```text
Premise job: <one sentence>

Problems already in play:
- ...

Reachable paths:
- <essential piece A> via <independent vector(s)>
- <essential piece B> via <independent vector(s)>
- <piece C> after learning B, via <vector(s)>   (only if C actually depends on B)

Conclusion: end states agree with these paths. This is not a visit order.
```

## Grounding audit

Pass/fail. Does not change the 120-point total. Fail any row, or leave it blank, and do not compile `RUN.md` as ready.

Coherence checks structure: is each essential piece reachable. This checks a different thing: for each fact the adventure's own tables already promise a player can chase, is there an actual decided value behind it, or only a category standing in for one?

**Trigger:** list every specific value that an Independent vector, a Discoverable roll's Success/Raise result, or an Essential-information line implies a player can obtain, verify, or act on — a plate number, an exact duration, a make/model, a registration or ownership answer, a code, a schedule, a precise location, and similar. Purely atmospheric or Mood-field language is never a row here.

| Fact | Where committed | Concrete value or GM's-call (with reason) | Pass? |
|---|---|---|---|
| | | | |

**Fail if:** a listed fact has neither a concrete value nor a “GM's call — `<reason>`” tag.

**Not a fail:** an explicitly tagged GM's-call item with a stated reason (e.g., “guard count: GM's call — scale to table size”); purely descriptive or Mood detail; a value correctly left to player choice (e.g., which witness she asks first).

## Ranked checklist

Score each item **0–5**, then multiply by its weight. Use the notes column to record the evidence or the repair.

| Rank | Requirement | Weight | Score (0–5) | Weighted | What good looks like | Notes |
|---:|---|---:|---:|---:|---|---|
| 1 | Clear objective and stakes | ×4 | | | Players quickly understand what they need to accomplish, why it matters, and what happens if they fail. | |
| 2 | Player agency | ×4 | | | There are multiple viable approaches and decisions meaningfully change later events. | |
| 3 | Strong pacing and escalation | ×3 | | | The situation keeps changing; scenes do not become repeated fights or information dumps. | |
| 4 | Memorable climax | ×3 | | | The finale combines opposition, environment, urgency, and objectives beyond “kill everyone.” | |
| 5 | Savage Worlds variety | ×2 | | | An appropriate mix of combat, Quick Encounters, Dramatic Tasks, Chases, social scenes, or exploration. Do not force unused subsystems. | |
| 6 | Useful opposition | ×2 | | | Extras provide action and scale while Wild Cards represent genuinely important threats. | |
| 7 | Failure moves the story forward | ×2 | | | Failed rolls introduce costs, danger, lost opportunities, or complications instead of stopping the adventure. | |
| 8 | Player-character relevance | ×2 | | | Hindrances, Edges, relationships, and backgrounds have opportunities to matter. | |
| 9 | Strong locations and imagery | ×1 | | | Each major situation has a recognizable identity, interactive features, and something visually memorable. Story-point Mood is a single player-perceivable paragraph describing the place, not a labeled checklist and not GM editorials. | |
| 10 | Clean ending and rewards | ×1 | | | Players see the consequences, receive rewards or advancement, and understand any continuing hook. | |

**Total (sum of Weighted):** /120

## Warning signs

An adventure needs revision if any of these is true. Repair before compile.

- [ ] One failed Notice, Persuasion, or Research roll can stop the story.
- [ ] Most situations can be summarized as “enter room, fight enemies.”
- [ ] The plot only works if players make one specific choice.
- [ ] A named NPC, secret, or likely fight appears without quoted lines, a GM Note, or at-hand stats beside that situation (`templates/adventure/SKELETON.md`).

## One-shot shape

Complete when `format` is `one-shot`. Ideal for testing an adventure, a convention, or a first-time group.

- [ ] Target **3–4 hours**, or a longer declared runtime with identified cuts down to 3–4 hours.
- [ ] Pregenerated characters with immediate connections, or supplied-PC hooks that engage the premise at once.
- [ ] Opening trouble within the first **10–15 minutes** of play (map-only briefing does not count as the opening).
- [ ] Roughly **4–6 substantial situations**, not a dungeon of rooms.
- [ ] **One** twist or major complication.
- [ ] **One** large climax.
- [ ] Minimal lore and no essential side quests.
- [ ] A complete ending even if further adventures are possible.

Format preference when choosing how to publish or test:

1. Focused one-shot
2. Two- or three-session mini-adventure (`short-arc`)
3. Short campaign
4. Open-ended long campaign

## Short campaign shape

Complete when `format` is `short-arc`. Prefer this if the adventure contains a recurring villain, faction politics, character development, several locations, or consequences that need time to develop.

Target about **6–12 sessions**.

| Arc beat | This adventure / campaign |
|---|---|
| 1. Opening adventure: introduce the danger | |
| 2. Expansion: reveal factions and competing objectives | |
| 3. Reversal: villain gains ground or the heroes’ assumptions prove wrong | |
| 4. Counterattack: players choose their strategy and allies | |
| 5. Finale: decisive confrontation shaped by earlier choices | |

## Long campaign

Use `format: campaign` only when all of the following are true:

- [ ] The setting generates new conflicts.
- [ ] Multiple factions stay active.
- [ ] Villains can adapt.
- [ ] Character advancement is meaningful.
- [ ] Problems do not depend upon the players following one predetermined plot.

Do not stretch a one-shot across twenty sessions. A campaign needs an evolving situation, not more encounters.

## Repair log

| Rank or warning | Problem | Repair | Done |
|---|---|---|---|
| | | | |
