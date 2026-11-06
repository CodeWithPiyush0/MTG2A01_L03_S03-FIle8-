"""The lesson's voice-over manifest - lesson_vo_manifest.xlsx (the format of File7's, MTG2A01_L04_S02).

Four sheets:
  VO Manifest     every clip where it is heard, in game order (start screen, transitions, pages 1-11, celebration):
                  page, screen, #, Audio ID, the Hindi script (spoken exactly), what it is, when it plays, the other
                  pages that play the same recording, duration, status
  Recording list  each recording once, in the order it is first heard, with its file name
  Sound effects   the sound files the lesson plays (supplied, not recorded)
  Recording spec  scope, folder, format, how to put new recordings in

Reads card.json (the build's own text and the page order), tools/lessons.py (the new lines not recorded yet - its
rendered(new, old) pairs) and the clips on disk (durations). A new line with no clip yet is listed in place of the line
that plays meanwhile, status TO GENERATE.
    python tools/gen_vo_manifest.py
"""
import json, os, re, subprocess
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CARD = json.load(open(os.path.join(ROOT, "card.json"), encoding="utf-8"))
TEXT = CARD["assets"]["audio_text"]
VO_DIR = os.path.join(ROOT, "assets", "voiceover")
SFX_DIR = os.path.join(ROOT, "assets", "sfx")
OUT = os.path.join(ROOT, "lesson_vo_manifest.xlsx")
TITLE = CARD["title"]["hi"] + " (" + CARD["skill_code"] + ")"

on_disk = lambda cid: os.path.exists(os.path.join(VO_DIR, cid + ".ogg"))
# the new lines waiting for a recording: old id (in the card meanwhile) -> new id
NEW_FOR = {old: new for new, old in re.findall(r'rendered\(vo\("(\w+)".*?vo\("(\w+)"',
                                               open(os.path.join(HERE, "lessons.py"), encoding="utf-8").read(), re.S)
           if not on_disk(new)}


def duration(path):
    try:
        return round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                                          capture_output=True, text=True).stdout.strip()), 2)
    except Exception:
        return None


