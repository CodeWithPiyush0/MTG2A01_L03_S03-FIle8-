"""MTG2A01_L03_S03 - the lesson, page by page (SME deck MTG2A01_L03_S03_review.pptx).

The one place the content lives: every slide, its on-screen text and its VO lines. Writes
    card.json               - the card (also embedded in index.html, <script id="cardData">)
    tools/vo_script.json    - clip id -> Hindi line, for tools/build_vo.py
and copies index.html to MTG2A01_L03_S03.html (the same game under the skill code's name).

    python tools/lessons.py

Built on MTG2A01_L04_S02's shell (File7: the same flow, layout, buttons, animation, colours, type). Lines are the
deck's, verbatim, with spelling / agreement slips fixed (ब्लॉकस -> ब्लॉक्स, खेल रहे है -> खेल रहे हैं, ब्लॉक्स है -> हैं,
जोड़ते है -> हैं) and the one number slip of page 6 (its completion line says 52 for 34 + 25 = 59) - see CHANGES.md.
"""
import json, os, re, shutil, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

VO = {}          # clip id -> line


def vo(cid, line):
    if cid in VO and VO[cid] != line:
        raise SystemExit(f"clip {cid} given two different lines")
    VO[cid] = line
    return cid


# ---- shared lines -----------------------------------------------------------------------------------------
vo("vo_landing", "नमस्ते दोस्त! मैं हूँ स्विफ्टी! आज हम संख्याओं को जोड़ना सीखेंगे।")        # deck page 1
vo("vo_pt_tutorial", "ध्यान से देखिए और मेरे साथ जानिए। चलिए, शुरू करें!")                     # (File7's phase screens)
vo("vo_pt_guided", "बहुत बढ़िया! अब हम साथ मिलकर शुरू करते हैं। चलिए, साथ में करें!")
vo("vo_pt_practice", "वाह! अब आपकी बारी।")
vo("vo_idle_build_t", "अब दहाई बनाइए।"); vo("vo_idle_build_o", "अब इकाई बनाइए।")               # (File7's 7s build reminders)
ASK_PICK = vo("vo_ask_pick", "सही जोड़ चुनिए।")                                                  # deck page 9's VO (also the 7s re-ask)
ASK_TYPE = vo("vo_ask_type", "सही जोड़ टाइप करिए।")                                              # deck pages 10-11's VO (also the 7s re-ask)

CAST = {"आकाश": "akash", "मोनी": "moni"}
PEOPLE = [{"who": "akash", "name": "आकाश"}, {"who": "moni", "name": "मोनी"}]


def split(n):
    return n // 10, n % 10


slides = []

# deck page 2 - replaced: "कुल कितने ब्लॉक्स?" Akash and Moni with their blocks and their numbers, 23 / + 14 one under the
# other; everything in sync with the VO (one deck line, said as three clips so the pictures can follow it)
slides.append({
    "id": "T1", "phase": "tutorial", "eis": "iconic", "type": "STORY_ADD", "prompt_hi": "कुल कितने ब्लॉक्स?",
    "audio": {"a": vo("vo_t1_a", "आकाश और मोनी ब्लॉक्स से खेल रहे हैं, और ये सारे ब्लॉक्स मिलाकर एक ऊँची बिल्डिंग बना रहे हैं।"),
              "b": vo("vo_t1_b", "आकाश के पास 23 ब्लॉक्स हैं और मोनी के पास 14 ब्लॉक्स हैं।"),
              "ask": vo("vo_t1_ask", "चलिए, पता करते हैं, दोनों के पास मिलाकर कुल कितने ब्लॉक्स हैं?")},
    "data": {"mode": "ask", "a": 23, "b": 14, "people": PEOPLE}})

