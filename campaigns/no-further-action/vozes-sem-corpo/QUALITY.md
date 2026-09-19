# Adventure quality gate

Scored before compiling `RUN.md`. The five beats diagnose pacing; they do not impose order.

## Configuration

| Field | Value |
|---|---|
| Adventure | Vozes sem Corpo |
| Declared format | one-shot |
| Declared runtime | 3–5 hours |
| Scored date | 2026-09-09 |
| Scored by | Co-GM |
| Total | 108/120 |
| Band | Numeric band: Strong (108/120). Grounding audit passed; RUN still needs rebuild. |

## Five-beat map

| Beat | How this adventure delivers it | Story point(s) | One-shot note |
|---|---|---|---|
| 1. Explosive opening | Ray is already attempting to remove the original reel; Lilly must decide custody, copying, challenge, or tail immediately. | Tape in Motion | Trouble is live in the first 10–15 minutes. |
| 2. Investigation and meaningful choices | Technical comparison, town witnesses, and access paperwork are parallel routes whose results affect time and evidence quality. | Missing Interval; Two Outsiders; Paper That Does Not Land | Multiple viable approaches; no essential side quest. |
| 3. Escalation or reversal | Once alerted, the crew changes from quiet retrieval to erasing the compound and moving Frank. | Triggered from any investigative point; manifests at Tower Compound | One major complication. |
| 4. Climactic set piece | Two Extras, wet metal, darkness, live equipment, truck, cleanup sequence, and body/original preservation. | Tower Compound | One large climax; defeating everyone is insufficient. |
| 5. Consequences and closure | The evidence Lilly protected determines whether the file proves murder, staging, the gap, or remains contested. | Disposition | Complete local ending; no hidden organization exposed. |

## Coherence (prep)

**Premise (contract):** The morning after Chief Whitley shelves Frank Loman, Lilly reaches 102.3 FM while a purported engineer is already trying to take Abigail's reel, and she must find Frank and preserve enough independent evidence to prevent the file from being honestly dismissed as a drowning before the crew moves his body and erases the originals.

| Check | Pass? | Evidence |
|---|---|---|
| Beginning with problems | yes | `ADVENTURE.md` Starting state puts Ray at 102.3 FM seeking the original reel while Frank remains at the compound and Cal prepares body/truck movement without destroying records until alerted. Story Point 1 begins with this exact custody problem. |
| Causal reachability | yes | Predetermined truths generate the reel, dispatch gap, witnesses, work order, truck route, and compound. `plot.md` gives independent vectors and reachable links among all six points; no point requires one visit order. |
| Ending answers the premise | yes | `plot.md` end states and Disposition resolve what happened to Frank and measure whether protected evidence can defeat drowning, including degraded failure states. |

### Logic summary

Premise job: Hear the tape, find Frank, and preserve enough independent evidence to prevent the file from being honestly dismissed as a drowning before cleanup.

Problems already in play:
- Ray is attempting to remove the reel at table start.
- Frank is dead at the compound and Cal can move him.
- Originals can be erased while local memory and paperwork are still fresh.

Reachable paths:
- The synchronized interval via station/dispatch comparison, maintenance timing, or the optional mud cassette.
- The two-man crew and inland lake-road route via Daisy’s / West End Fuel witnesses, Nancy/patrol knowledge, station observation, or access paperwork.
- Compound access via truck route, key register, maintenance timing, Ray's trail, or tower context on the cassette.
- Frank's murder and staged lake via the body, staging materials, crew conduct/statements, and signal equipment.

Conclusion: end states agree with these paths. This is not a visit order.

## Grounding audit

**Audit date:** 2026-09-19. **Auditor:** Codex co-GM (initial fail); Cursor co-GM recorded GM-approved values through G32 and rechecked this table against `ADVENTURE.md`, `plot.md`, `secrets.md`, `locations.md`, `encounters.md`, and local NPC files. **Result: PASS — 0 unresolved rows of 36.** Numeric score remains 108/120. `RUN.md` and print outputs still predate these values and must be rebuilt before table use; a stale RUN is a compile problem, not a remaining grounding gap.