# ---- what each role is and when it plays (the build's behaviour) ----
ROLE = {
    # T1 / T3 - the story (Akash and Moni)
    ("T1", "a"): ("story - Akash and Moni", "as the page opens; the two portraits come in, their blocks drop in on «ये सारे ब्लॉक्स»"),
    ("T1", "b"): ("story - 23 and 14", "next; 23 comes in on «23» (Akash's blocks beat), + 14 on «14» (Moni's blocks beat)"),
    ("T1", "ask"): ("story - the question", "next; the + on «दोनों», the line and the two empty boxes on «मिलाकर»; then the next button"),
    ("T3", "eq"): ("story's answer - the sum", "as the page opens; 23 with Akash, +, 14 with Moni; on «बराबर» their blocks fly into one pile, on «37» the box fills"),
    ("T3", "tot"): ("story's answer - the end", "after confetti; the names light, the pile beats and the 37 lights; then the next button"),
    # T2 - Swiftee shows it, the child builds 14 and moves the blocks
    ("T2", "head"): ("demo - what we will do", "as the page opens"),
    ("T2", "intro"): ("demo - build both numbers", "next; the table comes in with its first row"),
    ("T2", "r1"): ("demo - 23 = 2 tens 3 ones", "the 23 comes in; its digits light on «2 दहाई» / «3 इकाई»"),
    ("T2", "tens"): ("demo - the tens", "Swiftee's hand taps the rod + twice"),
    ("T2", "ones"): ("demo - the ones", "Swiftee's hand taps the cube + three times"),
    ("T2", "r2"): ("demo - 14 = 1 ten 4 ones", "the second row and + 14 come in; its digits light on «1 दहाई» / «4 इकाई»"),
    ("T2", "build"): ("the child builds 14", "the rod + pulses; the child taps it, then the cube + (7s idle: the hand on the + to tap)"),
    ("T2", "go"): ("now add them", "the + buttons go; the + on «दोनों», the sum row with the line and the two empty boxes on «जोड़ते»"),
    ("T2", "o_add"): ("add the ones", "the ones pulse (the tens dimmed); the child taps them down into the sum row"),
    ("T2", "o_sum"): ("the ones added", "the ones of each row beat and their digits light as said; the 7 fills the ones box"),
    ("T2", "t_add"): ("add the tens", "the tens pulse; the child taps them down"),
    ("T2", "t_sum"): ("the tens added", "the tens of each row beat and their digits light as said; the 3 fills the tens box"),
    ("T2", "total"): ("the result", "the columns beat, the digits of 37 light on «दहाइयाँ» / «इकाइयाँ», 37 on «यानी 37»"),
    ("T2", "done"): ("the completion line", "confetti; 23, 14 and 37 light as each is said; then the next button"),
    # G1 - the child builds both numbers
    ("G1", "intro"): ("build both numbers", "as the page opens"),
    ("G1", "r1"): ("34 = 3 tens 4 ones - build it", "the first row lights; the digits light on «3 दहाई» / «4 इकाई»; then the rod + pulses (7s idle: the hand on the + to tap)"),
    ("G1", "r2"): ("25 = 2 tens 5 ones - build it", "the second row lights; the same for 25"),
    ("G1", "go"): ("now add them", "the + comes in on «दोनों»"),
    ("G1", "o_add"): ("add the ones", "the ones pulse; the child taps them down into the sum row"),
    ("G1", "o_sum"): ("the ones added", "the ones beat and their digits light as said; the 9 fills the ones box"),
    ("G1", "t_add"): ("add the tens", "the tens pulse; the child taps them down"),
    ("G1", "t_sum"): ("the tens added", "the tens beat and their digits light as said; the 5 fills the tens box"),
    ("G1", "total"): ("the result", "the columns beat, 59 lights on «यानी 59»"),
    ("G1", "correct"): ("the completion line", "confetti; 34, 25 and 59 light as each is said"),
    # the guided / practice pages
    "prompt": ("page instruction", "as the page opens, the two numbers built (the speaker replays it); the + on «जोड़िए»"),
    "tap_o": ("inactivity reminder - add the ones", "the ones to tap pulse; after 7s with no tap this line, again every 7s"),
    "tap_t": ("inactivity reminder - add the tens", "the tens to tap pulse; after 7s with no tap this line, again every 7s"),
    "tap_o_hand": ("inactivity reminder - add the ones", "the ones pulse; after 7s with no tap this line and the hand on a block, again every 7s"),
    "tap_t_hand": ("inactivity reminder - add the tens", "the tens pulse; after 7s with no tap this line and the hand on a block, again every 7s"),
    "idle_build_t": ("inactivity reminder - building the tens", "after 7s with no tap at the build step: the rod + pulses, the hand on it, this line"),
    "idle_build_o": ("inactivity reminder - building the ones", "after 7s with no tap at the build step: the cube + pulses, the hand on it, this line"),
    "ask": ("the answer question", "the blocks are down; the heading changes, the sum row moves to the middle and three cards come in"),
    "reask_pick": ("inactivity reminder - pick", "the cards wait; after 7s with no tap, again every 7s"),
    "reask_type": ("inactivity reminder - type", "the ? waits (the hand on it); after 7s with no tap, again every 7s"),
    "h1_pick": ("Hint 1 (1st wrong answer)", "the wrong card wiggles"),
    "h1_type": ("Hint 1 (1st wrong answer)", "the box wiggles"),
    "h2": ("Hint 2 (2nd wrong answer)", "the sum row's tens column beats on «दहाइयाँ», the ones on «इकाइयाँ»"),
    "reveal_sum": ("Hint 3 (3rd wrong answer)", "the right card lit, the others off"),
    "correct": ("correct answer", "the answer goes into the ?; confetti; the numbers light as each is said"),
    "correct_late": ("correct answer after a wrong one", "the same as the correct line, without «शाबाश» (only a first-try answer gets it)"),
    # G4 - each column typed
    "type_o": ("type the ones", "the ones are down; the hand on the ones box of the ?; a tap opens the keypad (again after 7s idle)"),
    "type_t": ("type the tens", "the tens are down; the hand on the tens box; a tap opens the keypad (again after 7s idle)"),
    "again_o": ("Hint 1 - ones (1st wrong digit)", "the ones box wiggles"),
    "again_t": ("Hint 1 - tens (1st wrong digit)", "the tens box wiggles"),
    "is_o_g4": ("Hint 2 - ones (2nd wrong digit)", "the box wiggles; only the right key works"),
    "is_t_g4": ("Hint 2 - tens (2nd wrong digit)", "the box wiggles; only the right key works"),
    # P1-P3
    "prompt_pick": ("page instruction", "as the page opens; the sum written one under the other, three cards under it"),
    "prompt_type": ("page instruction", "as the page opens; the sum in the middle; a tap on the ? opens the keypad and the sum moves left"),
    "h1_mental": ("Hint 1 (1st wrong answer)", "the ones digits light on «… इकाई और … इकाई», then the tens digits on «… दहाई और … दहाई»"),
    "h2_mental_pick": ("Hint 2 (2nd wrong answer)", "the table comes in: both numbers in blocks, they move down into the sum row, its digits under the columns"),
    "h2_mental_type": ("Hint 2 (2nd wrong answer)", "the keypad moves right; the table comes in: both numbers in blocks, they move into the sum row, its digits under the columns"),
    "reveal_n_pick": ("Hint 3 (3rd wrong answer)", "the right card lit, the others off"),
    "reveal_n_type": ("inactivity reminder after Hint 3", "after 7s idle while the right keys are lit"),
    "is_o_mental": ("Hint 3 - the ones (3rd wrong answer)", "only the right keys work, the ones first; this line as the ones key lights"),
    "is_t_mental": ("Hint 3 - the tens", "once the ones key is typed; the tens key lights"),
    # the game
    "gm_intro1": ("activity 1 - the story", "the two walk in behind a table with their blocks; each hops and their blocks pop on their name"),
    "gm_build_a1": ("activity 1 - build Rumi's number", "the board; Rumi walks in with her 25; the child sets the − / + counters and taps जाँचें"),
    "gm_ok_a1": ("activity 1 - Rumi's is right", "Rumi walks off on «अब», Rohan walks in with his 12; the board empties"),
    "gm_intro2": ("activity 2 - the story", "the two behind the table with their blocks; then the child builds both numbers (no line between)"),
    "gm_again": ("1st wrong check", "the wrong column's blocks wiggle; the board empties"),
    "gm_t_more": ("2nd wrong check - too many tens", "the tens wiggle; only the tens − works until it is right"),
    "gm_t_less": ("2nd wrong check - too few tens", "the tens wiggle; only the tens + works until it is right"),
    "gm_o_more": ("2nd wrong check - too many ones", "the ones wiggle; only the ones − works until it is right"),
    "gm_o_less": ("2nd wrong check - too few ones", "the ones wiggle; only the ones + works until it is right"),
    "gm_add": ("add the two", "both numbers built; the board of three rows comes in"),
    "gm_ones": ("add the ones first", "the ones pulse; the child taps them down (also when the tens are tapped first - from the 2nd time the hand on a ones block, the 3rd time the tens are off)"),
    "gm_tap_o": ("inactivity reminder - add the ones", "after 7s with no tap: the ones pulse, the hand on one, this line"),
    "gm_tens": ("now the tens", "the ones are down and their digit filled; the tens pulse"),
    "gm_tap_t": ("inactivity reminder - add the tens", "after 7s with no tap: the tens pulse, the hand on one, this line"),
    "gm_done": ("activity done", "confetti, both hop; each number and its blocks light as said, the sum on its number"),
    "gm_type": ("activity - type the sum", "the sum one under the other, their faces beside their numbers; a tap on the ? opens the keypad (again after 7s idle)"),
    "gm_rewrite": ("Hint 1 (1st wrong answer)", "the ? wiggles"),
    "gm_type_h2": ("Hint 2 (2nd wrong answer) - no line", "the board comes in at the left with the blocks of the wrong column(s) only, and adds them"),
    "gm_type_h3": ("Hint 3 (3rd wrong answer) - no line", "only the right keys work, in turn"),
    "gm_done_t": ("correct answer", "confetti; each number lights as said, the sum on its number"),
    "gm_late": ("correct answer after a wrong one", "the same, without «शाबाश»"),
    "gm_final": ("the game's end", "both cheer; confetti"),
    "cel": ("celebration", "the end screen: Swiftee cheers and says the line lip-synced"),
}


