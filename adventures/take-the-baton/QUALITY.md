# Adventure quality gate

Score this adventure before compiling `RUN.md`. Re-score after a major plot change. Copy this file into every generated adventure.

The five-beat shape is a pacing and completeness diagnostic. It is not a scene script and must not replace story points or flexible situations. Map beats onto reachable situations. Players may hit them in another order, skip an optional situation, or create an unplanned path.

A good adventure does **not** need every Savage Worlds subsystem. Use the mechanic the fiction needs. A forced Chase or Dramatic Task is worse than a straightforward scene that belongs there.

## Configuration

| Field | Value |
|---|---|
| Adventure | Take the Baton |
| Declared format | one-shot |
| Declared runtime | 4 hours (3–4 hour core identified) |
| Scored date | 2026-09-12 |
| Scored by | Co-GM (Claude) |
| Total | 93 /120 |
| Band | 80–99 Solid |

Bands:

- **100–120:** Strong and ready to compile as ready.
- **80–99:** Solid; repair the weakest one or two ranks before calling it ready.
- **60–79:** Playable, but likely linear, repetitive, or underdeveloped. Rework before a convention or first-time table.
- **Below 60:** Rework the objective, choices, escalation, and climax first. Do not compile as ready.

Ready also requires **Coherence (prep)** and **Grounding audit** to pass. A failed or missing block, or a missing logic summary after a Coherence pass, blocks compile regardless of this total.

## Five-beat map

| Beat | How this adventure delivers it | Story point(s) | One-shot note |
|---|---|---|---|
| 1. Explosive opening | A PC sees Jesse, unmistakably present and wrong, across the reunion assembly, while Nora is publicly named anchor for the first time. | Story Point 1 | Required for a one-shot. Met. |
| 2. Investigation and meaningful choices | Archives, Hal Prewitt, and Miller's Hole/Jesse — three independent, non-exclusive vectors to the same historical pattern. | Story Points 3, 4, 5 | Multiple viable approaches; none required. |
| 3. Escalation or reversal | The pep rally and retired-jersey ceremony visibly advance Nora's erosion in front of the players. | Story Point 2 | One complication (the ritual's escalating hold), not a chain. |
| 4. Climactic set piece | The state final's anchor exchange — opposition (Coach Arnholt, boosters), environment (packed field, short clock), urgency (the race itself), secondary objective (reach Jesse or the shaft fence). | Story Point 6 | One large climax. |
| 5. Consequences and closure | Five named end states from full success through main-objective failure, each with a concrete, playable consequence. | `plot.md`, "Possible end states" | Complete ending regardless of outcome. |

## Coherence (prep)

Pass/fail. Does not change the 120-point total. Fail any row, or omit the logic summary after a pass, and do not compile `RUN.md` as ready.

**Premise (contract):** Twenty-five years after their state championship, four former teammates return to Colston for the anniversary of that win and must save one of their own — this year's anchor runner — from the same fate that quietly took their fifth teammate the night they became legends.

| Check | Pass? | Evidence |
|---|---|---|
| Beginning with problems | yes | `ADVENTURE.md` "Starting state": Nora is freshly named anchor and Jesse is already visibly present and wrong within the first scene (Story Point 1, `plot.md`). The premise's problem is live at table start, not a later reveal. |
| Causal reachability | yes | Every essential story point is reached through predetermined truths (`ADVENTURE.md`) plus player decision, per the Revelation audit in `plot.md`: three independent vectors to the historical pattern (Story Points 3, 4, 5) and four independent vectors to a climax intervention (Story Point 6). No essential piece exists only because the plot needs it. |
| Ending answers the premise | yes | `plot.md` "Possible end states" resolve the same job the premise names — whether Nora is saved from tonight's mark — across full success, costly success, partial success, and main-objective failure. None require a scripted last scene. |

**Not a fail:** the false-intel-style "winner's curse" newspaper phrase (color, not a clue); Miller's Hole and Hal Prewitt's scene being fully optional and redundant with the archives; the climax's opposition scaling instructions (three or four boosters) being a GM's call rather than a fixed count.

### Logic summary

