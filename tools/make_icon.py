"""Bulgarca Rehber ikonu: Bulgaristan ve Türkiye bayrakları, iç içe iki daire."""
from PIL import Image, ImageDraw, ImageFilter
import math, os
S = 1024; SS = 4; N = S * SS
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets')

def flag_bg(d):
    im = Image.new('RGBA', (d, d)); dr = ImageDraw.Draw(im)
    for i, c in enumerate([(255, 255, 255), (0, 150, 110), (214, 38, 18)]):
        dr.rectangle([0, i * d / 3, d, (i + 1) * d / 3], fill=c)
    return im

def flag_tr(d):
    im = Image.new('RGBA', (d, d), (227, 10, 23)); dr = ImageDraw.Draw(im)
    G = d * 0.95  # bayrak yüksekliği ölçeği
    cx, cy = d * 0.42, d / 2
    r1 = G * 0.25; dr.ellipse([cx - r1, cy - r1, cx + r1, cy + r1], fill='white')
    r2 = G * 0.20; ox = cx + G * 0.0625; dr.ellipse([ox - r2, cy - r2, ox + r2, cy + r2], fill=(227, 10, 23))
    # yıldız
    sx = cx + G * 0.0625 + G * 0.0625 * 1.15 + G * 0.03; R = G * 0.125; r = R * 0.382
    pts = []
    for k in range(10):
        a = math.pi + k * math.pi / 5  # bir uç sola baksın (hilale)
        rr = R if k % 2 == 0 else r
        pts.append((sx + rr * math.cos(a), cy + rr * math.sin(a)))
    dr.polygon(pts, fill='white')
    return im

def disc(img, d, ring):
    mask = Image.new('L', (d, d), 0); ImageDraw.Draw(mask).ellipse([0, 0, d - 1, d - 1], fill=255)
    out = Image.new('RGBA', (d + 2 * ring, d + 2 * ring), (0, 0, 0, 0))
    ImageDraw.Draw(out).ellipse([0, 0, d + 2 * ring - 1, d + 2 * ring - 1], fill=(255, 255, 255, 255))
    out.paste(img, (ring, ring), mask)
    return out

def make(bg=True, scale=1.0):
    im = Image.new('RGBA', (N, N), (0, 0, 0, 0))
    if bg:
        grad = Image.new('RGBA', (N, N))
        gd = ImageDraw.Draw(grad)
        for y in range(N):
            t = y / N
            gd.line([(0, y), (N, y)], fill=(int(22 + 10 * t), int(36 + 8 * t), int(48 + 14 * t), 255))
        m = Image.new('L', (N, N), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, N - 1, N - 1], radius=int(N * 0.22), fill=255)
        im.paste(grad, (0, 0), m)
    d = int(N * 0.50 * scale); ring = int(N * 0.022 * scale)
    a = disc(flag_bg(d), d, ring); b = disc(flag_tr(d), d, ring)
    sh = Image.new('RGBA', a.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([0, 0, a.size[0] - 1, a.size[1] - 1], fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(N / 60))
    c = N / 2; off = N * 0.13 * scale
    pa = (int(c - off - a.size[0] / 2), int(c - off - a.size[1] / 2))
    pb = (int(c + off - b.size[0] / 2), int(c + off - b.size[1] / 2))
    im.alpha_composite(sh, (pa[0], pa[1] + int(N * 0.015))); im.alpha_composite(a, pa)
    im.alpha_composite(sh, (pb[0], pb[1] + int(N * 0.015))); im.alpha_composite(b, pb)
    return im.resize((S, S), Image.LANCZOS)

full = make(True)
full.save(os.path.join(OUT, 'icon_rounded.png'))
flat = Image.new('RGB', (S, S), (26, 40, 54)); flat.paste(make(True), (0, 0), make(True))
# kare (launcher için arka plan dolu)
sq = Image.new('RGBA', (S, S), (26, 40, 54, 255)); sq.alpha_composite(make(False))
sq.convert('RGB').save(os.path.join(OUT, 'icon.png'))
make(False, 0.78).save(os.path.join(OUT, 'icon_fg.png'))
make(True).resize((180, 180), Image.LANCZOS).save(os.path.join(OUT, 'icon_180.png'))
print('ok')