# deck page 3 - 23 + 14 in the stacked table: Swiftee builds 23, the child builds 14, the child moves the ones, then the tens
slides.append({
    "id": "T2", "phase": "tutorial", "eis": "iconic", "type": "PV_ADD_DEMO", "prompt_hi": "आइए, 23 और 14 को जोड़ते हैं।",
    "audio": {"head": vo("vo_t2_head", "आइए, 23 और 14 को जोड़ते हैं।"),
              "intro": vo("vo_t2_intro", "सबसे पहले ब्लॉक्स की सहायता से दोनों संख्याएँ बनाते हैं।"),
              "r1": vo("vo_t2_r1", "23 में 2 दहाई और 3 इकाई हैं।"),
              "tens": vo("vo_t2_tens", "पहले 2 दहाई के लिए 2 बंडल रखते हैं।"),
              "ones": vo("vo_t2_ones", "अब 3 इकाई के लिए 3 ब्लॉक रखते हैं।"),
              "r2": vo("vo_t2_r2", "इसी तरह, 14 में 1 दहाई और 4 इकाई हैं।"),
              "build": vo("vo_t2_build", "अब आप ब्लॉक्स की सहायता से 14 बनाइए।"),
              "go": vo("vo_t2_go", "बहुत बढ़िया! अब दोनों संख्याओं को जोड़ते हैं।"),
              "o_add": vo("vo_t2_o_add", "पहले इकाइयों को जोड़ते हैं।"),
              "o_sum": vo("vo_t2_o_sum", "3 इकाई और 4 इकाई मिलाकर हुई, 7 इकाई।"),
              "t_add": vo("vo_t2_t_add", "अब दहाइयों को जोड़ते हैं।"),
              "t_sum": vo("vo_t2_t_sum", "2 दहाई और 1 दहाई मिलाकर हुई, 3 दहाई।"),
              "total": vo("vo_t2_total", "अब हमारे पास कुल 3 दहाइयाँ और 7 इकाइयाँ हैं, यानी 37"),
              "done": vo("vo_t2_done", "इसलिए, 23 और 14 को जोड़ने पर 37 मिलता है।")},
    "data": {"a": 23, "b": 14, "demo": True}})

# deck page 4 - replaced: "कुल कितने ब्लॉक्स?" again - their blocks come together, 23 / + 14 / 37
slides.append({
    "id": "T3", "phase": "tutorial", "eis": "iconic", "type": "STORY_ADD", "prompt_hi": "कुल कितने ब्लॉक्स?",
    "audio": {"eq": vo("vo_t3_eq", "23 जोड़ 14 बराबर 37"),
              "tot": vo("vo_t3_tot", "आकाश और मोनी के पास कुल मिलाकर 37 ब्लॉक्स हैं।")},
    "data": {"mode": "sum", "a": 23, "b": 14, "people": PEOPLE}})

# deck page 5: deleted

# deck page 6 (G1) - 34 + 25: the child builds both numbers (the rows tapped by themselves), then moves the ones, then the tens
slides.append({
    "id": "G1", "phase": "guided", "eis": "iconic", "type": "PV_ADD", "prompt_hi": "संख्याएँ जोड़िए।",
    "audio": {"intro": vo("vo_g1_intro", "पहले ब्लॉक्स की सहायता से दोनों संख्याएँ बनाते हैं।"),
              "r1": vo("vo_g1_r1", "34 में 3 दहाई और 4 इकाई हैं। ब्लॉक्स की सहायता से 34 बनाइए।"),
              "r2": vo("vo_g1_r2", "25 में 2 दहाई और 5 इकाई हैं। ब्लॉक्स की सहायता से 25 बनाइए।"),
              "go": vo("vo_g1_go", "बहुत बढ़िया! अब दोनों संख्याओं को जोड़ते हैं।"),
              "o_add": vo("vo_g1_o_add", "पहले इकाइयों को जोड़ते हैं।"),
              "o_sum": vo("vo_g1_o_sum", "4 इकाई और 5 इकाई मिलाकर हुईं, 9 इकाई।"),
              "t_add": vo("vo_g1_t_add", "अब दहाइयों को जोड़ते हैं।"),
              "t_sum": vo("vo_g1_t_sum", "3 दहाई और 2 दहाई मिलाकर हुईं, 5 दहाई।"),
              "total": vo("vo_g1_total", "अब हमारे पास कुल 5 दहाइयाँ और 9 इकाइयाँ हैं, यानी 59"),
              "correct": vo("vo_g1_correct", "शाबाश! 34 और 25 को जोड़ने पर 59 मिलता है।")},   # (deck: "52" - a slip, 34 + 25 = 59)
    "data": {"a": 34, "b": 25, "build": True, "answer": "none"}})