def page_rows(s):
    """the clips of one page in the order they are heard: [(audio id, (what, when))]"""
    sid, au, d, ty = s["id"], s.get("audio") or {}, s.get("data") or {}, s["type"]
    out = []
    def add(cid, key):
        if cid:
            out.append((cid, ROLE[key]))
    hand = d.get("idle_hand")
    if ty == "STORY_ADD":
        for r in ("a", "b", "ask", "eq", "tot"):
            add(au.get(r), (sid, r))
    elif ty == "PV_ADD_DEMO":
        for r in ("head", "intro", "r1", "tens", "ones", "r2", "build"):
            add(au.get(r), (sid, r))
        add("vo_idle_build_t", "idle_build_t"); add("vo_idle_build_o", "idle_build_o")
        for r in ("go", "o_add", "tap_o", "o_sum", "t_add", "tap_t", "t_sum", "total", "done"):
            add(au.get(r), (r + ("_hand" if hand else "")) if r in ("tap_o", "tap_t") else (sid, r))
    elif ty == "PV_ADD" and d.get("build"):
        for r in ("intro", "r1"):
            add(au.get(r), (sid, r))
        add("vo_idle_build_t", "idle_build_t"); add("vo_idle_build_o", "idle_build_o")
        add(au.get("r2"), (sid, "r2"))
        for r in ("go", "o_add", "tap_o", "o_sum", "t_add", "tap_t", "t_sum", "total", "correct"):
            add(au.get(r), (r + ("_hand" if hand else "")) if r in ("tap_o", "tap_t") else (sid, r))
    elif ty == "PV_ADD" and d.get("answer") == "mcq":
        add(au.get("prompt"), "prompt"); add(au.get("tap_o"), "tap_o"); add(au.get("tap_t"), "tap_t")
        add(au.get("ask"), "ask"); add(au.get("reask"), "reask_pick")
        add(au.get("h1"), "h1_pick"); add(au.get("h2"), "h2"); add(au.get("reveal"), "reveal_sum")
        add(au.get("correct"), "correct"); add(au.get("correct_late"), "correct_late")
    elif ty == "PV_ADD":                                                    # G4: each column typed
        add(au.get("prompt"), "prompt")
        for k in ("o", "t"):
            add(au.get("tap_" + k), "tap_" + k); add(au.get("type_" + k), "type_" + k)
            add(au.get("again_" + k), "again_" + k); add(au.get("is_" + k), "is_%s_g4" % k)
        add(au.get("correct"), "correct"); add(au.get("correct_late"), "correct_late")
    elif ty == "MENTAL_ADD":
        pick = d.get("answer") == "mcq"
        add(au.get("prompt"), "prompt_pick" if pick else "prompt_type"); add(au.get("reask"), "reask_pick" if pick else "reask_type")
        add(au.get("h1"), "h1_mental"); add(au.get("h2"), "h2_mental_pick" if pick else "h2_mental_type")
        if pick:
            add(au.get("reveal"), "reveal_n_pick")
        else:
            add(au.get("is_o"), "is_o_mental"); add(au.get("is_t"), "is_t_mental"); add(au.get("reveal"), "reveal_n_type")
        add(au.get("correct"), "correct"); add(au.get("correct_late"), "correct_late")
    elif ty == "CELEBRATION":
        add(au.get("prompt"), "cel")
    return out