```text
Premise job: save this year's anchor runner from Colston's recurring toll before it
seals at tonight's championship, and learn enough of the truth to act.

Problems already in play:
- Nora is freshly named anchor.
- Jesse is already visibly present, unaged, and wrong.
- The town is already mid-ceremony, treating tonight as tradition.

Reachable paths:
- Recognizing danger to Nora via Story Points 1 and 2 (direct observation, Toby's
  parental instinct) — both independently sufficient to motivate action.
- Learning the historical pattern via Story Point 3 (archives), Story Point 4 (Hal
  Prewitt), or Story Point 5 (Jesse himself) — any one, none required.
- Intervening at the climax after learning B (the pattern) is not required — Story
  Point 6 offers physical, social, and environmental vectors reachable even if the
  PCs never learn the deeper mechanism, per its Independent vectors list.

Conclusion: end states agree with these paths. This is not a visit order.
```

## Grounding audit

Pass/fail. Does not change the 120-point total. Fail any row, or leave it blank, and do not compile `RUN.md` as ready.

**Trigger:** every specific value an Independent vector, Discoverable roll result, or Essential-information line implies a player can obtain, verify, or act on.

| Fact | Where committed | Concrete value or GM's-call (with reason) | Pass? |
|---|---|---|---|
| Wesley Corbin, 1966 anchor, vanished ~3 weeks after states, presumed drowned at Miller's Hole, no body | `secrets.md` Secret 3; `plot.md` SP3 | Concrete: name, year, role, timeframe, location all specified | yes |
| Denise Kowalski, 1983 anchor, same pattern | `secrets.md` Secret 3; `plot.md` SP3 | Concrete | yes |
| Jesse Calloway, 2001 anchor, same pattern; not actually dead, hollowed and lingering | `ADVENTURE.md` predetermined truths; `secrets.md` Secret 1 | Concrete | yes |
| "The winner's curse" — 1966 letter-to-the-editor phrase | `plot.md` SP3; `secrets.md` Secret 3 | Concrete as color; explicitly tagged as not a clue to a name or culprit | yes |
| The shaft fence is reopened/re-strung every anniversary by the booster committee | `secrets.md` Secret 4; `plot.md` SP5 | Concrete | yes |
| Climax Dramatic Task token requirement | `encounters.md` "The Anchor Exchange" | GM's call — 4–5 tokens/3 rounds at a table of 4, scaled to 3–4 for three players and 5–6 for five, reason stated (match table size, not add named opposition) | yes |
| Number of boosters present at the climax | `encounters.md` "The Anchor Exchange" | GM's call — "three or four," reason stated (scale insistence and noise, not headcount, for a larger table) | yes |
| Nora Sharpe's age and current role | `npcs/nora-sharpe.md`; `ADVENTURE.md` | Concrete: 16, newly named anchor | yes |
| Timeline gaps between incidents (17, 18, 25 years) | `ADVENTURE.md` predetermined truths | Concrete | yes |

## Ranked checklist

Score each item **0–5**, then multiply by its weight. Use the notes column to record the evidence or the repair.

