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
