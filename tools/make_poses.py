"""make_poses.py <src_dir> <who> <out_dir> - the first screen's whole-figure poses of one child, as the old ones are made:
char_<who>_full.webp (standing, 640px tall), char_<who>_cheer.webp (both arms up - at the SAME scale, so the child does not
grow or shrink when the pose changes) and the eyes-shut copy of each (_blink, cropped exactly as its open picture).

Sources in <src_dir> (Gemini pictures on a flat magenta-ish background - tools/gen_char_art.py): <who>_full_src.png,
<who>_cheer_src.png (an edit of the full one: same size, same feet), and their _blink_src.png copies.
Each picture is cut to its figure; the bottom edge is the soles (the engine stands it there, centred).
Prints the HANDS entry for app.js PVLanding (where the two raised palms are in the cheer picture, as shares of its width /
height - the lifted red top is held there) and the open / shut overlap (alignment check).
POSES=carry (env; default "full,cheer"): <who>_carry_src.png - both hands held together in front, palms up (the cover's
children carry their blocks on them, user 2026-11-02) - cut at the standing picture's scale; prints PALMS: the middle of
the palms' top as shares of its width / height (the blocks stand there)."""
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

src, who, out = sys.argv[1], sys.argv[2], sys.argv[3]
H_FULL = 640


def key(path):
    """the background = the near-magenta area connected to the edges (flood fill) + near-exact background pockets; the
    outline softened by one pixel; only magenta-tinted outline pixels cleaned (B and R well above G = spill)"""
    a = np.asarray(Image.open(path).convert("RGB")).astype(np.float32)
    border = np.concatenate([a[6:12].reshape(-1, 3), a[-12:-6].reshape(-1, 3), a[:, 6:12].reshape(-1, 3), a[:, -12:-6].reshape(-1, 3)])
    bg = np.median(border, axis=0)
    d = np.sqrt(((a - bg) ** 2).sum(-1))
    near = Image.fromarray(np.where(d < float(os.environ.get("KEY_NEAR", 75)), 255, 0).astype(np.uint8), "L").copy()   # (copy: an array-backed image is read-only)
    h, w = d.shape
    for x in range(6, w - 6, 8):
        for y in (6, h - 7):
            if near.getpixel((x, y)) == 255: ImageDraw.floodfill(near, (x, y), 128)
    for y in range(6, h - 6, 8):
        for x in (6, w - 7):
            if near.getpixel((x, y)) == 255: ImageDraw.floodfill(near, (x, y), 128)
    bgm = np.asarray(near) == 128
    bgm |= d < float(os.environ.get("KEY_POCKET", 50))            # (KEY_NEAR / KEY_POCKET: tighter for a very even background, so white shoes stay)
    bgm[:6] = bgm[-6:] = True; bgm[:, :6] = bgm[:, -6:] = True
    al = np.asarray(Image.fromarray(np.where(bgm, 0, 255).astype(np.uint8), "L").filter(ImageFilter.GaussianBlur(1.0))).astype(np.float32) / 255
    grown = np.asarray(Image.fromarray((bgm * 255).astype(np.uint8), "L").filter(ImageFilter.MaxFilter(7))) > 0
    fg = a.copy(); R, G, B = fg[..., 0], fg[..., 1], fg[..., 2]
    spill = grown & (B > G + 15) & (R > G + 15)
    m = np.minimum(R, B) - G
    R[spill] -= m[spill] * 0.85; B[spill] -= m[spill] * 0.85
    return Image.fromarray(np.dstack([np.clip(fg, 0, 255), al * 255]).astype(np.uint8), "RGBA"), al


def box(al):
    ys, xs = np.where(al > 0.5)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def save(img, bb, scale, path):
    c = img.crop(bb)
    c = c.resize((round(c.width * scale), round(c.height * scale)), Image.LANCZOS)
    c.save(path, "WEBP", quality=90, method=6)
    return c


full, alf = key(os.path.join(src, who + "_full_src.png"))
bf = box(alf); scale = H_FULL / (bf[3] - bf[1])                    # the standing child: 640px tall
report = []
for pose in os.environ.get("POSES", "full,cheer").split(","):
    img, al = (full, alf) if pose == "full" else key(os.path.join(src, "%s_%s_src.png" % (who, pose)))
    bb = bf if pose == "full" else box(al)
    c = save(img, bb, scale, os.path.join(out, "char_%s_%s.webp" % (who, pose)))
    imb, alb = key(os.path.join(src, "%s_%s_blink_src.png" % (who, pose)))
    save(imb, bb, scale, os.path.join(out, "char_%s_%s_blink.webp" % (who, pose)))
    o, s = al > .5, alb > .5
    report.append("%s %dx%d, open/shut overlap %.3f" % (pose, c.width, c.height, (o & s).sum() / max((o | s).sum(), 1)))
    if pose == "cheer":
        # the raised palms: the figure's top in the outer thirds (the arms), the palm a little below the fingertips
        A = np.asarray(c)[..., 3] > 128; Hc, Wc = A.shape; hands = []
        for x0, x1 in ((0, int(Wc * .34)), (int(Wc * .66), Wc)):
            ys, xs = np.where(A[:, x0:x1]); top = ys.min()
            sel = ys < top + Hc * .07                                   # the fingers and the palm
            hands.append([round(float((xs[sel] + x0).mean()) / Wc, 3), round(float(top + Hc * .06) / Hc, 3)])
        report.append("HANDS %s: %s" % (who, hands))
    if pose == "carry":
        # the palms: skin (warm, light) in the middle columns, between the chest and the hips - their top edge
        a = np.asarray(c).astype(int); Hc, Wc = a.shape[:2]; R, G, B = a[..., 0], a[..., 1], a[..., 2]
        skin = (a[..., 3] > 128) & (R > 190) & (R > G + 15) & (G > B + 10) & (B > 110)   # (B > 110: not the orange / yellow clothes)
        x0, x1, y0, y1 = int(Wc * .38), int(Wc * .62), int(Hc * .42), int(Hc * .66)   # (below the neck)
        sk = skin[y0:y1, x0:x1]; top = int(np.argmax(sk.sum(1) >= 10))      # (a row of hand, not a drawstring's sliver)
        ys, xs = np.where(sk[top:top + 12])
        report.append("PALMS %s: [%.3f, %.3f]" % (who, (xs.mean() + x0) / Wc, (top + y0) / Hc))
print(who, "scale %.3f;" % scale, "; ".join(report))