**Scope:** checked the information promised by the six story points' Essential information, Independent vectors, and Discoverable results in [plot.md](plot.md), [RUN.md](RUN.md), [locations.md](locations.md), [secrets.md](secrets.md), and [encounters.md](encounters.md), together with [ADVENTURE.md](ADVENTURE.md), local NPC files, the campaign configuration and relevant world files, and the session-1 recap. Source pointers below use SP1–SP6 for the corresponding story points. This checks prepared facts, not rules legality, historical accuracy, or a fresh full Coherence review.

**Method:** a pass needs an existing concrete answer, an explicitly reasoned GM's call, or a value appropriately left to player choice. A named evidence category or a conclusion without the promised underlying value fails. Missing answers were not invented to pass the audit. Player-facing notebook material was checked for continuity only and receives no unplayed answers.

| Fact | Where committed | Concrete value or GM's-call (with reason) | Pass? |
|---|---|---|---|
| G01 — Missing duration | ADVENTURE.md, Predetermined truths; plot.md SP2; secrets.md VSC-02 | Exactly 1 minute 52 seconds, repeated across the independent records. | yes |
| G02 — Missing interval start and stop | ADVENTURE.md, Predetermined truths; plot.md SP2 Research; secrets.md VSC-02; RUN.md SP2/SP4 | GM approved: 9:14:00–9:15:52 p.m. on the evening of session 1, shared by station and dispatch; maintenance log refers to the same clock window. The exact campaign calendar date remains unset. Present in the compiled RUN. | yes |
| G03 — Reel counter positions | ADVENTURE.md, Predetermined truths; plot.md SP1 Notice raise; locations.md KCRK; RUN.md SP1 | GM approved: machine counter 0418 immediately before the cut and 0419 immediately after. These are reel position marks, not clock time or a measure of the 1 minute 52 second interval; station/dispatch logs supply elapsed time. Present in the compiled RUN. | yes |
| G04 — Ray's arrival time | ADVENTURE.md, Predetermined truths and Starting state; plot.md SP1 Persuasion raise; locations.md KCRK; RUN.md SP1 | GM approved: Ray arrived at 8:45 a.m. on the morning after session 1. Abigail refused the original reel, keeping him at KCRK when Lilly arrives later; her exact arrival time remains open. Present in the compiled RUN. | yes |
| G05 — Identity and source of the voice | plot.md SP1/SP2; secrets.md VSC-01; ADVENTURE.md | Lilly's surname is heard in captured local police traffic, replayed through the crew's equipment. It is not a live supernatural voice. No full transcript is promised. | yes |
| G06 — Maintenance notation and timing discrepancy | plot.md SP2/SP4 Research raises; secrets.md VSC-02; locations.md Town Hall public works | GM approved: typed sheet says “tower isolated 9:16 p.m.” while handwritten key-board note says “tower key out 9:14 p.m. — C. Briggs,” placing Cal's access inside the 9:14:00–9:15:52 interval. | yes |
| G07 — Mud cassette custody/location | ADVENTURE.md, Predetermined truths; plot.md SP2; secrets.md VSC-01 | Session 1 did not record custody. Final-run GM call: precinct property area with incomplete seal/date fields; an explicit player memory of another location overrides this prep default. Recovery costs time/custody and is optional. | yes |
| G08 — Legible cassette work label | plot.md SP2 Notice fail; RUN.md SP2; technical vector to SP5 | GM approved: TDK SA C-60, mud-smudged white sticker, Ray's ballpoint **ALIGN CK — TWR 2**. Routine tower/alignment work media; no road, agency, or clock time. Present in the compiled RUN. | yes |
| G09 — Cassette's independent timing marks | plot.md SP2 Notice raise; secrets.md VSC-02; Revelation audit | GM approved: yellow leader spliced at the head of the capture block and again after it. Splice-to-splice play is exactly 1 minute 52 seconds. No clock times or 0418/0419 on the cassette. Present in the compiled RUN. | yes |
| G10 — Two men and their split | ADVENTURE.md; plot.md SP3; locations.md Daisy's/West End Fuel | Ray Holtz and Cal Briggs ate early at Daisy's. Ray drove south toward KCRK; Cal took the truck toward Barrow Lake Rd / Co. Rd. 12, not 328 east toward Lowater. | yes |
| G11 — Truck description and partial plate | plot.md SP3 Persuasion fail/raise; RUN.md SP3; locations.md Daisy's | GM approved: faded chrome-yellow utility; **LANE CO.** door stencil; raise remembers Oregon **WNT 41_** (last character unread). Full plate waits until Lilly sees the truck. Ray's car remains XLR 204. Present in the compiled RUN. | yes |
| G12 — Fuel slip time and vehicle match | plot.md SP3 Persuasion raise and Notice success; SP4 paper vector | GM approved: West End Fuel carbon **8:22 a.m.**, pump 1, **12.4 gal diesel**, scrawl **YEL LANE** and **WNT 41**. Identifies the yellow Lane County truck, not the Maxima. Destination is still attendant testimony (not 328 toward Lowater). Present in the compiled RUN. | yes |
| G13 — Identifiable early-shift witnesses | plot.md SP3 Common Knowledge raise; locations.md Records/West End Fuel; campaign Daisy's file | Daisy Pell is specified at the breakfast register. GM approved: **Bud Ellison** on the West End Fuel early island; adventure-local extra in [`npcs/bud-ellison.md`](npcs/bud-ellison.md). Present in the compiled RUN. | yes |
| G14 — Ray's car | ADVENTURE.md; plot.md SP3; npcs/ray-holtz.md; RUN.md SP1/SP3 | Slate-gray 1983 Datsun 810 Maxima sedan, Oregon XLR 204. Parked at Daisy's during breakfast, then driven to KCRK. | yes |
| G15 — Car-registration/rental return | ADVENTURE.md; plot.md SP3 Notice/Research raise; RUN.md SP3 | GM approved: **Valley U-Drive**, Eugene; cash renter **Alan Vickers**; no local ID match. Ownership remains unresolved. Present in the compiled RUN. | yes |
| G16 — Mud comparison | plot.md SP3 Notice raise; locations.md West End Fuel; RUN.md SP3 | GM approved: orange-red clay with angular crushed-basalt chips at the fuel parking smear and inland shoulder; lake bank is gray organic silt with pine needles; KCRK lot is wet river gravel and asphalt fines. Visual match, not a lab. Present in the compiled RUN. | yes |
| G17 — Named town locations | locations.md; campaign world/locations/ashgrove.md and daisys.md | KCRK south of the river at Bridge Street; Daisy's south of Main east of Church; West End Fuel west of Mill south of Main; public works in Town Hall with PD. The compound is a separate site. | yes |
| G18 — Precise compound access | plot.md SP3/SP4/SP5 vectors; RUN.md Finding the compound; locations.md Inland Tower Compound | GM approved: past Barrow Bait & Tackle, short of lake parking; inland two-track; orange survey stake **T-2** by a clay-spoil culvert. Not on the 1984 sheets. Present in the compiled RUN. | yes |
| G19 — Wrong letterhead and absent local agency | ADVENTURE.md; plot.md SP1 Common Knowledge and SP4 Persuasion; secrets.md VSC-05 | Water Authority letterhead; continuity maintenance; no station equipment ID; Ashgrove has no Water Authority. Public works holds the local keys; Rookton Public Works does not own this job. | yes |
| G20 — Eugene callback | plot.md SP1/SP4; secrets.md VSC-05; RUN.md SP4 | GM approved: **(503) 687-4419**; answering service **“Continuity desk. Leave a number.”**; no return call tonight; no Eugene Water Authority listing. Present in the compiled RUN. | yes |
| G21 — Billing PO box | plot.md SP4 Common Knowledge; secrets.md VSC-05; RUN.md SP4 | GM approved: **P.O. Box 2144, Eugene, OR 97401**. Window: cash rental three months ahead, pickup happens; renter's name not released tonight; no operating company in the directory. Present in the compiled RUN. | yes |
| G22 — Key collector | plot.md SP4 Persuasion raise; secrets.md VSC-05; RUN.md SP4 | Cal, not Ray, collected the access key; the clerk/register can establish that. | yes |
| G23 — Signed access and document join | plot.md SP4 Research fail/success; RUN.md Finding the compound | GM approved: evening of session 1, **9:14 p.m.**, **C. Briggs**, key **TWR-2 / lake rd**, vehicle **YEL LANE / WNT 41**; work order site **T-2**. Calendar date remains unset. Present in the compiled RUN. | yes |
| G24 — Added fields on the older form | plot.md SP4 Common Knowledge raise; secrets.md VSC-05 | GM approved: purple spirit-duplicator body; callback and box in black electric type, slightly misaligned, under typed CALLBACK / BILL TO captions not printed on the ditto. Present in the compiled RUN. | yes |
| G25 — Ownership boundary | ADVENTURE.md; secrets.md VSC-05 and GM-only campaign boundary; RUN.md SP4/SP6 | No local record or crew statement identifies the remote employer, consortium, ClearWave, or Concordance. Unresolved ownership is an explicit information boundary, not a missing promised revelation. | yes |
| G26 — Frank's location and initial condition | ADVENTURE.md; plot.md SP5; locations.md Inland Tower Compound | Dead, wrapped, in the outbuilding set back from the tower. On an unalerted arrival he is not loaded; the truck is empty and all evidence categories remain. | yes |
| G27 — Murder evidence and injuries | ADVENTURE.md, Predetermined truths; plot.md SP5; secrets.md VSC-04; locations.md Inland Tower Compound | Cal blocked Frank's exit and struck his head with a heavy work flashlight when Frank tried to push past. Cal did not get help. Frank's visible head injury and blood on his collar challenge drowning; that evidence does not alone identify Cal. Ray witnessed the aftermath, not the blow. | yes |
| G28 — Staging materials, footwear, and truck residue | ADVENTURE.md, Predetermined truths; plot.md SP5 and Revelation audit; secrets.md VSC-04; RUN.md SP5 | GM approved: Frank's boots dry in the outbuilding; Ray's work boots in the truck (gray lake silt in treads, orange-red clay on uppers); truck bed silt, wet rope, lake-water bucket. Visual media comparison, not a session-1 print match. Present in the compiled RUN. | yes |
| G29 — Ray's narrow account | secrets.md VSC-04; npcs/ray-holtz.md; plot.md Dynamic forces | Ray knows Cal killed Frank, helped stage the lake afterward, understands the technical job, and fears taking the murder blame. Cooperation depends on his circumstances; no roll guarantees a confession or employer identity. | yes |
| G30 — Capture/replay record | ADVENTURE.md; secrets.md VSC-01; plot.md SP2/SP5; encounters.md | Local police traffic, including Lilly's name, was captured and replayed. The rack/original record and matching recordings support that local mechanism. Specific frequencies or equipment models are not promised by these results. | yes |
| G31 — Independently timed machine state | plot.md SP5 Electronics raise; encounters.md At-hand environment; RUN.md SP5 | GM approved: alignment generator elapsed-time display, zeroed at last night's isolate/capture start, showing **0:01:52**. If cleanup is active, the raise catches it before rack power is killed. Present in the compiled RUN. | yes |
| G32 — Discovered escape line and cable hazard | plot.md SP5 Notice raise; RUN.md SP5; locations.md/encounters.md compound | GM approved: Ray's on-foot exit is a **cut flap in the chain-link on the timber side of the shed**, opposite the gate. Live hazard is an **orange generator feeder** across the shed doorway to the rack. Present in the compiled RUN. | yes |
| G33 — Observable alert/cleanup states | plot.md SP5; locations.md Inland Tower Compound; encounters.md Compound states | Unalerted: closed gate, empty parked truck, cold fire, intact evidence. Warning/detection starts cleanup without immediate loss; subsequent steps threaten log, signal record, body/truck, then escape. Outcomes depend on intervention. | yes |
| G34 — Which originals/copies survive | plot.md SP1/SP5/SP6; encounters.md; RUN.md Evidence categories | Player choice and resolved events determine custody and loss. Evidence already protected stays protected; one failure does not erase every independent category. A predetermined list of surviving items would override play. | yes |
| G35 — Official disposition and preservation holds | plot.md SP6; RUN.md SP6/End states | Existing outcomes specify contested wording, reopening as suspicious death/homicide, and holds on station, dispatch, work-order/key-register originals. Which applies depends on evidence and play; no absent conspiracy proof is added. | yes |
| G36 — Helen's relationship and habit testimony | npcs/helen-loman.md; characters.md; RUN.md SP3 | Helen Loman is Frank's sister, distinct from Helen Broome. She says he removed boots at home and would not voluntarily walk cold mud barefoot. She cannot testify to his unseen confrontation. | yes |