def game_screens(s):
    """the game page: one screen per activity, then the end"""
    au, d = s["audio"], s["data"]
    out = []
    for i, ((a, b), mode) in enumerate(zip(d["acts"], d["modes"]), 1):
        rows = []
        def add(cid, key):
            if cid:
                rows.append((cid, ROLE[key]))
        wrong = lambda: [add(au.get(r), "gm_" + r) for r in ("again", "t_more", "t_less", "o_more", "o_less")]
        if mode == "keypad":
            add(au.get("type%d" % i), "gm_type"); add(au.get("rewrite"), "gm_rewrite")
            rows.append(("-", ROLE["gm_type_h2"])); rows.append(("-", ROLE["gm_type_h3"]))
            add(au.get("done%d" % i), "gm_done_t"); add(au.get("late%d" % i), "gm_late")
        else:
            add(au.get("intro%d" % i), "gm_intro%d" % min(i, 2))
            if au.get("build_a%d" % i):
                add(au.get("build_a%d" % i), "gm_build_a1"); wrong(); add(au.get("ok_a%d" % i), "gm_ok_a1")
            else:
                wrong()
            add(au.get("add"), "gm_add"); add(au.get("ones"), "gm_ones"); add(au.get("tap_o"), "gm_tap_o")
            add(au.get("tens"), "gm_tens"); add(au.get("tap_t"), "gm_tap_t"); add(au.get("done%d" % i), "gm_done")
        out.append(("GAME · activity %d  (%d + %d%s)" % (i, a, b, ", type it" if mode == "keypad" else ", blocks"), rows))
    out.append(("GAME · the end", [(au["final"], ROLE["gm_final"])]))
    return out