def pv_add(sid, a, b, answer, options=None):
    """deck slides 9-11: the tables come with a and b built one by one; the child moves the ones, then the tens, into the
    sum row; then the answer - three cards (the sum row moves to the middle) or the number pad (an answer box below)"""
    s = a + b; st, so = split(s); low = sid.lower()
    pick = answer == "mcq"
    au = {"prompt": vo(f"vo_{low}_prompt", f"{a} और {b} को जोड़िए।" if pick else f"{a} और {b} को जोड़िए और सही जोड़ टाइप करिए।"),
          "h1": vo("vo_h1_pick" if pick else "vo_h1_type",
                   "ब्लॉक्स को गिनिए और सही जोड़ चुनिए।" if pick else "ब्लॉक्स को गिनिए और सही जोड़ टाइप करिए।"),
          "h2": vo(f"vo_{low}_h2", f"ध्यान से देखिए, कुल {st} दहाइयाँ और {so} इकाइयाँ हैं।"),
          "correct": vo(f"vo_{low}_correct", f"शाबाश! {a} और {b} का जोड़ {s} है।"),
          "reask": ASK_PICK if pick else ASK_TYPE}
    if pick:
        au["ask"] = vo("vo_ask_pick2", "बहुत बढ़िया! अब सही जोड़ चुनिए।")
    d = {"a": a, "b": b, "build": False, "answer": answer, "prompt2": "सही जोड़ चुनिए।" if pick else "सही जोड़ टाइप करिए।"}
    if options:
        d["options"] = options
    return {"id": sid, "phase": "guided", "eis": "iconic", "type": "PV_ADD", "prompt_hi": "संख्याएँ जोड़िए।", "audio": au, "data": d}


slides.append(pv_add("G2", 42, 35, "mcq", [77, 76, 14]))      # deck slide 9 (a second "page 6" - a new page, user 2026-10-28)
slides.append(pv_add("G3", 56, 33, "mcq", [98, 89, 17]))      # deck page 7
slides.append(pv_add("G4", 47, 21, "numpad"))                  # deck page 8


def mental(sid, a, b, answer, options=None):
    """deck pages 9-11: only the sum, written one under the other; the answer in three cards or typed"""
    s = a + b; (at, ao), (bt, bo) = split(a), split(b); low = sid.lower(); pick = answer == "mcq"
    tail = "अब सही जोड़ चुनिए।" if pick else "अब सही जोड़ टाइप करिए।"
    au = {"prompt": ASK_PICK if pick else vo(f"vo_{low}_prompt", f"{a} और {b} को जोड़िए और सही जोड़ टाइप करिए।"),
          "h1": vo(f"vo_{low}_h1", f"ध्यान से देखिए— {ao} इकाई और {bo} इकाई; {at} दहाई और {bt} दहाई। {tail}"),
          "h2": vo("vo_h1_pick" if pick else "vo_h1_type",
                   "ब्लॉक्स को गिनिए और सही जोड़ चुनिए।" if pick else "ब्लॉक्स को गिनिए और सही जोड़ टाइप करिए।"),
          "correct": vo(f"vo_{low}_correct", f"शाबाश! {a} और {b} का जोड़ {s} है।"),
          "reask": ASK_PICK if pick else ASK_TYPE}
    d = {"a": a, "b": b, "answer": answer}
    if options:
        d["options"] = options
    prompt = "संख्याएँ जोड़िए और सही जोड़ चुनिए।" if pick else "संख्याएँ जोड़िए और सही जोड़ टाइप करिए।"
    return {"id": sid, "phase": "practice", "eis": "symbolic", "type": "MENTAL_ADD", "prompt_hi": prompt, "audio": au, "data": d}


slides.append(mental("P1", 61, 20, "mcq", [80, 18, 81]))      # deck page 9
slides.append(mental("P2", 76, 22, "numpad"))                  # deck page 10
slides.append(mental("P3", 37, 60, "numpad"))                  # deck page 11
# deck pages 12-13: deleted

# deck slide 17 - the game: Bibi & Johny, four activities. Swiftee hands the blocks out, then leads the total (user 2026-10-28)
ORD = {1: "पहली", 2: "दूसरी", 3: "तीसरी", 4: "चौथी"}
ACTS = [(25, 12), (13, 55), (31, 45), (42, 46)]
game_audio = {"w1": vo("vo_gm_w1", "फिर से कोशिश कीजिए।"),
              "w2": vo("vo_gm_w2", "ब्लॉक्स ध्यान से गिनिए।"),
              "w3": vo("vo_gm_w3", "देखिए, सही ब्लॉक्स ये हैं।"),
              "next": vo("vo_gm_next", "अब अगली एक्टिविटी शुरू करें!"),
              "add": vo("vo_gm_add", "अब दोनों के ब्लॉक्स को जोड़ते हैं। पहले इकाई जोड़िए।"),
              "tens": vo("vo_gm_tens", "शाबाश! अब दहाइयाँ जोड़िए।"),
              "final": vo("vo_gm_final", "शाबाश! आपने बीबी और जॉनी की सभी एक्टिविटी पूरी कर दीं!")}
