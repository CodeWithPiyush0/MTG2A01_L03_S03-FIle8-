"""make_walk.py <src_dir> <who> <out_dir> - the game's side-view walking child, as a cut-out puppet (user 2026-10-30: "the
walking does not feel good"): one side-view picture in a walking stride (<who>_side_src.png on a flat background, facing
right, straight legs apart in an upside-down V - tools/gen_image.py) becomes char_<who>_side.webp, and this prints the
numbers app.js needs to swing its two legs from the hip (the card's kids[].side):

  h     the picture's height as a share of the standing picture's (640px): the side child stands as tall as the front one
  ar    its width / height
  cut   where the body ends (the crotch), as a share of the height - below it are only the legs
  split the line between the two legs (x share): left of it the back leg, right of it the front leg
  px/py the hip the legs turn on (shares)
  a     the angle between the two legs (degrees): each leg swings through it, so they change places every step
  bob   how far the body rises (share of the height) when the legs pass each other (a straight leg is longest upright)

The scale: the standing height a straight-legged child would have (head to hip + one leg) is set to 640px, as the front
picture's. Stray specks are dropped (pieces under 1% of the figure)."""
import json, math, os, sys
import numpy as np
from PIL import Image
from scipy import ndimage

src, who, out = sys.argv[1], sys.argv[2], sys.argv[3]


def shadow(a, bgv):
    """the floor shadow: grey (unsaturated), darker than the background, in the bottom eighth - and in each column only
    BELOW the lowest bright or coloured pixel there (a white shoe's grey shading and outline stay)"""
    h = a.shape[0]; mx, mn = a[..., :3].max(-1), a[..., :3].min(-1); sat = (mx - mn) / np.maximum(mx, 1)
    grey = (sat < .07) & (mx < bgv - 2) & (mx > 40) & (a[..., 3] > 0)
    solid = (a[..., 3] > 128) & ((sat > .12) | (mx > bgv + 18))
    ys = np.arange(h)[:, None]
    low = np.where(solid.any(0), h - 1 - np.argmax(solid[::-1], 0), -1)  # the lowest solid pixel per column
    return grey & (ys > h * .85) & (ys > low[None, :])

H = 640
sys.argv = sys.argv[:1] + ["", "", ""]                                # (make_poses runs on import: only its helpers are used)
ns = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "make_poses.py"), encoding="utf8").read().split("full, alf = key(")[0], ns)
img, al = ns["key"](os.path.join(src, who + "_side_src.png"))
# the soft floor shadow the picture may have under the feet (grey, a little darker than the background, in the bottom
# eighth) is cleared first - a thin line of it would join the two feet
rgb = np.asarray(Image.open(os.path.join(src, who + "_side_src.png")).convert("RGB")).astype(np.float32)
bgv = float(np.median(np.concatenate([rgb[:8].reshape(-1, 3), rgb[:, :8].reshape(-1, 3), rgb[:, -8:].reshape(-1, 3)])))
a = np.asarray(img).astype(np.float32)
a[..., 3][shadow(a, bgv)] = 0; img = Image.fromarray(a.astype(np.uint8), "RGBA")
m = a[..., 3] > 128
low = np.arange(m.shape[0])[:, None] > m.shape[0] * .85
m = np.where(low, ndimage.binary_opening(m, iterations=2), m)       # (and any hair-thin remains of it)
lab, n = ndimage.label(m)
if n > 1:                                                             # (specks go; a shoe drawn apart from its leg stays)
    sizes = ndimage.sum(m, lab, range(1, n + 1))
    m = np.isin(lab, [i + 1 for i, v in enumerate(sizes) if v > sizes.max() * .01])
    a = np.asarray(img).copy(); a[..., 3][~ndimage.binary_dilation(m, iterations=2)] = 0; img = Image.fromarray(a, "RGBA")
ys, xs = np.where(m); top, bot, left, right = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1


def runs(row):
    x = np.where(row)[0]
    if not len(x): return []
    br = np.where(np.diff(x) > 2)[0]
    return [(x[s], x[e]) for s, e in zip(np.r_[0, br + 1], np.r_[br, len(x) - 1]) if x[e] - x[s] > 3]


# the crotch: the top of the longest unbroken run of rows (in the lower half) where the legs are two (a foot raised on its
# toes makes the very bottom rows hold only one)
crotch, gap, best, cur = None, None, 0, []
for y in range(bot - 1, top + int((bot - top) * .45), -1):
    r = runs(m[y])
    if len(r) >= 2: cur.append((y, (r[0][1] + r[1][0]) / 2))
    else:
        if len(cur) > best: best, crotch, gap = len(cur), cur[-1][0], cur[-1][1]
        cur = []
if len(cur) > best: crotch, gap = cur[-1][0], cur[-1][1]
assert crotch is not None, "no gap between the legs"
hip_y = crotch - (bot - top) * .035                                   # the hip: a little above the crotch
# the feet: the lowest pixels left and right of the gap
feet = []
for side in (m[:, :int(gap)], m[:, int(gap):]):
    yy, xx = np.where(side); lo = yy > yy.max() - 12
    feet.append((float(xx[lo].mean()) + (0 if not feet else int(gap)), float(yy.max())))
ang = [math.degrees(math.atan2(fx - gap, fy - hip_y)) for fx, fy in feet]   # (back leg negative, front positive)
leg = float(np.mean([math.hypot(fx - gap, fy - hip_y) for fx, fy in feet]))
stand = (hip_y - top) + leg
scale = H / stand
fig = img.crop((left, top, right, bot))
fig = fig.resize((round(fig.width * scale), round(fig.height * scale)), Image.LANCZOS)
fig.save(os.path.join(out, "char_%s_side.webp" % who), "WEBP", quality=90, method=6)
w, h = right - left, bot - top
a = abs(ang[1] - ang[0])
side = {"h": round(fig.height / H, 4), "ar": round(fig.width / fig.height, 4), "cut": round((crotch - top) / h, 4), "split": round((gap - left) / w, 4),
        "px": round((gap - left) / w, 4), "py": round((hip_y - top) / h, 4), "a": round(a, 1),
        "bob": round(leg * (1 - math.cos(math.radians(a / 2))) / h, 4)}
print(who, fig.size, json.dumps(side))