# ---- the game order ----
slides = CARD["slides"]
order = [("Start screen", "Start screen", [("vo_landing", ("greeting", "the start screen: Swiftee's greeting as Rumi and Rohan walk in with their blocks"))]),
         ("Transition 1", "before page 1", [("vo_pt_tutorial", ("transition line", "Swiftee rises talking; «चलिए, शुरू करें!» wipes in as it is said"))])]
gate_before = {"G1": ("Transition 2", "before page 4", "vo_pt_guided", "«चलिए, साथ में करें!»"),
               "P1": ("Transition 3", "before page 8", "vo_pt_practice", "«अब आपकी बारी!»")}
for i, s in enumerate(slides):
    if s["id"] in gate_before:
        g = gate_before[s["id"]]
        order.append((g[0], g[1], [(g[2], ("transition line", "Swiftee rises talking; " + g[3] + " wipes in"))]))
    if s["type"] == "CELEBRATION":
        order.append(("Celebration", "CEL · CELEBRATION", page_rows(s)))
    elif s["type"] == "ADD_GAME":
        for screen, rows in game_screens(s):
            order.append(("Page %d" % (i + 1), screen, rows))
    else:
        dd = s.get("data") or {}
        screen = s["id"] + " · " + s["type"] + ("  (%d + %d)" % (dd["a"], dd["b"]) if "a" in dd else "")
        order.append(("Page %d" % (i + 1), screen, page_rows(s)))

# a new line not recorded yet takes the place of the line that plays meanwhile
order = [(p, sc, [(NEW_FOR.get(cid, cid), (what + (" - NEW LINE, replaces " + cid + " (which plays until it is recorded)" if cid in NEW_FOR else ""), when))
                  for cid, (what, when) in rows]) for p, sc, rows in order]

# where else each recording is heard
heard = {}
for page, screen, rows in order:
    for cid, _ in rows:
        if cid == "-":
            continue
        heard.setdefault(cid, [])
        if page not in heard[cid]:
            heard[cid].append(page)

DUR = {cid: duration(os.path.join(VO_DIR, cid + ".ogg")) if on_disk(cid) else None for cid in heard}
def status(cid):
    if cid == "-":
        return ""
    return "TTS (Gemini, Kore)" if on_disk(cid) else "TO GENERATE"

manifest = []
n = 0
for page, screen, rows in order:
    for k, (cid, (what, when)) in enumerate(rows, 1):
        n += 1
        also = ", ".join(p for p in heard.get(cid, []) if p != page)
        manifest.append(([n, page, screen, k, cid, TEXT.get(cid, "(no line)" if cid == "-" else ""), what, when, also, DUR.get(cid), status(cid)], status(cid)))

recordings = []
for page, screen, rows in order:
    for cid, _ in rows:
        if cid != "-" and cid not in [r[0][1] for r in recordings]:
            recordings.append(([len(recordings) + 1, cid, cid + ".ogg", TEXT.get(cid, ""), ", ".join(heard[cid]), DUR[cid], status(cid)], status(cid)))
todo = [r[0][1] for r in recordings if r[1] == "TO GENERATE"]
# in the card but never heard (kept for safety); the lines a new one replaces
unheard = sorted(k for k in CARD["assets"]["audio"] if k.startswith("vo_") and k not in heard and k not in NEW_FOR)