for i, (a, b) in enumerate(ACTS, 1):
    s = a + b; (at, ao), (bt, bo), (st, so) = split(a), split(b), split(s)
    game_audio[f"intro{i}"] = vo(f"vo_gm{i}_intro",
        f"बीबी और जॉनी ब्लॉक्स से एक्टिविटी कर रहे हैं। बीबी को {a} और जॉनी को {b} ब्लॉक्स चाहिए। चलिए, उनकी मदद करें!" if i == 1
        else f"अब बीबी को {a} और जॉनी को {b} ब्लॉक्स चाहिए। चलिए, उनकी मदद करें!")
    game_audio[f"build_a{i}"] = vo(f"vo_gm{i}_build_a", f"पहले बीबी के लिए {at} दहाई और {ao} इकाई बनाइए।")
    game_audio[f"ok_a{i}"] = vo(f"vo_gm{i}_ok_a", f"शाबाश! बीबी के {a} ब्लॉक्स तैयार हैं।")
    game_audio[f"build_b{i}"] = vo(f"vo_gm{i}_build_b", f"अब जॉनी के लिए {bt} दहाई और {bo} इकाई बनाइए।")
    game_audio[f"ok_b{i}"] = vo(f"vo_gm{i}_ok_b", f"बहुत बढ़िया! जॉनी के {b} ब्लॉक्स भी तैयार हैं।")
    game_audio[f"ones{i}"] = vo(f"vo_gm{i}_ones", f"{ao} इकाई और {bo} इकाई जोड़िए।")
    game_audio[f"total{i}"] = vo(f"vo_gm{i}_total", f"बहुत बढ़िया! {st} दहाई और {so} इकाई, यानी {s} ब्लॉक्स।")
    game_audio[f"done{i}"] = vo(f"vo_gm{i}_done", f"वाह! {s} ब्लॉक्स से बीबी और जॉनी की {ORD[i]} एक्टिविटी पूरी हो गई!")
slides.append({
    "id": "GAME", "phase": "practice", "eis": "enactive", "type": "ADD_GAME", "prompt_hi": "",
    "audio": game_audio,
    "data": {"no_head": True, "acts": [list(x) for x in ACTS],
             "kids": [{"who": "bibi", "name": "बीबी"}, {"who": "johny", "name": "जॉनी"}]}})

# deck page 14 - the end (no change asked: the draft's own line)
slides.append({"id": "CEL", "phase": "practice", "eis": "enactive", "type": "CELEBRATION", "prompt_hi": "",
               "audio": {"prompt": vo("vo_cel", "शाबाश! अब आप ऊपर-नीचे लिखकर जोड़ सकते हैं। याद रखिए — जोड़ हमेशा इकाई से शुरू होता है।")},
               "data": {}})

# ---- checks: every sum is the sum it claims to be, and none needs regrouping (this skill: WITHOUT regrouping) ----
for s_ in slides:
    d = s_["data"]
    pairs = [(d["a"], d["b"])] if "a" in d else [tuple(x) for x in d.get("acts", [])]
    for a, b in pairs:
        assert a % 10 + b % 10 < 10 and a + b < 100, f"{s_['id']}: {a}+{b} needs regrouping"
    if "options" in d:
        assert d["options"].count(d["a"] + d["b"]) == 1, s_["id"]

phase_n = {}
for s_ in slides:
    phase_n[s_["phase"]] = phase_n.get(s_["phase"], 0) + 1


def clip_len(cid):
    f = os.path.join(ROOT, "assets", "voiceover", cid + ".ogg")
    if not os.path.exists(f):
        return None
    try:
        return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                    capture_output=True, text=True).stdout.strip())
    except Exception:
        return None


def weight(t):
    """a rough spoken length: a number is a word (two digits ~ 7 letters), a pause mark a beat"""
    t = re.sub(r"\d{2,}", "ooooooo", t); t = re.sub(r"\d", "ooo", t)
    return len(re.sub(r"[।,.!?—;]", "oo", t))


def frac(cid, phrase, after=None):
    """where `phrase` starts in clip `cid`, as a share of its length (the 0.28s lead and 0.36s tail of build_vo.py known)"""
    text = VO[cid]; i0 = text.index(after) + len(after) if after else 0
    i = text.index(phrase, i0); dur = clip_len(cid)
    pos = weight(text[:i]) / weight(text)
    if not dur:
        return round(.06 + .88 * pos, 3)
    return round((0.28 + pos * (dur - 0.28 - 0.36)) / dur, 3)


