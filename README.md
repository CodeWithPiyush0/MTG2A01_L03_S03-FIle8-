# MTG2A01_L03_S03 — संख्याओं का जोड़ (Adds vertically without regrouping)

**Grade:** G2 · **LO:** MTG2A01_L03 · **Attribute:** A01 · **Type:** CORE
**Slides:** 12 · Tutorial 3 / Guided 4 / Practice 5 (the game and the celebration count as practice)
**Source:** `MTG2A01_L03_S03_review.pptx` (SME review 1). Every deck page is mapped in `CHANGES.md`.

## Built on MTG2A01_L04_S02's shell
The flow, layout, buttons, animation, colours and type are File7's (`../MTG2A01_L04_S02 (File7 Maths)`): the courtyard
cover with the wall title, the tutorial card, the header band with Swiftie's moods, the yellow → button, SFX + music,
the three phase screens, confetti, the nudge hand, the place-value table and its + source box, the answer cards and the
3 × 4 keypad, the 7 s reminders, "शाबाश" only on a first-try answer, the celebration. The SME's first draft (another
engine) is kept in `_archive_v1/`.

What this skill adds (`app.js` `[pv add]`, `style.css` `[pv add]`):
- **the stacked table** (`PVK.vtable`): one दहाई | इकाई head over three rows — the first number, "+" the second, a thick
  line, the sum (shaded). Each row is a table to the rest of File7's kit, so the + buttons, `childBuild`, `transfer`
  (a tapped block flies down, its grey copy stays) and the beats work on it unchanged.
- **the written sum beside it** (`PVK.vcards`): 23 / + 14 / a line / ?, each card level with its row.
- `moveKind` (the child moves the ones, then the tens — the other kind dimmed), `autoMove`, `soloSum` (the sum row alone,
  moved to the middle: deck "replacing the first two PV tables").
- the garden game `ADD_GAME` (deck slide 17) and the cover's "addv" build (Akash and Moni with their 23 and 14, the
  written sum appearing word by word with the greeting).

## The lesson
| slide | deck | type | what happens |
|---|---|---|---|
| landing | p1 | — | "संख्याओं का जोड़"; Akash and Moni glide in, their blocks drop, 23 / + 14 / ? appears with the greeting |
| T1 | p2 | STORY_ADD ask | "कुल कितने ब्लॉक्स?" Akash 23, Moni 14, the written sum 23 / + 14 — in sync with the VO |
| T2 | p3 | PV_ADD_DEMO | Swiftee builds 23, the child builds 14, moves the ones then the tens; 3 + 4 = 7, 2 + 1 = 3, 37 |
| T3 | p4 | STORY_ADD sum | "23 जोड़ 14 बराबर 37" — their blocks fly into one pile, 37 |
| G1 | p6 | PV_ADD build | 34 + 25: the child builds both rows, moves the ones, then the tens → 59 |
| G2 | slide 9 | PV_ADD mcq | 42 + 35 (77 / 76 / 14): built rows, the child moves the blocks, the sum row to the middle, pick |
| G3 | p7 | PV_ADD mcq | 56 + 33 (98 / 89 / 17) |
| G4 | p8 | PV_ADD numpad | 47 + 21 → 68 typed in the answer box under the table, flown into the "?" |
| P1 | p9 | MENTAL_ADD mcq | 61 / + 20 / ? (80 / 18 / 81); help: digits → blocks → the blocks merged, the right card lit |
| P2 | p10 | MENTAL_ADD numpad | 76 + 22 → 98 typed into the "?" |
| P3 | p11 | MENTAL_ADD numpad | 37 + 60 → 97 |
| GAME | slide 17 | ADD_GAME | Bibi & Johny, 4 activities (25+12, 13+55, 31+45, 42+46) in the garden |
| CEL | p14 | CELEBRATION | "शाबाश! अब आप ऊपर-नीचे लिखकर जोड़ सकते हैं। याद रखिए — जोड़ हमेशा इकाई से शुरू होता है।" |

Deleted (deck): pages 5, 12, 13. No sum needs regrouping (`tools/lessons.py` asserts it).

Art: Akash / Moni / Johny / Bibi are the existing portraits under new names (Madhav, Aanya, Aaru, Pari — user
2026-10-28); `assets/game_garden.webp` was generated (`tools/gen_image.py`, Gemini).

## Rebuilding
```
python tools/lessons.py          # card.json + tools/vo_script.json; embeds the card in index.html, copies MTG2A01_L03_S03.html
python tools/build_vo.py         # renders any VO line not yet on disk (GEMINI_KEY in the environment; ffmpeg)
python tools/lessons.py          # again after new VO: the cue times are measured from the clips
node tools/gen_asset_sizes.js    # the preload manifest - after ANY asset change
```
The key in `.env` is named `GKEY`: `set -a; . ./.env; set +a; export GEMINI_KEY=$GKEY`.
Dev: `index.html?slide=N` opens slide N directly; `?dev=1` adds the slide navigator.

## Deploying (Vercel)
As File7: a plain static site, `vercel.json` pins no build and the output directory `.`; `.vercelignore` keeps the dev
files out. The upload is `index.html`, `MTG2A01_L03_S03.html`, `app.js`, `style.css`, `swiftpal-bridge.js`, `vercel.json`, `assets/`.