### Repair priorities

All listed grounding gaps now have GM-approved values in the modular sources and the compiled [RUN.md](RUN.md). The SP1 discrepancy is repaired: Notice locates the cut at counters 0418/0419, while independent clocks in SP2 establish the exact 9:14:00–9:15:52 interval. Final print verification remains the release step.

## Ranked checklist

| Rank | Requirement | Weight | Score (0–5) | Weighted | What good looks like | Notes |
|---:|---|---:|---:|---:|---|---|
| 1 | Clear objective and stakes | ×4 | 5 | 20 | Players quickly understand objective, stakes, and failure. | Opening custody crisis and mission are immediate; cleanup costs are explicit. |
| 2 | Player agency | ×4 | 5 | 20 | Multiple viable approaches change later events. | Custody, copying, tailing, records, witnesses, paperwork, direct approach, and evidence priorities all alter state. |
| 3 | Strong pacing and escalation | ×3 | 4 | 12 | Situation changes rather than repeating. | Fresh memory and a state-based cleanup clock work; unalerted play earns a full-evidence observation beat, while alert triggers the single reversal. Investigative pacing still depends on GM enforcing time costs. |
| 4 | Memorable climax | ×3 | 5 | 15 | Opposition, environment, urgency, and secondary objective. | Compound has body, live record, truck, wet structure, two exits, and sequential loss. |
| 5 | Savage Worlds variety | ×2 | 3 | 6 | Appropriate mix without forced subsystems. | Ordinary tests, optional Tailing/Hitting the Books, social work, and one combat; deliberately restrained for solo noir. |
| 6 | Useful opposition | ×2 | 4 | 8 | Extras provide fitting action and scale. | Two distinct Extras with escape/destruction goals; no inflated enemy Wild Card. |
| 7 | Failure moves the story forward | ×2 | 5 | 10 | Failure changes cost, danger, or opportunity. | Every point names time/evidence/heat/relationship costs and fallback vectors. |
| 8 | Player-character relevance | ×2 | 4 | 8 | Sheet and background have opportunities to matter. | Lilly's police role and investigative/technical Edges matter; one-PC format limits party contrast. |
| 9 | Strong locations and imagery | ×1 | 4 | 4 | Recognizable interactive situations and player-facing Mood. | Re-audited after Ashgrove geography lock. SP3 now uses Daisy’s and West End Fuel; SP4 is Town Hall public works; KCRK and the inland compound are distinct sites. Three Feel clauses remain figurative, so this rank stays 4. |
| 10 | Clean ending and rewards | ×1 | 5 | 5 | Consequences and complete closure are clear. | Five evidence-defined endings answer Frank's case; night 3 remains unrelated. |