# "शाबाश" only for a first-try right answer (File7, user 2026-10-28): after a wrong one the same line without it
for sl in slides:
    au = sl.get("audio", {})
    if sl["type"] in ("PV_ADD", "MENTAL_ADD") and au.get("correct") and VO[au["correct"]].startswith("शाबाश! ") and sl["data"].get("answer") != "none":
        au["correct_late"] = vo(au["correct"] + "_late", VO[au["correct"]][len("शाबाश! "):])

for sl in slides:
    au, d = sl["audio"], sl["data"]; cues = {}
    if "a" not in d:
        continue
    a, b = d["a"], d["b"]; s = a + b
    (at, ao), (bt, bo), (st, so) = split(a), split(b), split(s)
    if sl["type"] == "STORY_ADD":
        names = {}
        for role, cid in au.items():
            txt = VO[cid]; hits = []
            for word, who in CAST.items():
                i = txt.find(word)
                while i >= 0:
                    hits.append([frac(cid, word, after=txt[:i] if i else None), who]); i = txt.find(word, i + 1)
            if hits:
                names[role] = sorted(hits)
        cues["names"] = names
        if "b" in au:
            cues["b"] = {"a": frac(au["b"], str(a)), "b": frac(au["b"], str(b))}
            cues["a"] = {"bld": frac(au["a"], "ये सारे")}
            cues["ask"] = {"q": frac(au["ask"], "कुल")}
        if "eq" in au:
            cues["eq"] = {"a": frac(au["eq"], str(a)), "op": frac(au["eq"], "जोड़"), "b": frac(au["eq"], str(b)),
                          "eq": frac(au["eq"], "बराबर"), "n": frac(au["eq"], str(s), after="बराबर")}
            cues["tot"] = {"n": frac(au["tot"], str(s))}
    if sl["type"] in ("PV_ADD_DEMO", "PV_ADD"):
        if "r1" in au:
            cues["r1"] = {"t": frac(au["r1"], f"{at} दहाई"), "o": frac(au["r1"], f"{ao} इकाई")}
            cues["r2"] = {"t": frac(au["r2"], f"{bt} दहाई"), "o": frac(au["r2"], f"{bo} इकाई")}
        if "o_sum" in au:
            cues["o_sum"] = {"a": frac(au["o_sum"], f"{ao} इकाई"), "b": frac(au["o_sum"], f"{bo} इकाई", after="और"),
                             "s": frac(au["o_sum"], f"{so} इकाई", after="मिलाकर")}
            cues["t_sum"] = {"a": frac(au["t_sum"], f"{at} दहाई"), "b": frac(au["t_sum"], f"{bt} दहाई", after="और"),
                             "s": frac(au["t_sum"], f"{st} दहाई", after="मिलाकर")}
            cues["total"] = {"t": frac(au["total"], f"{st} दहाइयाँ"), "o": frac(au["total"], f"{so} इकाइयाँ"),
                             "n": frac(au["total"], str(s), after="यानी")}
        for role in ("done", "correct", "correct_late"):
            if role in au:
                t = VO[au[role]]
                cues[role] = {"a": frac(au[role], str(a)), "b": frac(au[role], str(b), after=str(a)),
                              "n": frac(au[role], str(s), after=str(b))}
        if "h2" in au:
            cues["h2"] = {"t": frac(au["h2"], f"{st} दहाइयाँ"), "o": frac(au["h2"], f"{so} इकाइयाँ")}
    if sl["type"] == "MENTAL_ADD":
        cues["h1"] = {"ao": frac(au["h1"], f"{ao} इकाई"), "bo": frac(au["h1"], f"{bo} इकाई", after=f"{ao} इकाई"),
                      "at": frac(au["h1"], f"{at} दहाई"), "bt": frac(au["h1"], f"{bt} दहाई", after=f"{at} दहाई")}
        for role in ("correct", "correct_late"):
            if role in au:
                cues[role] = {"a": frac(au[role], str(a)), "b": frac(au[role], str(b), after=str(a)),
                              "n": frac(au[role], str(s), after=str(b))}
    if cues:
        d["cues"] = cues