SFX = [("sfx_play", "Play button on the start screen - on the press", "Start"),
       ("sfx_next", "Next arrow (pages 1-3) - on a real press", "1-3"),
       ("sfx_gate_whoosh", "The three transition screens - as each opens", "transitions"),
       ("sfx_whoosh", "Start screen - only if a child's walking picture fails to load (the glide-in instead)", "Start"),
       ("sfx_correct", "Correct answer; a box filling; a right check in the game", "2-11"),
       ("sfx_wrong", "Wrong answer / a wrong check in the game", "5-11"),
       ("sfx_confetti", "Confetti on a correct answer", "2-11"),
       ("sfx_nudge", "A button / block pulsing again when the child is idle (with the hand)", "2-11"),
       ("bgm", "Background music - from the play button on, dipped under the voice; paused while the tab is hidden", "all")]
sfx_rows = []
for sid, what, pages in SFX:
    f = os.path.join(SFX_DIR, sid + ".ogg")
    sfx_rows.append(([sid, "assets/sfx/" + sid + ".ogg", what, pages, duration(f) if os.path.exists(f) else "MISSING"], None))
f = os.path.join(VO_DIR, "sfx_celebrate.ogg")
sfx_rows.append((["sfx_celebrate", "assets/voiceover/sfx_celebrate.ogg", "Celebration screen - as it opens", "Celebration",
                  duration(f) if os.path.exists(f) else "MISSING"], None))

# ---- the workbook ----
thin = Side(style="thin", color="C9CED6"); box = Border(left=thin, right=thin, top=thin, bottom=thin)
hfill = PatternFill("solid", fgColor="1F4E79"); DEV = "Nirmala UI"
PAGE_FILL = {"Start screen": "EAF2FB", "Celebration": "FFF4D6"}


def sheet(ws, title, sub, head, widths, data, dev_col=None, wrap_cols=(), center=(), freeze="E5", fill=None):
    ws.append([title]); ws["A1"].font = Font(bold=True, size=14, color="1F4E79")
    ws.append([sub]); ws["A2"].font = Font(italic=True, size=10, color="555555")
    ws.append([])
    ws.append(head)
    for c in range(1, len(head) + 1):
        cell = ws.cell(row=4, column=c)
        cell.font = Font(bold=True, color="FFFFFF"); cell.fill = hfill; cell.border = box
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for row, meta in data:
        ws.append(row); r = ws.max_row
        for c in range(1, len(head) + 1):
            cell = ws.cell(row=r, column=c); cell.border = box
            if fill: cell.fill = PatternFill("solid", fgColor=fill(row))
            cell.alignment = Alignment(vertical="center", wrap_text=(c in wrap_cols), horizontal="center" if c in center else None)
            if dev_col and c == dev_col:
                cell.font = Font(name=DEV, size=12, bold=True)
        if meta == "TO GENERATE":
            for c in range(1, len(head) + 1):
                ws.cell(row=r, column=c).fill = PatternFill("solid", fgColor="FDECEA")
            ws.cell(row=r, column=len(head)).font = Font(bold=True, color="B03A2E")
    for i, w in enumerate(widths):
        ws.column_dimensions[chr(65 + i)].width = w
    if freeze: ws.freeze_panes = freeze


def page_fill(row):
    p = str(row[1])
    if p.startswith("Transition"): return "EEF7EE"
    return PAGE_FILL.get(p, "FFFFFF" if int(row[0]) % 2 else "F7F9FC")


wb = Workbook()
ws = wb.active; ws.title = "VO Manifest"
sheet(ws, TITLE + " - lesson vo",
      "Start screen -> transitions and pages 1-11 in game order (page 11: the game, by activity) -> celebration. On each page: what "
      "plays as it opens, the steps, the 7s reminders and the 1st / 2nd / 3rd wrong answer (Hint 1, 2, 3), then the correct answer."
      + (" %d line(s) TO GENERATE (red)." % len(todo) if todo else ""),
      ["S.No", "Page", "Screen", "#", "Audio ID", "Hindi script (spoken exactly)", "What it is", "When it plays", "Same recording also on",
       "Duration (s)", "Status"],
      [6, 13, 30, 4, 22, 50, 30, 62, 22, 10, 18], manifest, dev_col=6, wrap_cols=(3, 6, 7, 8, 9), center=(1, 4, 10), fill=page_fill)
sheet(wb.create_sheet("Recording list"), "Recording list - each recording once, in the order it is first heard",
      "%d recordings%s. Record each once; the file name is the Audio ID + .ogg, in assets/voiceover/." %
      (len(recordings), (" - %d TO GENERATE: %s" % (len(todo), ", ".join(todo))) if todo else ""),
      ["S.No", "Audio ID", "File name", "Hindi script (spoken exactly)", "Plays on", "Duration (s)", "Status"],
      [6, 22, 24, 54, 44, 10, 22], recordings, dev_col=4, wrap_cols=(4, 5), center=(1, 6))
