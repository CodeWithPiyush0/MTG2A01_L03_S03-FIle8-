# MTG2A01_L03_S03 — SME review 1 → build 2

Source: `MTG2A01_L03_S03_review.pptx` (18 slides; deck pages = the "Page N" labels on them).
The flow, layout, buttons, animation, colours and type are File7's (`../MTG2A01_L04_S02 (File7 Maths)`) — the
first draft (another engine) is kept in `_archive_v1/`.

Decisions taken with the user before the build (2026-10-28):
- Deck slide 9 is a second "Page 6": it is a **new guided page** (42 + 35) after the 34 + 25 page.
- Names are the deck's (आकाश, मोनी, बीबी, जॉनी); the art is the existing portraits
  (Madhav → Akash, Aanya → Moni, Aaru → Johny, Pari → Bibi).
- Game: Swiftee is the third character — she hands the built blocks to Bibi / Johny, then leads the total.
- Game: all 4 activities, in the garden look of the deck's reference (garden background generated, wooden board).

Status: ✅ DONE · ⚑ FLAGGED-BACK · ⏳ PENDING · N/C (nothing asked)

| # | Deck slide · page | Change (deck's words) | Status | Proof |
|---|---|---|---|---|
| 1 | s2 · overview | Developer's own notes / open questions | N/C | (answered by the deck itself: ghosts stay — "leaving a greyed-out image behind"; title is now "संख्याओं का जोड़") |
| 2 | s3 · p1 landing | Text: संख्याओं का जोड़। | ✅ DONE | cover: wall title `संख्याओं का जोड़` (card title.hi) — capture landing |
| 3 | s3 · p1 | 23 + 14 = ? (mockup: 23 / + 14 / ? written one under the other on the cover) | ✅ DONE | Akash/Moni with their 23 / 14 blocks; 23, + 14, line + ? appear on «आज हम / संख्याओं / जोड़ना» (landing_hero.beats) — capture at 4 s / 10 s |
| 4 | s3 · p1 | VO: नमस्ते दोस्त! मैं हूँ स्विफ्टी! आज हम संख्याओं को जोड़ना सीखेंगे। | ✅ DONE | vo_landing (transcribed back: नमस्ते दोस्त, मैं हूं स्विफ्टी। आज हम संख्याओं को जोड़ना सीखेंगे।) |
| 5 | s4 · p2 | Replace the slide. Heading: कुल कितने ब्लॉक्स? | ✅ DONE | T1 prompt_hi — capture |
| 6 | s4 · p2 | Visuals: Akash and Moni with blocks and number of blocks (23, + 14 one under the other) | ✅ DONE | STORY_ADD ask: portraits + names, 2 rods 3 cubes / 1 rod 4 cubes, 23 / + 14 / line — capture |
| 7 | s4 · p2 | VO: आकाश और मोनी ब्लॉक्स से खेल रहे है, … दोनों के पास मिलाकर कुल कितने ब्लॉक्स हैं? — everything appears in sync with the VO | ✅ DONE | portraits on their names, blocks on «ये सारे», 23 on «23», + 14 on «14», line on «कुल» (card cues); spelling है→हैं |
| 8 | s5 · p3 | Heading text + VO: आइए, 23 और 14 को जोड़ते हैं। | ✅ DONE | T2 prompt_hi + vo_t2_head |
| 9 | s5 · p3 | VO1 सबसे पहले ब्लॉक्स की सहायता से दोनों संख्याएँ बनाते हैं। | ✅ DONE | vo_t2_intro |
| 10 | s5 · p3 | VO2 23 में 2 दहाई और 3 इकाई हैं। [Tap on the first row, the table appears and then the card; its tens and ones digits highlight in sync] | ✅ DONE | Swiftee's hand taps row 1 → the table + 23 card come in; digits lit on «2 दहाई» / «3 इकाई» — play-through |
| 11 | s5 · p3 | VO3 पहले 2 दहाई के लिए 2 बंडल रखते हैं। [Source buttons appear below; Swiftee adds 2 rods by tapping the tens +] | ✅ DONE | source box under the table; Swiftee taps the tens + twice — play-through |
| 12 | s5 · p3 | VO4 अब 3 इकाई के लिए 3 ब्लॉक रखते हैं। [Swiftee adds 3 blocks with the ones +] | ✅ DONE | Swiftee taps the ones + three times — play-through |
| 13 | s5 · p3 | VO5 इसी तरह, 14 में 1 दहाई और 4 इकाई हैं। [row + card appear; digits highlight in sync] | ✅ DONE | row 2 + «+ 14» come in, digits lit in sync — capture 24 s |
| 14 | s5 · p3 | VO6 अब आप ब्लॉक्स की सहायता से 14 बनाइए। [Tens + pulses, off after 1 tap; then Ones + pulses, off after 4; idle → pulse again] | ✅ DONE | childBuild: tens + pulses, off at 1; ones + pulses, off at 4; idle 7 s → pulse + «अब दहाई/इकाई बनाइए।» (File7) |
| 15 | s5 · p3 | VO7 बहुत बढ़िया! अब दोनों संख्याओं को जोड़ते हैं। [source buttons go; the sum row shows] | ✅ DONE | sources fade, the sum row + line + ? show — capture 42 s |
| 16 | s5 · p3 | VO8 पहले इकाइयों को जोड़ते हैं। [tens disabled; ones pulse till all tapped; each moves to the sum, a grey copy stays] | ✅ DONE | moveKind: rods dimmed, cubes pulse, each tap flies down, grey copy stays — capture 42 s |
| 17 | s5 · p3 | VO9 3 इकाई और 4 इकाई मिलाकर हुई, 7 इकाई। [sum's cubes highlight in sync] | ✅ DONE | sum cubes from row 1 beat on «3 इकाई», row 2's on «4 इकाई», all + head on «7 इकाई» |
| 18 | s5 · p3 | VO10 अब दहाइयों को जोड़ते हैं। [rods pulse till all tapped; each moves, a grey copy stays] | ✅ DONE | moveKind(t) — capture 90 s (grey rods left) |
| 19 | s5 · p3 | VO11 2 दहाई और 1 दहाई मिलाकर हुई, 3 दहाई। [sum's rods highlight in sync] | ✅ DONE | same, rods |
| 20 | s5 · p3 | VO12 अब हमारे पास कुल 3 दहाइयाँ और 7 इकाइयाँ हैं, यानी 37 [rods, cubes, digits and 37 highlight in sync] | ✅ DONE | rods + tens digit on «3 दहाइयाँ» (card fills), cubes + ones digit on «7 इकाइयाँ», the 37 on «37» |
| 21 | s5 · p3 | Completion VO: इसलिए, 23 और 14 को जोड़ने पर 37 मिलता है। | ✅ DONE | vo_t2_done — 23, 14, 37 cards beat in sync; confetti; → button |
| 22 | s6 · p4 | Replace the slide. Heading कुल कितने ब्लॉक्स?; Akash and Moni with their blocks; 23 / 14 / + / 37 one under the other; VO1 23 जोड़ 14 बराबर 37; VO2 आकाश और मोनी के पास कुल मिलाकर 37 ब्लॉकस है। — in sync | ✅ DONE | STORY_ADD sum: grey originals, 37 pile, 23 / + 14 / 37 — capture 12 s; «ब्लॉकस है» → «ब्लॉक्स हैं» |
| 23 | s7 · p5 | delete | ✅ DONE | no slide (lessons.py) |
| 24 | s8 · p6 (G1) | Use the same place-value table. Text: संख्याएँ जोड़िए। | ✅ DONE | PV_ADD build, header «संख्याएँ जोड़िए।», same stacked table — capture |
| 25 | s8 · p6 | VO1 पहले ब्लॉक्स की सहायता से दोनों संख्याएँ बनाते हैं। | ✅ DONE | vo_g1_intro |
| 26 | s8 · p6 | VO2 34 में 3 दहाई और 4 इकाई हैं। ब्लॉक्स की सहायता से 34 बनाइए। [Auto tap the first row. Tens + pulses till 3 taps then off; then Ones + till 4 then off] | ✅ DONE | hand taps row 1 (row lights), sources, childBuild 3 / 4 — capture 16 s |
| 27 | s8 · p6 | VO3 25 में 2 दहाई और 5 इकाई हैं। ब्लॉक्स की सहायता से 25 बनाइए। [same, second row, 2 / 5] | ✅ DONE | same, row 2 (2 / 5) |
| 28 | s8 · p6 | VO4 बहुत बढ़िया! अब दोनों संख्याओं को जोड़ते हैं। | ✅ DONE | vo_g1_go |
| 29 | s8 · p6 | VO5 पहले इकाइयों को जोड़ते हैं। [ones of both rows pulse, tens disabled; each tapped cube moves to the sum row] | ✅ DONE | moveKind(o) from both rows, tens dimmed |
| 30 | s8 · p6 | VO6 4 इकाई और 5 इकाई मिलाकर हुईं, 9 इकाई। | ✅ DONE | pvAddSumLine(o) |
| 31 | s8 · p6 | VO7 अब दहाइयों को जोड़ते हैं। [rods of both rows pulse; each tapped rod moves to the sum's tens] | ✅ DONE | moveKind(t) |
| 32 | s8 · p6 | VO8 3 दहाई और 2 दहाई मिलाकर हुईं, 5 दहाई। [sum's rods highlight in sync] | ✅ DONE | pvAddSumLine(t) |
| 33 | s8 · p6 | VO9 अब हमारे पास कुल 5 दहाइयाँ और 9 इकाइयाँ हैं, यानी 59 [rods, cubes, digits, 59 highlight in sync] | ✅ DONE | pvAddTotal — capture 60 s (59) |
| 34 | s8 · p6 | Completion VO: शाबाश! 34 और 25 को जोड़ने पर 52 मिलता है। | ⚑ | the deck's 52 is a slip (34 + 25 = 59, as its own VO9 says) — built with **59** |
| 35 | s9 · p6b (G2, new) | Title 1 संख्याएँ जोड़िए।; 42 + 35 = ?; the PV tables with the numbers built with blocks one by one | ✅ DONE | G2 (new page): rows built block by block with their cards — capture 5 s |
| 36 | s9 · p6b | VO1 42 और 35 को जोड़िए। [ones tappable first, then tens; each tapped block moves to the sum; idle 7 s → blocks pulse] | ✅ DONE | vo_g2_prompt; ones first (tens dimmed), then tens; idle 7 s pulse (tapAcross) |
| 37 | s9 · p6b | Title 2 सही जोड़ चुनिए।; VO2 बहुत बढ़िया! अब सही जोड़ चुनिए। [the sum table moves to the centre replacing the first two; the options show] | ✅ DONE | header → «सही जोड़ चुनिए।»; vo_ask_pick2; soloSum: the sum row to the middle, rows 1–2 go; cards under it — capture 14 s |
| 38 | s9 · p6b | Options 77 / 76 / 14; Correct: शाबाश! 42 और 35 का जोड़ 77 है। [the right option moves into the "?"] | ✅ DONE | options 77 / 76 / 14 (shuffled); right card flies into the ? ; vo_g2_correct (first try) / _late |
| 39 | s9 · p6b | WA1 wiggle + ब्लॉक्स को गिनिए और सही जोड़ चुनिए। · WA2 wiggle + ध्यान से देखिए, कुल 7 दहाइयाँ और 7 इकाइयाँ हैं। [blocks highlight in sync] · WA3 wiggle + the right option lit, the others faded | ✅ DONE | wrong card shakes (wiggle); WA1 vo_h1_pick; WA2 vo_g2_h2 + tens/ones beat in sync; WA3 right lit, others faded (no VO — none in the deck) |
| 40 | s10 · p7 (G3) | Same as #35–39 with 56 + 33; options 98 / 89 / 17; correct शाबाश! 56 और 33 का जोड़ 89 है।; WA2 कुल 8 दहाइयाँ और 9 इकाइयाँ | ✅ DONE | G3 — same module, 56 + 33 |
| 41 | s11 · p8 (G4) | Title 1 संख्याएँ जोड़िए।; 47 + 21 = ?; tables built one by one; Title 2 सही जोड़ टाइप करिए। | ✅ DONE | G4 header «संख्याएँ जोड़िए।» → «सही जोड़ टाइप करिए।» — capture 16 s |
| 42 | s11 · p8 | VO 47 और 21 को जोड़िए और सही जोड़ टाइप करिए। [tap the ones and tens blocks to add; then an answer counter below with a hand nudge; on tap, the number pad] | ✅ DONE | answer box under the table with the hand; keypad on tap — capture 16 s |
| 43 | s11 · p8 | Correct: शाबाश! 47 और 21 का जोड़ 68 है। [the typed answer moves into the "?"] · WA1 ब्लॉक्स को गिनिए और सही जोड़ टाइप करिए। · WA2 ध्यान से देखिए, कुल 6 दहाइयाँ और 8 इकाइयाँ हैं। · WA3 the right digit keys light in sequence | ✅ DONE | flyAnsToQ into ?; WA1 vo_h1_type; WA2 vo_g4_h2; WA3 guideKeys |
| 44 | s12 · p9 (P1) | संख्याएँ जोड़िए और सही जोड़ चुनिए।; 61 + 20 = ? (61 / + 20 / ? one under the other); options 80 / 18 / 81; VO सही जोड़ चुनिए।; correct शाबाश! 61 और 20 का जोड़ 81 है। | ✅ DONE | MENTAL_ADD mcq, 61 / + 20 / ? (vertical, as the mockup) — capture 4 s |
| 45 | s12 · p9 | WA1 ध्यान से देखिए— 1 इकाई और 0 इकाई; 6 दहाई और 2 दहाई। अब सही जोड़ चुनिए। [digits highlight in sync] · WA2 61 and 20 in blocks on separate tables + ब्लॉक्स को गिनिए और सही जोड़ चुनिए। · WA3 the blocks move to a third table (options hidden meanwhile); the first two rows go; the options again below, only the right one lit | ✅ DONE | WA1 ones digits then tens lit in sync; WA2 stacked table rows 1–2 + cards glide beside — capture; WA3 autoMove → soloSum → options back, only right lit — capture 24 s |
| 46 | s13 · p10 (P2) | संख्याएँ जोड़िए और सही जोड़ टाइप करिए।; 76 + 22 = ?; VO 76 और 22 को जोड़िए और सही जोड़ टाइप करिए। [idle 7 s → hand nudge on the box]; VO सही जोड़ टाइप करिए।; correct शाबाश! 76 और 22 का जोड़ 98 है। | ✅ DONE | MENTAL_ADD numpad: type into the ?; idle 7 s → hand on it + «सही जोड़ टाइप करिए।» |
| 47 | s13 · p10 | WA1 ध्यान से देखिए— 6 इकाई और 2 इकाई; 7 दहाई और 2 दहाई। अब सही जोड़ टाइप करिए। · WA2 76 and 22 in blocks on separate tables + ब्लॉक्स को गिनिए और सही जोड़ टाइप करिए। · WA3 the right digit keys light in sequence | ✅ DONE | WA1 digits — capture 14 s; WA2 blocks — capture 22 s; WA3 guideKeys |
| 48 | s14 · p11 (P3) | Same as #46–47 with 37 + 60 → 97 | ✅ DONE | P3 37 + 60 → 97 — capture |
| 49 | s15 · p12 | Delete | ✅ DONE | no slide |
| 50 | s16 · p13 | Delete | ✅ DONE | no slide |
| 51 | s17 · game | Bibi & Johny – ब्लॉक्स की एक्टिविटी: VO1 intro, the two with their block requirements, the child taps play | ✅ DONE | intro: banner, wishes «मुझे 25 ब्लॉक्स चाहिए।», Swiftee + the pile, play button — capture |
| 52 | s17 · game | VO2 पहले बीबी के लिए 2 दहाई और 5 इकाई बनाइए। — the child uses + / − for 2 rods and 5 cubes, taps Check; VO3 शाबाश! बीबी के 25 ब्लॉक्स तैयार हैं। — the blocks highlight, Bibi is replaced by Johny | ✅ DONE | build screen: Bibi + badge, wooden board, − n + ×2, जाँचें — capture 19 s; right → blocks light, VO3 |
| 53 | s17 · game | VO4 / VO5 the same for Johny (1 दहाई, 2 इकाई) | ✅ DONE | same for Johny (activity loop) |
| 54 | s17 · game | VO6 अब दोनों के ब्लॉक्स को जोड़ते है। पहले इकाई जोड़िए। — Bibi's 25 in row 1, Johny's 12 in row 2, row 3 empty, the ones column lit; VO7 5 इकाई और 2 इकाई जोड़िए। — the child adds 7 cubes in row 3; VO8 शाबाश! अब दहाइयाँ जोड़िए। — 3 rods; VO9 बहुत बढ़िया! 3 दहाई और 7 इकाई, यानी 37 ब्लॉक्स। — 25 + 12 = 37 appears | ✅ DONE | 3-row board (बीबी / + जॉनी / कुल), ones column lit, ones − n + only, then tens; «= 37» joins «25 + 12» — capture 64 s |
| 55 | s17 · game | VO10 वाह! … पहली एक्टिविटी पूरी हो गई! — success animation, अगली एक्टिविटी button; VO11 अब अगली एक्टिविटी शुरू करें! | ✅ DONE | confetti, hops, VO10 (पहली…चौथी), अगली एक्टिविटी → VO11 |
| 56 | s17 · game | Activities: 25+12=37, 13+55=68, 31+45=76, 42+46=88 | ✅ DONE | data.acts = 25+12, 13+55, 31+45, 42+46 (lessons.py asserts no regrouping) — all 4 played through |
| 57 | s17 · game | Common feedback: 1st wrong फिर से कोशिश कीजिए। (retry) · 2nd ब्लॉक्स ध्यान से गिनिए। (the relevant blocks light) · 3rd देखिए, सही ब्लॉक्स ये हैं। (the right blocks shown) | ✅ DONE | 1st w1 retry; 2nd w2 + the blocks to count light; 3rd w3 + counters set right by themselves |
| 58 | s17 · game | VO15 शाबाश! आपने बीबी और जॉनी की सभी एक्टिविटी पूरी कर दीं! — both celebrate | ✅ DONE | after activity 4: both kids + Swiftee, confetti, vo_gm_final → celebration |
| 59 | s17 · game (note) | Dono enable honge (tens and ones) — both + / − pairs live at once | ✅ DONE | build screens: both − n + live at once |
| 60 | s17 · game (note) | Include third character, swiftee: distribute and then total | ✅ DONE | Swiftee on screen throughout: hands each child their blocks (they fly into the badge), then glows and leads the total |
| 61 | s18 · p14 | FINISH — 'शाबाश! … याद रखिए — जोड़ हमेशा इकाई से शुरू होता है।' (the draft's own line, no change asked) | N/C | |

## Changed beyond the deck
Each of these is either the user's instruction (build on File7) or a mechanical consequence of a deck row — nothing else.
- **The engine is File7's** (user: "for the flow, layout, buttons, animation, colors, typography … follow my file7"): the
  draft's engine and pages are replaced, not patched; the draft is in `_archive_v1/`. Hence File7's phase screens and
  their lines, its celebration, its 7 s reminders («अब दहाई बनाइए।» while building, the page's own "choose / type" line
  as the re-ask), its answer feedback (wrong = shake; "शाबाश" only for a first-try answer — the `*_late` clips).
- **Hindi slips fixed** in the deck's lines: ब्लॉकस → ब्लॉक्स, खेल रहे है → खेल रहे हैं, 37 ब्लॉकस है → 37 ब्लॉक्स हैं,
  जोड़ते है → जोड़ते हैं; G1's completion 52 → 59 (row 34).
- **Page 2's one VO is said as three clips** (same words) so the pictures can follow it; T1 shows a line under «+ 14»
  (the written sum) but no "?" (the mockup has none).
- **Names** under the portraits (आकाश, मोनी) — the deck's placeholders were name circles.
- **The → button** sits at the right on the three tutorial pages (clear of the table / the written sum).
- **The game**: the deck's script is written for activity 1; activities 2–4 reuse it with their numbers — VO1 becomes
  «अब बीबी को 13 और जॉनी को 55 ब्लॉक्स चाहिए। चलिए, उनकी मदद करें!», VO10 says दूसरी / तीसरी / चौथी. The reference
  picture's English words are in Hindi: «एक्टिविटी 1: ब्लॉक्स बनाइए और जोड़िए», «मुझे 25 ब्लॉक्स चाहिए।», «Check» →
  «जाँचें», «Total» → «कुल». Its LEVEL badge and menu button are left out (no score / level in these lessons). The garden
  background was generated (`assets/game_garden.webp`), the board is drawn in CSS.
- **Art**: four portraits copied under the deck's names (char_akash/moni/johny/bibi*.webp = Madhav/Aanya/Aaru/Pari).
- **Signals**: `pv_block_moved`, `game_check` (new), `pv_merge_done`; ADD_GAME/PV_ADD/MENTAL_ADD send `question_started`.

## Observations — noticed, NOT changed
The game was left exactly as the deck specified on these; for the SME to decide.
1. **The celebration line** still says «…अब आप ऊपर-नीचे लिखकर जोड़ सकते हैं…» while the title is now «संख्याओं का जोड़».
2. **Agreement mixes in the deck's lines**: T2 «मिलाकर हुई, 7 इकाई» vs G1 «मिलाकर हुईं, 9 इकाई»; T2 «3 ब्लॉक रखते हैं» vs
   «ब्लॉक्स» everywhere else.
3. **Register**: all polite आप, but two forms mix — «कोशिश कीजिए» (game) and «टाइप करिए / जोड़िए» elsewhere.
4. **The game is long**: 4 activities × (2 builds + 2 checks of the total) ≈ 5 minutes on its own.
5. **Page 3's start**: the heading line and VO1 play over an empty card (~5 s) — the deck brings the table in only on
   VO2's tap.
6. **Deck slide 9** carries the label "Page 6" (a copy of slide 8's label) — built as a new page, as agreed.
7. **G1** has no answer question (the deck's page 6 ends on its completion line); it still counts as a right page for the
   hidden mastery ratio, as File7's "fill" pages do.
8. **Game VO8** «शाबाश! अब दहाइयाँ जोड़िए।» says शाबाश even when the ones took three tries.

## Ear-check (a human listens before delivery)
All 98 lines are Gemini TTS, voice **Kore** (File7's voice), none needed a retry. Every clip was transcribed back by
Gemini and compared with its script (numbers are said in Hindi: तेईस, चौदह, सैंतीस, उनसठ …). Four takes failed that
check and were re-rendered and re-checked (same text): `vo_gm1_build_a`, `vo_gm3_intro`, `vo_gm4_done` (बीबी came out
close to "Baby") and `vo_p1_correct_late` (इकसठ was slurred). Listen first to those four, and to:
`vo_landing` (the first thing a child hears), `vo_t2_total`, `vo_gm_final`, `vo_cel`.

## Verification
- Full automated play in headless Chrome (real VO, autoplay on), cover → celebration, one wrong answer included:
  reached the celebration, 145 signals, **0 console errors / warnings**. Every `signals_expected` fired: slide_entered,
  slide_completed, pv_build_done, pv_block_moved, mcq_correct, numpad_correct, game_check, mastery_score,
  lesson_completed (+ phase_transition, pv_block_added, pv_merge_done, answer_wrong).
- Each screen captured and read; help ladders exercised to the 3rd step on G2, P1 (cards) and P2 (keypad).
- Taps were simulated by script (element clicks). A human play-through on a tablet is still the final touch test.

## User changes (2026-10-29)
| # | Change | Status | Proof |
|---|---|---|---|
| U1 | The → button placed as in File7 | ✅ DONE | the per-page override is gone: bottom centre on the tutorial pages (File7's CSS). The T2 table was made compact (its bottom at 588, the button's top at ~599) and T3's rows moved up, so nothing sits under it — captures T1, T2 (end), T3 |
| U2 | Page 1: no names of the kids | ✅ DONE | T1 portraits without names (T3 keeps them) — capture T1 |
| U3 | Each page: every digit in its own box (2 3 / + 1 4 / line) | ✅ DONE | the written sum on every page (T1–T3, G1–G4, P1–P3) and the cover; the "?" stays one box and fills as digit boxes; lit digits light their own box — captures cover, T1, T2, T3, G1, P2 |
| U4 | Less space between 23 and 14 | ✅ DONE | T1 / T3: the written sum is one compact block beside the rows (it no longer follows the rows' spacing); the table pages keep each card level with its row — captures T1, T3 |
| U5 | T2 and T3: no heading | ✅ DONE | prompt_hi "" on both; T2's heading line is still spoken (only the text is gone) — captures T2, T3 |
| U6 | Digit boxes closer: gap 0.12em | ✅ DONE | `.pv-num.pv-vc` gap .16em → .12em (every page) |
| U7 | T3: no names of the characters | ✅ DONE | T3 portraits without names — capture T3 |
| U8 | T2: a bigger table | ✅ DONE | blocks 16.5 → 20.5 px wide, rows 118 → 146 px; the table now starts where the heading was and still ends above the → button (586) — captures T2 at 24 s / end |
| U9 | T2: the table a little smaller | ✅ DONE | blocks 20.5 → 19 px, rows 146 → 136 px; it now sits a little lower with more room above it and above the → button — capture T2 end |
| U10 | T2: the table starts in the centre and moves up as each row is added below | ✅ DONE | `vtable.moveBy`; T2 keeps the table centred: row 1 in the middle, it glides up half a row as row 2, then the sum row come in; the written sum and the + buttons move with it (the + buttons stay under the table) — captures T2 at 14 / 25 / 36 / 86 s |
| U11 | T1: on "दोनों मिलाकर" the "+" appears; two empty "?" boxes under the numbers | ✅ DONE | 14 comes in alone; the "ask" line: "+" on "दोनों", the line and the two dashed "?" boxes (tens, ones) on "मिलाकर" (cues measured from the clip) — capture T1 17 s |
| U12 | T2: no hand before the table is shown | ✅ DONE | the hand's tap on the empty first row is gone; the table comes in by itself, then 23 (the hand still does Swiftee's + taps on the shown table) |
| U13 | T2: tens rods a little shorter (touching the row border) | ✅ DONE | `vtable`: a rod is at most 82% of its row (tutorial 128 → 112 px, main 121 → 112 px); the table width is unchanged — every stacked table |
| U14 | No "+" left of the table; only the written sum's "+" (left of the second number) | ✅ DONE | `vtable` has no "+" (its line spans only the table) — T2, G1–G4, P1–P3 help |
| U15 | The written sum's "+" only when the VO says to add | ✅ DONE | T2 / G1: on "दोनों" of "अब दोनों संख्याओं को जोड़ते हैं।" (T2: the sum row with the "?" boxes on "जोड़ते"); G2–G4 (no such line): on "जोड़िए" of "42 और 35 को जोड़िए।"; P1–P3 (the sum is the question, no table) keep it from the start |
| U16 | Two empty "?" boxes under the numbers; each digit goes in as the VO says it | ✅ DONE | `vcards`: the answer is two "?" boxes (tens, ones) on every page and on the cover; T2 / G1: the ones digit goes in on "…मिलाकर हुई, 7 इकाई", the tens digit on "…3 दहाई"; T3 fills on "37"; MCQ answers fly into both; P2 / P3 type into the boxes one digit each (blue caret box) — captures T2 42–48 s, G1 40 s, P2 6–11 s |
| U17 | T3: the kids' pictures and their blocks bigger | ✅ DONE | portraits 100 → 130 px, blocks 108 → 138 px tall, rows spread (190 / 345 / 500); the pile clears the → button — capture T3 11 s |

## The game — updated deck "file6 ppt.pdf" page 17 (2026-10-29)
| # | Deck / user | Status | How |
|---|---|---|---|
| G1 | New characters (the old ones are used in earlier files): Rumi & Rohan | ✅ DONE | new Gemini art in the lesson's style (`tools/gen_image.py`, cut with `make_poses.py` / `make_portrait.py`): `char_rumi*`, `char_rohan*` — standing, cheering, round portrait, each with its blink copy. Bibi / Johny art and VO moved to `_archive_v1/game_bibi_johny/` |
| G2 | The deck's VO lines | ✅ DONE | screen 1 "रूमी को 25 और रोहन को 12 ब्लॉक्स मिले हैं।"; "पहले रूमी के लिए 2 दहाई और 5 इकाई बनाइए।"; "शाबाश! अब रोहन के लिए 1 दहाई और 2 इकाई बनाइए।"; "अब दोनों के ब्लॉक्स जोड़ते हैं।"; "पहले इकाइयाँ जोड़िए।"; "शाबाश! 25 और 12 जोड़ने पर 37 मिले।". ⚠ The PDF page is cut off at its right edge: the endings of "पहले रूमी…", "…अब रोहन के लि…", "अब दोनों के ब्लॉक्स जो…" and "…and the …" were completed in the deck's own pattern — please confirm. All 24 new clips transcribed back by Gemini |
| G3 | Background not cluttered | ✅ DONE | `assets/game_meadow.webp` (Gemini): a plain pastel lawn and sky, empty middle — replaces `game_garden.webp` |
| G4 | No Swiftee in the game | ✅ DONE | removed (the VO is the narrator) |
| G5 | Screen 1: Rumi and Rohan appear in the garden | ✅ DONE | the two standing; each hops and their number badge comes as the VO names them |
| G6 | Screen 2: empty दहाई–इकाई table; + / −; जाँचें; right → blocks highlight, the table resets, Rohan's turn | ✅ DONE | on "अब" of "शाबाश! अब रोहन के लिए…" the board empties and Rohan takes Rumi's place |
| G7 | WA1 "फिर से करिए।" + the − / + pulse "according to the blocks" | ✅ DONE | the button that helps (+ if too few, − if too many) pulses. The line is "चलिए, फिर से करिए।" — on its own "फिर से करिए।" was spoken as "कहिए" in 5 takes |
| G8 | WA2 "इसमें दहाई / इकाई ज़्यादा / कम है।" + only that button active until the number is right | ✅ DONE | column by column (tens first); the other buttons are greyed until it is right |
| G9 | Three-row table: Row 1 Rumi, Row 2 Rohan, Row 3 empty, + beside Row 2; ones first, then tens | ✅ DONE | portraits + names in the first column; the ones column lit with "पहले इकाइयाँ जोड़िए।" — a tap on the tens buttons says it again and the ones buttons pulse; then "शाबाश! अब दहाइयाँ जोड़िए।"; each step checked with जाँचें (kept from the build screens — the deck names no check here) |
| G10 | "शाबाश! 25 और 12 जोड़ने पर 37 मिले।" | ✅ DONE | कुल (37), "25 + 12 = 37", confetti, the two hop; then अगली एक्टिविटी (4 activities, the earlier deck's sums); the end: both cheer — "शाबाश! आपने रूमी और रोहन की सभी एक्टिविटी पूरी कर दीं!" |
| G11 | (not in the deck) the old "5 इकाई और 2 इकाई जोड़िए।" / "3 दहाई और 7 इकाई, यानी 37" / "वाह!…" lines and the play button | ✅ REMOVED | the deck's new script has none of them |
Verified: the game played through 4 activities to the celebration (one wrong check each step; WA2 path forced separately), 0 console errors.

## Review round — 2026-10-29 (pages + game)
| # | User | Status | How |
|---|---|---|---|
| R1 | Page 1: the sum's horizontal line goes out of the table | ✅ DONE | `vtable`: the line between row 2 and the sum row now runs inside the table's border (was 8 px over each side) — every stacked table |
| R2 | Remove the hand nudge on the table | ✅ DONE | G1: the row lights by itself — no hand tapping it |
| R3 | P1, after the 2nd wrong answer: the written sum a little right; its answer boxes were hidden behind the options | ✅ DONE | the sum 50 px further right of the table; the three cards come under the answer boxes (were over them) |
| R4 | P2 / P3: the tens box was active first — addition starts from the ones; the keypad nearer the sum | ✅ DONE | the cursor starts in the ones box: the 1st key goes into the ones, the 2nd into the tens (the 3rd help lights the ones key first too); the sum and keypad sit together near the middle (the keypad moves back right when the help's table comes in) |
| R5 | Game start: both kids standing, the blocks on a table (not on one another); the camera turns to look from the top and the table becomes the blocks' table | ✅ DONE | screen 1: Rumi and Rohan behind a wooden table, each one's rods and cubes lying side by side in front of them; after the VO the kids and the table's legs slide out at the bottom while its top turns to face the camera and becomes the दहाई–इकाई board |
| R6 | After one kid's blocks, the kid walks off to the left and the next one comes | ✅ DONE | Rumi walks in; on "अब" she walks off to the left and Rohan walks in |
| R7 | A wrong check: the wrong blocks wiggle, not the check button | ✅ DONE | the wrong column's blocks wiggle (its number, when it has no blocks) |
| R8 | The board a little higher (little space between the buttons and it) | ✅ DONE | board 96 → 56 px from the top, 470 → 450 px tall; the − / + under it with a gap, जाँचें below them |
| R9 | White bars left and right — fill them with the background | ✅ DONE | the lawn is the stage's own backdrop for the game (`data.bg = "meadow"`), so the side bands carry it on |
| R10 | Error hint only for the column that is wrong | ✅ DONE | 1st wrong: only the wrong column's line ("इसमें इकाई कम है।" …) and its helping button pulses; 2nd: only that button works until it is right. The generic "चलिए, फिर से करिए।" is gone (clip in `_archive_v1/game_retry/`) |
| R11 | The adding board: no names, just the picture and the number | ✅ DONE | each row: the kid's round picture and the number |
| R12 | The sum shown in the box below | ✅ DONE | the sum row has two "?" boxes (tens, ones): the ones digit goes in when the ones are added, the tens digit when the tens are |
| R13 | Adding: no + / − buttons — tap a block and it goes into the sum row | ✅ DONE | the ones pulse; each tapped block glides down into the sum row, leaving a grey copy; a tens block tapped first: "पहले इकाइयाँ जोड़िए।"; then the tens — no check button |
| R14 | No button to move to the next activity | ✅ DONE | after "शाबाश! 25 और 12 जोड़ने पर 37 मिले।", "अब अगली एक्टिविटी शुरू करें!" and the next one starts by itself |
| R15 | A submenu for the game's parts (testing one part without playing the whole game) | ✅ DONE | `?dev=1`: a second list "खेल · भाग चुनें…" — any activity's table / Rumi's blocks / Rohan's blocks / adding, or the last screen (also `?slide=10&gm=2.total`) |
Verified: the whole game played through (one wrong check per build step) to the celebration, 0 console errors; ones-only wrong checks say only the ones line; P3 three wrong answers → the keys light 7 then 9; P1 cards under the answer boxes (measured); the submenu jumps to activity 2's adding, the last screen and activity 3's Rohan.

## The game — the user's updated review deck (MTG2A01_L03_S03_review.pptx, page 17, 2026-10-30)
Slides 1–16 of this deck are unchanged; page 17 now carries the full game script with a 4-question summary. The deck replaced the project copy of `MTG2A01_L03_S03_review.pptx`.
| # | Deck | Status | How |
|---|---|---|---|
| D1 | Questions: 25 + 12, 34 + 25 (make and add blocks); 41 + 30, 62 + 17 (direct vertical addition + keypad) | ✅ DONE | `ACTS` / `MODES` in `tools/lessons.py` (were 25+12, 13+55, 31+45, 42+46, all blocks) |
| D2 | Q1 lines: "रूमी को 25 और रोहन को 12 ब्लॉक्स मिले हैं। पहले रूमी के लिए 25 बनाइए।", "शाबाश! अब रोहन के लिए 12 बनाइए।", "अब दोनों के ब्लॉक्स जोड़िए। पहले इकाइयाँ जोड़िए।", "शाबाश! 25 और 12 जोड़ने पर 37 मिले।" | ✅ DONE | new clips `vo_gm1_make_a2`, `vo_gm1_make_b2`, `vo_gm_add3` (+ the existing "पहले इकाइयाँ जोड़िए।") |
| D3 | Q2: "रूमी को 34 और रोहन को 25 ब्लॉक्स मिले हैं। दोनों संख्याएँ बनाइए।" — both made, the same hints; "अब दोनों के ब्लॉक्स जोड़िए।"; the child combines the blocks, enters 9 in the ones and 5 in the tens, Check; "बहुत बढ़िया! 34 और 25 जोड़ने पर 59 मिले।" | ✅ DONE | no other lines on Q2 (as the deck): the blocks pulse; after combining, the keypad opens beside the board and the sum's two boxes fill ones first; wrong: "फिर से लिखिए।" (2nd: the sum row's blocks counted again; 3rd: only the right key) |
| D4 | Q3/Q4 "Add Vertically": no blocks, two blank boxes, tap → keypad; "अब बिना ब्लॉक्स के जोड़िए। 41 और 30 को जोड़कर सही उत्तर टाइप करिए।" / "अब 62 और 17 को जोड़िए। सही उत्तर टाइप करिए।" | ✅ DONE | the written sum and its keypad (ones box first), no kids, no table |
| D5 | Hints: 1 wiggle + "फिर से लिखिए।"; 2 wiggle + adding the two numbers with blocks, the total's blocks kept on screen; 3 only the correct digit tappable | ✅ DONE | 2: a's and b's blocks appear beside their rows, then glide (ones, then tens) into the sum's row, grey copies left; 3: the keys light one at a time (ones digit first) |
| D6 | Right: "शाबाश! 41 और 30 का जोड़ 71 होता है।" / "बहुत अच्छे! 61 और 17 का जोड़ 79 होता है।"; after a wrong answer the same without the praise | ✅ DONE | ⚠ the deck's "61 और 17" is read as 62 (the sum shown is 62 + 17 = 79) — please confirm |
| D7 | "Move to the next screen." | ✅ DONE | no "अब अगली एक्टिविटी…" line any more — the next question comes after a short pause |
Kept from the earlier rounds (not in the deck's script): the table and top-view camera at the start of Q1 and Q2, the kids walking, the column's own line on a wrong build check ("इसमें इकाई कम है।" — the deck lists it as the alternative to "फिर से करिए।"), "शाबाश! अब दहाइयाँ जोड़िए।" before Q1's tens, and the closing screen with both cheering. Unused clips → `_archive_v1/game_round3/`. All 12 new clips transcribed back by Gemini (`vo_gm2_meet2` re-rendered once: "रूमी" was heard as "नूमी").
Verified: the whole game played through to the celebration (one wrong answer at each step), 0 console errors; Q3 with three wrong answers (blocks animation, then only "1", then "7"); the dev menu lists 11 parts (Q3/Q4: "टाइप करिए").

## Game review — 2026-10-30
| # | User | Status | How |
|---|---|---|---|
| E1 | No keypad in question 2 | ✅ DONE | Q2 adds like Q1: tap the ones, then the tens into the sum row ("पहले इकाइयाँ जोड़िए।" / "शाबाश! अब दहाइयाँ जोड़िए।"); the digits go into the boxes by themselves; "बहुत बढ़िया! 34 और 25 जोड़ने पर 59 मिले।" |
| E2 | Q3/Q4: the blocks after the 2nd wrong answer — in the table | ✅ DONE | a three-row दहाई–इकाई board comes in at the left and the written sum glides beside its rows; 41's blocks fill row 1, 30's row 2, then they go down into the sum row (ones, then tens), grey copies left; the total stays |
| E3 | The blocks on the table like the picture (rods lying flat, side by side; cubes in a grid) | ✅ DONE | real 3D boxes on the tabletop (CSS preserve-3d): each rod a 10-segment bar with a top, front and sides, lying pointing away; the cubes in rows of 3; they turn with the table in the camera move |
| E4 | Fix the table's edge at the bottom ends | ✅ DONE | the front edge and the legs now hang from the tabletop in 3D (the old flat strip stuck out past its rounded corners) |
| E5 | Kids walking with their legs moving | ✅ DONE | while walking, the picture is split at the hem / shorts line: each leg swings and lifts in turn on its own hip, the body bobs with each step (cut points measured from the art: `kids[].legs` in the card) |
Verified: the whole game played through (one wrong answer per step) to the celebration, 0 console errors; the walk checked frame by frame (animation paused); Q3 with three wrong answers (the table help, then the guided keys).

## Game review — 2026-10-30 (2)
| # | User | Status | How |
|---|---|---|---|
| F1 | The kids should look 7–8 years old | ✅ DONE | Rumi and Rohan redrawn younger (Gemini, from their own pictures): bigger heads, rounder faces, shorter limbs, the same clothes and colours — standing, cheering, both blink copies and the round portraits (`make_poses.py`, `make_portrait.py` from head-and-shoulders crops). The older set is in `_archive_v1/kids_older/` |
| F2 | Walk in side profile; face the front when they stop | ✅ DONE | new side-view pictures per child — mid-stride and legs-together (`char_<who>_walk1/2.webp`, `tools/make_walk.py`: one canvas, soles and head lined up) — take turns every 170 ms with a step bob, mirrored when walking left; at the stop the child turns to the front (its standing picture). Replaces E5's leg-cutting walk. Rohan's side pictures were drawn on grey (on magenta his hair came out purple); a purple cast in Rumi's side hair was neutralised |
| F3 | The kids appeared from between the screen — they should come from out of the screen | ✅ DONE | during the game the stage does not clip (`.stage[data-bg="meadow"]`), so the kids walk in from beyond the screen's real edge over the lawn the side bands continue; screen 1: Rumi from the left, Rohan from the right, up to the table; the build screen: each walks in from the left edge and Rumi walks off out of it |
Verified: the whole game played through (one wrong answer per step) to the celebration, 0 console errors; captures on a wide window (1700×800): the two walking in side-on over the bands, turned to the front at the table, Rumi walking off to the left.

## Game review — 2026-10-30 (3)
| # | User | Status | How |
|---|---|---|---|
| H1 | Change the kids — use the kids from the PPT as the reference | ✅ DONE | new Rumi and Rohan drawn from the review deck's mockup children (`ppt image24/25`), 7–8 years old, in the deck's cartoon style: Rumi — ponytail bun, pink polka-dot headband, yellow t-shirt, blue denim dungarees, pink sneakers; Rohan — blue cap with a yellow front, orange hoodie, blue jeans, white sneakers (their lower halves are not in the deck - chosen to match). Standing, cheering, blink copies, round portraits. Drawn on flat grey and keyed tighter (`KEY_NEAR=24 KEY_POCKET=12` for `make_poses.py` / `make_portrait.py`, so the white shoes stay); the floor shadow cleared. The previous set: `_archive_v1/kids_young_v2/` |
| H2 | The walking does not feel good | ✅ DONE | replaced the two-picture flip (F2) with a cut-out puppet: one side-view stride picture (`char_<who>_side.webp`, `tools/make_walk.py` measures the crotch, the hip and the legs' angle → `kids[].side` in the card) in three layers — the body, and each leg turning on the hip so the legs swing through each other step after step (eased like a pendulum), the body rising as they pass, the step timed to the ground covered (no sliding feet); the body's lower edge fades over the hips so no seam shows. Mirrored when walking left; the child turns to the front on stopping |
Verified: each child's walk checked frame by frame through a stride (animation paused); the whole game played through to the celebration, 0 console errors; captures on a wide window.
