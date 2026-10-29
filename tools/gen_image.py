"""gen_image.py <out.png> <prompt> [--ref <img>]... [--aspect 16:9] - Gemini image generation (optionally from reference images).

Key: GEMINI_KEY from the environment (the .env's GKEY: set -a; . ./.env; set +a; export GEMINI_KEY=$GKEY).
"""
import base64, json, mimetypes, os, sys, urllib.request, urllib.error

args = sys.argv[1:]
out, prompt = args[0], args[1]
refs, aspect, model = [], None, "gemini-2.5-flash-image"
i = 2
while i < len(args):
    if args[i] == "--ref": refs.append(args[i + 1]); i += 2
    elif args[i] == "--aspect": aspect = args[i + 1]; i += 2
    elif args[i] == "--model": model = args[i + 1]; i += 2
    else: sys.exit("unknown arg " + args[i])
key = os.environ.get("GEMINI_KEY") or os.environ.get("GKEY")
if not key: sys.exit("set GEMINI_KEY")
parts = [{"inlineData": {"mimeType": mimetypes.guess_type(r)[0] or "image/png", "data": base64.b64encode(open(r, "rb").read()).decode()}} for r in refs]
parts.append({"text": prompt})
gc = {"responseModalities": ["IMAGE", "TEXT"]}
if aspect: gc["imageConfig"] = {"aspectRatio": aspect}
body = {"contents": [{"parts": parts}], "generationConfig": gc}
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
try:
    r = json.loads(urllib.request.urlopen(urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json"}), timeout=240).read())
except urllib.error.HTTPError as e:
    sys.exit("HTTP %d %s" % (e.code, e.read()[:300]))
for c in r.get("candidates", []):
    for p in c.get("content", {}).get("parts", []):
        if "inlineData" in p:
            open(out, "wb").write(base64.b64decode(p["inlineData"]["data"])); print("ok", out); sys.exit(0)
sys.exit("no image: " + json.dumps(r)[:400])