# the landing follows the greeting word by word: the times (s) of its words in vo_landing (estimated from the clip's
# length, re-made on every build): glide = "नमस्ते दोस्त", drop = "मैं हूँ स्विफ्टी" (the blocks), a = "आज हम" (23),
# b = "संख्याओं" (+ 14), q = "जोड़ना" (the line and the "?"), cheer = "सीखेंगे", end = the line's end
_ld = clip_len("vo_landing")
def _at(phrase):
    return round(frac("vo_landing", phrase) * _ld, 2) if _ld else None
BEATS = {"glide": 0.28, "drop": _at("मैं हूँ") or 1.3, "a": _at("आज हम") or 2.6, "b": _at("संख्याओं") or 3.0,
         "q": _at("जोड़ना") or 3.7, "cheer": _at("सीखेंगे") or 4.3, "end": round(_ld - 0.36, 2) if _ld else 4.8}

AUDIO_IDS = sorted(set(VO) | {"sfx_celebrate"})
card = {
    "version": "0.2",
    "skill_code": "MTG2A01_L03_S03",
    "lo_code": "MTG2A01_L03",
    "grade": "G2",
    "attribute": "A01",
    "skill_type": "CORE",
    "part_label": "",
    "theme": "toybox",
    "title": {"hi": "संख्याओं का जोड़", "en": "Adds vertically without regrouping"},
    "landing_hero": {"kind": "pv_story", "people": ["akash", "moni"], "build": "addv", "title_look": "wall", "start_at": 0,
                     "a": 23, "b": 14, "beats": BEATS},
    "skill_description_hi": "दो अंकों की दो संख्याओं को ऊपर-नीचे लिखकर (बिना हासिल के) जोड़ता है: पहले इकाई, फिर दहाई।",
    "phase_distribution": phase_n,
    "scaffold_rules": {"nudge_timeout_ms": {"tutorial": 7000, "guided": 7000, "practice": 7000, "independent": 7000},
                       "max_attempts": 3},
    "signals_expected": ["slide_entered", "slide_completed", "pv_build_done", "pv_block_moved", "mcq_correct",
                         "numpad_correct", "game_check", "mastery_score", "lesson_completed"],
    "assets": {"audio_ext": "ogg", "img_ext": "webp",
               "audio": {k: f"assets/voiceover/{k}.ogg" for k in AUDIO_IDS},
               "audio_text": {k: VO[k] for k in sorted(VO)}},
    "slides": slides,
}

# the celebration Swiftie (File7's kit): the lip-sync track measured from OUR celebration line (re-measured on every build)
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("make_lipsync", os.path.join(HERE, "make_lipsync.py")); _ml = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_ml)
_cel = os.path.join(ROOT, "assets", "voiceover", "vo_cel.ogg")
_bits, _ms = _ml.lipsync(_cel) if os.path.exists(_cel) else ("0", 25)
card["end_anim"] = {"base": "assets/celebration/", "vo": "vo_cel",
    "meta": {"cols": 6, "frames": 36, "fw": 329, "fh": 440,
             "shabaash": {"src": "cel_shabaash.webp", "pre": [0, 1, 2, 3, 4, 5], "word": list(range(6, 30)), "post": list(range(30, 36))},
             "talk": {"src": "cel_talk.webp", "open": [0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32]},
             "idle": {"src": "cel_idle.webp", "loop": [0, 1, 2, 3, 4, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]}},
    "track": {"bits": _bits, "step_ms": 25, "ms": _ms}}

with open(os.path.join(ROOT, "card.json"), "w", encoding="utf-8") as f:
    json.dump(card, f, ensure_ascii=False, indent=1)
with open(os.path.join(HERE, "vo_script.json"), "w", encoding="utf-8") as f:
    json.dump({k: VO[k] for k in sorted(VO)}, f, ensure_ascii=False, indent=1)

# embed the card in index.html, and keep the page title and the landing's title in step
idx = os.path.join(ROOT, "index.html")
html = open(idx, encoding="utf-8").read()
blob = json.dumps(card, ensure_ascii=False, indent=1)
html, n = re.subn(r'(<script type="application/json" id="cardData">\n).*?(\n</script>)',
                  lambda m: m.group(1) + blob + m.group(2), html, count=1, flags=re.S)
assert n == 1, "cardData block not found in index.html"
html = re.sub(r"<title>.*?</title>", f"<title>SwiftPAL · {card['skill_code']} · {card['title']['hi']}</title>", html, count=1)
open(idx, "w", encoding="utf-8", newline="\n").write(html)
shutil.copyfile(idx, os.path.join(ROOT, "MTG2A01_L03_S03.html"))
print(f"card: {len(slides)} slides {phase_n} · {len(VO)} VO lines")