**Total (sum of Weighted):** 108/120

## Warning signs

- [ ] One failed Notice, Persuasion, or Research roll can stop the story.
- [ ] Most situations can be summarized as “enter room, fight enemies.”
- [ ] The plot only works if players make one specific choice.
- [ ] A named NPC, secret, or likely fight appears without quoted lines, a GM Note, or at-hand stats beside that situation.

## One-shot shape

- [x] Targets 3–5 hours with a 3–4 hour core.
- [x] Supplied-PC hook engages the premise at once.
- [x] Opening trouble within the first 10–15 minutes.
- [x] Six substantial flexible situations, with three investigative points compressible into two.
- [x] One twist or major complication.
- [x] One large climax.
- [x] Minimal lore and no essential side quests.
- [x] Complete ending even if further adventures are possible.

## Short campaign shape

Not applicable.

## Long campaign

Not applicable.

## Repair log

| Rank or warning | Problem | Repair | Done |
|---|---|---|---|
| Pacing | Parallel investigation could sprawl beyond five hours. | Defined time costs and a 3–4 hour compression that folds paperwork into the records/town route. | yes |
| Opposition | Solo combat could become too volatile. | Kept both opponents as lightly equipped Extras with escape/destruction goals; Ray may be absent or surrender. | yes |
| Geography vs town lore | Generic diner/fuel/Water Authority could fight Sheet 2 (KCRK south of the river; Daisy’s; West End Fuel; no Water Authority building). | Locked the inland compound off the lake road; named Daisy’s and West End Fuel; moved the clerk to Town Hall public works; kept Water Authority as inapt letterhead. | yes |