sheet(wb.create_sheet("Sound effects"), "Sound effects and music (supplied - not recorded)",
      "Only the files the lesson plays. The small interface sounds (taps, a block appearing / moving / popping, a block set "
      "down) are made in the browser (WebAudio) - no file.",
      ["Audio ID", "File name", "What it is / where it plays", "Page(s)", "Duration (s)"],
      [20, 34, 84, 12, 11], sfx_rows, wrap_cols=(3,), center=(5,), freeze=None)
sp = wb.create_sheet("Recording spec")
SPEC = [
    (TITLE + " - recording spec", None), (None, None),
    ("Scope", "The whole lesson - start screen, 3 transitions, 11 pages (T1-T3, G1-G4, P1-P3, the game with its 4 activities), celebration."),
    ("Order", "Game order. On each page: what plays as it opens, the steps, the 7s inactivity reminders, then the 1st / 2nd / 3rd "
              "wrong answer (Hint 1, 2, 3) and the correct answer. A recording heard on more than one page is listed on each "
              "('Same recording also on'). A help step with no line is listed with Audio ID '-'."),
    ("Clips", "%d rows, %d distinct recordings (see 'Recording list')." % (len(manifest), len(recordings)) +
              (" TO GENERATE: " + ", ".join(todo) + " (new lines - until they are recorded the line they replace plays)." if todo else "") +
              (" In the card but not heard in this build (not listed): " + ", ".join(unheard) + "." if unheard else "")),
    ("Folder", "assets/voiceover/<Audio ID>.ogg - the file name is the Audio ID."),
    ("Voice", "Gemini TTS (gemini-2.5-flash-preview-tts, voice Kore, tools/build_vo.py)."),
    ("Format", "Ogg/Opus, 48 kHz mono, 32 kbps; 0.28 s before the voice, 0.36 s after; -18.5 LUFS (two-pass loudnorm)."),
    ("Register", "आप form throughout (the transition lines included); the celebration line is Swiftee's «तुमने»."),
    ("Script", "Record exactly the text in the Hindi script column - it is the build's own text. Numbers written in digits are "
               "read as Hindi words (23 = तेईस, 37 = सैंतीस)."),
    ("Timing", "Several pages light / move things on given words of a clip (e.g. «दोनों» brings the +, «बराबर» flies the blocks into "
               "one pile, each number lights as it is said). The times are measured from each clip's length: after new recordings "
               "run  python tools/lessons.py  so they are measured again from the new takes."),
    ("Celebration", "Swiftee's lip-sync on the celebration line is measured from vo_cel2.ogg by tools/lessons.py - re-run it after a new take."),
    ("New takes", "Generate with  python tools/build_vo.py  (the missing ones, needs Gemini credits), or make them elsewhere as "
                  "<Audio ID>.wav / .mp3 in one folder and run  python tools/build_vo.py --from <folder>  (finished as the others). "
                  "Then  python tools/lessons.py  and  node tools/gen_asset_sizes.js  (bump the ?v= stamp in index.html so "
                  "browsers fetch the new audio)."),
    ("Regenerate", "python tools/gen_vo_manifest.py"),
]
for r, (a, b_) in enumerate(SPEC, 1):
    sp.cell(row=r, column=1, value=a); sp.cell(row=r, column=2, value=b_)
    sp.cell(row=r, column=1).font = Font(bold=True, size=14 if r == 1 else 11, color="1F4E79" if b_ is None else "000000")
    if b_:
        sp.cell(row=r, column=2).font = Font(name=DEV, size=11)
        sp.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
        sp.cell(row=r, column=1).alignment = Alignment(vertical="top")
sp.column_dimensions["A"].width = 16; sp.column_dimensions["B"].width = 120

wb.save(OUT)
print("lesson_vo_manifest.xlsx: %d rows, %d recordings%s" % (len(manifest), len(recordings), ("; TO GENERATE: " + ", ".join(todo)) if todo else ""))
if unheard:
    print("in the card, not heard:", ", ".join(unheard))