| Rank | Requirement | Weight | Score (0–5) | Weighted | What good looks like | Notes |
|---:|---|---:|---:|---:|---|---|
| 1 | Clear objective and stakes | ×4 | 4 | 16 | Players quickly understand what they need to accomplish, why it matters, and what happens if they fail. | Objective (save Nora) and stakes (act quickly / delay / fail) are explicit in `ADVENTURE.md`; understanding builds across SP1–2 rather than landing in one briefing line, appropriate for the horror genre. |
| 2 | Player agency | ×4 | 4 | 16 | Multiple viable approaches; decisions meaningfully change later events. | Three independent investigation vectors, four independent climax vectors; no single roll, NPC, or PC is required. |
| 3 | Strong pacing and escalation | ×3 | 4 | 12 | The situation keeps changing; scenes do not become repeated fights or information dumps. | Five-beat map delivered across six varied story points; one complication (Nora's advancing erosion), not a chain. |
| 4 | Memorable climax | ×3 | 4 | 12 | Combines opposition, environment, urgency, and objectives beyond "kill everyone." | Opposition (Coach Arnholt, boosters), environment (packed field, short race clock), urgency (the anchor exchange), and a secondary objective (reach Jesse or the shaft fence) all present; no combat required. |
| 5 | Savage Worlds variety | ×2 | 4 | 8 | Appropriate mix of subsystems; nothing forced. | Test (p.107), Dramatic Task (p.122), Social Conflict flavor, and a single optional Fear check; no forced Chase or unused subsystem. |
| 6 | Useful opposition | ×2 | 3 | 6 | Extras provide action and scale while Wild Cards represent genuinely important threats. | Deliberately no Wild Card antagonist — opposition is well-meaning Extras (Coach Arnholt, boosters), and the entity is never statted or fought. Weakest rank: opposition is thin by design; repair is naming this as intentional rather than an oversight (done above) so a GM does not go looking for a missing villain stat block. |
| 7 | Failure moves the story forward | ×2 | 4 | 8 | Failed rolls introduce costs, danger, lost opportunities, or complications instead of stopping the adventure. | Main-objective failure is a fully playable, complete ending (Nora vanishes in the following weeks) rather than a stopped session. |
| 8 | Player-character relevance | ×2 | 4 | 8 | Hindrances, Edges, relationships, and backgrounds have opportunities to matter. | Each PC's Hindrance (Heroic, Secret, Stubborn, Curious) and personal bond to Jesse is load-bearing across multiple story points, not cosmetic. |
| 9 | Strong locations and imagery | ×1 | 4 | 4 | Each major situation has a recognizable identity and something visually memorable. | Gym, field (day/night), library archive, Hal's house, and Miller's Hole are each distinct; Mood-ready first impressions in `locations.md`. |
| 10 | Clean ending and rewards | ×1 | 3 | 3 | Players see the consequences and understand any continuing hook. | Five end states are clear and consequence-driven. Weakest rank: this one-shot has no mechanical advancement (no XP/Advance awarded) — acceptable for the format, but named here as a repair: the GM should say so explicitly at the table rather than leave it implicit. |

**Total (sum of Weighted):** 93 /120

## Warning signs

An adventure needs revision if any of these is true. Repair before compile.

- [ ] One failed Notice, Persuasion, or Research roll can stop the story. — Not present; every essential fact has 2–3 independent vectors (Revelation audit, `plot.md`).
- [ ] Most situations can be summarized as "enter room, fight enemies." — Not present; no situation in this adventure is a combat encounter.
- [ ] The plot only works if players make one specific choice. — Not present; four independent climax vectors.
- [ ] A named NPC, secret, or likely fight appears without quoted lines, a GM Note, or at-hand stats beside that situation. — Not present; verified against `npcs/`, `secrets.md`, and `encounters.md`.

## One-shot shape

Complete when `format` is `one-shot`. Ideal for testing an adventure, a convention, or a first-time group.

- [x] Target **3–4 hours**, or a longer declared runtime with identified cuts down to 3–4 hours. See `ADVENTURE.md` "Scope budget."
- [x] Pregenerated characters with immediate connections. Four returning teammates, all bonded to Jesse and to each other; see `characters.md`.
- [x] Opening trouble within the first **10–15 minutes** of play. Seeing Jesse at the reunion assembly, Story Point 1.
- [x] Roughly **4–6 substantial situations**, not a dungeon of rooms. Six story points, three of them optional/redundant vectors.
- [x] **One** twist or major complication. Nora's advancing erosion across the ritual beats.
- [x] **One** large climax. The state final's anchor exchange.
- [x] Minimal lore and no essential side quests. Miller's Hole and Hal Prewitt's house are both optional.
- [x] A complete ending even if further adventures are possible. Five named end states, `plot.md`.

Format preference when choosing how to publish or test:

1. Focused one-shot
2. Two- or three-session mini-adventure (`short-arc`)
3. Short campaign
4. Open-ended long campaign

## Repair log

| Rank or warning | Problem | Repair | Done |
|---|---|---|---|
| Rank 6 (Useful opposition) | Opposition is entirely non-lethal Extras; no Wild Card antagonist exists to fight | Documented as an intentional design choice in this rank's Notes and in `encounters.md`'s framing, so a GM does not go looking for a missing stat block | Yes — documented, not a mechanical change needed |
| Rank 10 (Clean ending and rewards) | No mechanical advancement/reward is defined for a one-shot | Documented as acceptable for format; GM should state explicitly at the table that consequences, not XP, are the reward tonight | Yes — documented |
