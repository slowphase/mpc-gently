"""Vector diagrams for MPC, Gently. All drawn from verified layouts; concept
diagrams are labelled as diagrams, never as screenshots."""

INK = "#2B2A28"
ORANGE = "#C4572A"
AMBER = "#E2A33B"
GREY = "#8C847A"
LIGHT = "#E6DDCB"
PAPER = "#F7F2E7"
CREAM = "#FBF7EE"
FONT = "Archivo, sans-serif"

# ---------------------------------------------------------------------------
# Top-panel schematic. Coordinates follow the official Akai top-panel diagram
# (offset so the body starts at 0,0). Simplified: not to scale in detail.
# ---------------------------------------------------------------------------
OX, OY = 188, 112

def R(x0, y0, x1, y1):
    return (x0 - OX, y0 - OY, x1 - x0, y1 - y0)

BUTTONS = {
    "B1": (R(463, 139, 509, 161), "B1"),
    "B2": (R(524, 139, 570, 161), "B2"),
    "B3": (R(585, 139, 631, 161), "B3"),
    "SAMPLE": (R(220, 366, 277, 396), "SAMPLE"),
    "SEQ": (R(292, 366, 348, 396), "SEQ"),
    "PADFX": (R(220, 411, 277, 442), "PAD FX"),
    "KNOBFX": (R(292, 411, 348, 442), "KNOB FX"),
    "SHIFT": (R(218, 470, 279, 520), "SHIFT"),
    "PADBANK": (R(292, 472, 348, 504), "PAD BANK"),
    "ERASE": (R(220, 773, 277, 803), "ERASE"),
    "NOTEREPEAT": (R(292, 773, 348, 803), "NOTE RPT"),
    "CHOP": (R(746, 366, 802, 397), "CHOP"),
    "MUTE": (R(817, 366, 873, 397), "MUTE"),
    "LOOP": (R(746, 411, 802, 442), "LOOP"),
    "16LEVELS": (R(817, 411, 873, 442), "16 LEV"),
    "SAMPLESELECT": (R(746, 473, 802, 504), "SMP SEL"),
    "TAPTEMPO": (R(817, 473, 873, 504), "TAP"),
    "MINUS": (R(746, 650, 802, 680), "−"),
    "PLUS": (R(817, 650, 873, 680), "+"),
    "SAMPLERECORD": (R(746, 710, 802, 750), "SMP REC"),
    "SEQRECORD": (R(817, 710, 873, 750), "SEQ REC"),
    "STOP": (R(746, 765, 802, 805), "STOP"),
    "PLAY": (R(817, 765, 873, 805), "PLAY"),
}
KNOBS = {
    "MAINVOL": ((276 - OX, 234 - OY), 30, "VOLUME"),
    "K1": ((412 - OX, 410 - OY), 30, "K1"),
    "K2": ((547 - OX, 410 - OY), 30, "K2"),
    "K3": ((673 - OX, 410 - OY), 30, "K3"),
    "ENCODER": ((818 - OX, 605 - OY), 44, "ENCODER"),
}
PAD_X = [375, 465, 555, 645]
PAD_Y = [732, 642, 553, 462]  # row of pads 1-4 is the bottom row


def pad_rect(n):
    i = n - 1
    col, row = i % 4, i // 4
    return (PAD_X[col] - OX, PAD_Y[row] - OY, 76, 76)


def panel(highlight=(), pads=(), width="100%", caption=True, dim_unlit=True,
          pad_labels=None, small_labels=True):
    """Return an SVG of the top panel. highlight: control keys to colour.
    pads: pad numbers to colour. pad_labels: {n: text} drawn on pads."""
    hl = set(highlight)
    pads = set(pads)
    pad_labels = pad_labels or {}
    W, H = 905 - OX + 12, 955 - OY + 12
    o = [f'<svg class="panel" xmlns="http://www.w3.org/2000/svg" viewBox="-6 -6 {W} {H}" width="{width}">']
    # body
    o.append(f'<rect x="0" y="0" width="{905-OX}" height="{955-OY}" rx="34" fill="{CREAM}" stroke="{INK}" stroke-width="3"/>')
    # top band
    o.append(f'<rect x="12" y="12" width="{905-OX-24}" height="{335-OY-12}" rx="22" fill="{INK}"/>')
    # display
    dx, dy, dw, dh = R(457, 180, 640, 318)
    o.append(f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" rx="6" fill="#1a1918" stroke="{GREY}" stroke-width="2"/>')
    o.append(f'<text x="{dx+dw/2}" y="{dy+dh/2+6}" text-anchor="middle" font-family="{FONT}" font-size="17" letter-spacing="2" fill="{GREY}">SCREEN</text>')
    if "SCREEN" in hl:
        o.append(f'<rect x="{dx-4}" y="{dy-4}" width="{dw+8}" height="{dh+8}" rx="8" fill="none" stroke="{ORANGE}" stroke-width="6"/>')
    # meters
    for mx in (672, 690):
        for k in range(5):
            o.append(f'<rect x="{mx-OX}" y="{185-OY+k*27}" width="13" height="20" rx="2" fill="#4a4743"/>')
    # speaker
    sx, sy, sw, sh = R(735, 182, 862, 305)
    o.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="12" fill="#3a3835"/>')
    for gy in range(int(sy) + 12, int(sy + sh) - 6, 12):
        for gx in range(int(sx) + 12, int(sx + sw) - 6, 12):
            o.append(f'<circle cx="{gx}" cy="{gy}" r="2.2" fill="#55524d"/>')
    # bank letters
    o.append(f'<text x="{358-OX}" y="{232-OY}" font-family="{FONT}" font-size="15" fill="{GREY}" letter-spacing="3">EFGH</text>')
    o.append(f'<text x="{358-OX}" y="{256-OY}" font-family="{FONT}" font-size="15" fill="{GREY}" letter-spacing="3">ABCD</text>')
    if "BANKLEDS" in hl:
        o.append(f'<rect x="{350-OX}" y="{212-OY}" width="62" height="52" rx="6" fill="none" stroke="{ORANGE}" stroke-width="5"/>')
    # fader
    fx, fy, fw, fh = R(262, 545, 326, 735)
    o.append(f'<rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="8" fill="{PAPER}" stroke="{INK}" stroke-width="2.5"/>')
    o.append(f'<rect x="{fx+fw/2-6}" y="{fy+14}" width="12" height="{fh-28}" rx="5" fill="{INK}"/>')
    fill = ORANGE if "FADER" in hl else "#d9d1c1"
    o.append(f'<rect x="{fx+8}" y="{fy+70}" width="{fw-16}" height="34" rx="5" fill="{fill}" stroke="{INK}" stroke-width="2.5"/>')
    o.append(f'<rect x="{323-OX}" y="{632-OY}" width="16" height="10" rx="2" fill="#9b7fb4"/>')
    # mic
    o.append(f'<g transform="translate({869-OX},{548-OY})" fill="{ORANGE if "MIC" in hl else INK}">'
             '<circle cx="-5" cy="-9" r="3.2"/><circle cx="5" cy="-9" r="3.2"/><circle cx="-5" cy="0" r="3.2"/><circle cx="5" cy="0" r="3.2"/>'
             '</g>')
    if "MIC" in hl:
        o.append(f'<circle cx="{869-OX}" cy="{544-OY}" r="20" fill="none" stroke="{ORANGE}" stroke-width="4"/>')
    # pad well
    o.append(f'<rect x="{366-OX}" y="{453-OY}" width="{737-366}" height="{825-453}" rx="6" fill="#2f3542"/>')
    for n in range(1, 17):
        x, y, w, h = pad_rect(n)
        on = n in pads
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{ORANGE if on else "#9a968e"}" stroke="{INK if on else "#77736b"}" stroke-width="{3 if on else 1.5}"/>')
        lab = pad_labels.get(n, str(n))
        fs = 28 if len(lab) <= 3 else (18 if len(lab) <= 5 else 14)
        col = "#fff" if on else "#f1ece2"
        o.append(f'<text x="{x+w/2}" y="{y+h/2+fs*0.36}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{fs}" fill="{col}">{lab}</text>')
    # labels for regions
    o.append(f'<text x="{284-OX}" y="{358-OY}" text-anchor="middle" font-family="{FONT}" font-size="12" letter-spacing="2" fill="{GREY}">MODE</text>')
    o.append(f'<text x="{810-OX}" y="{358-OY}" text-anchor="middle" font-family="{FONT}" font-size="12" letter-spacing="2" fill="{GREY}">PAD PLAY</text>')
    # buttons
    for key, ((x, y, w, h), lab) in BUTTONS.items():
        on = key in hl
        top = key in ("B1", "B2", "B3")
        base = "#5b5852" if top else ("#e9e3d6")
        if key in ("CHOP", "MUTE", "LOOP", "16LEVELS") and not on:
            base = "#b9c4c9"
        if key in ("PADFX", "KNOBFX") and not on:
            base = "#e3c7b4"
        fillc = ORANGE if on else base
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fillc}" stroke="{INK}" stroke-width="{3 if on else 1.8}"/>')
        if key in ("SAMPLERECORD", "SEQRECORD"):
            o.append(f'<rect x="{x+8}" y="{y+h-11}" width="{w-16}" height="5" fill="#b8322a"/>')
        if key in ("STOP", "PLAY"):
            o.append(f'<rect x="{x+8}" y="{y+h-11}" width="{w-16}" height="5" fill="{"#5aa356" if key=="PLAY" else "#ddd"}"/>')
        tcol = "#fff" if on else (CREAM if top else INK)
        fs = 14 if len(lab) > 5 else 16
        if lab in ("−", "+"):
            fs = 22
        o.append(f'<text x="{x+w/2}" y="{y+h/2+fs*0.33 - (3 if key in ("SAMPLERECORD","SEQRECORD","STOP","PLAY") else 0)}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="{fs}" fill="{tcol}">{lab}</text>')
    # knobs
    for key, ((cx, cy), r, lab) in KNOBS.items():
        on = key in hl
        if key == "ENCODER":
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ORANGE if on else "#efe9dc"}" stroke="{INK}" stroke-width="{3.5 if on else 2.5}"/>')
            o.append(f'<circle cx="{cx}" cy="{cy}" r="{r-9}" fill="none" stroke="{INK}" stroke-opacity=".35" stroke-width="1.5" stroke-dasharray="3 4"/>')
            o.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="14" fill="{"#fff" if on else INK}">ENCODER</text>')
            continue
        dark = key == "MAINVOL"
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r+9}" fill="none" stroke="{CREAM if dark else INK}" stroke-opacity=".5" stroke-width="2"/>')
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ORANGE if on else ("#6b6862" if dark else "#5b5852")}" stroke="{INK}" stroke-width="2.5"/>')
        o.append(f'<line x1="{cx}" y1="{cy-r+4}" x2="{cx}" y2="{cy-6}" stroke="#fff" stroke-width="5" stroke-linecap="round"/>')
        lc = CREAM if dark else INK
        o.append(f'<text x="{cx}" y="{cy+r+30}" text-anchor="middle" font-family="{FONT}" font-weight="700" font-size="17" fill="{ORANGE if on else lc}">{lab}</text>')
    # palm rest
    px, py, pw, ph = R(200, 838, 893, 945)
    o.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#cfc8ba"/>')
    o.append(f'<text x="{px+pw/2}" y="{py+ph/2+5}" text-anchor="middle" font-family="{FONT}" font-size="13" letter-spacing="3" fill="{GREY}">SCHEMATIC · NOT TO SCALE</text>')
    o.append('</svg>')
    return "".join(o)


# ---------------------------------------------------------------------------
# Concept diagrams
# ---------------------------------------------------------------------------

def _svg(w, h, body, cls="fig"):
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" font-family="{FONT}">{body}</svg>'


def t(x, y, s, size=13, fill=INK, anchor="start", weight=400, ls=0, italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" letter-spacing="{ls}"{st}>{s}</text>'


def beats_bars():
    b = []
    W = 600
    x0, x1 = 20, 580
    bw = (x1 - x0) / 2
    for bar in range(2):
        bx = x0 + bar * bw
        b.append(f'<rect x="{bx+3}" y="40" width="{bw-6}" height="70" rx="8" fill="{LIGHT}"/>')
        b.append(t(bx + 14, 30, f"BAR {bar+1}", 12, GREY, weight=700, ls=2))
        for k in range(4):
            cx = bx + bw / 8 + k * bw / 4
            r = 20 if k == 0 else 13
            col = ORANGE if k == 0 else INK
            b.append(f'<circle cx="{cx}" cy="75" r="{r}" fill="{col}"/>')
            b.append(t(cx, 81 if k else 82, str(k + 1), 15 if k else 18, "#fff", "middle", 700))
            b.append(t(cx, 135, ["one", "two", "three", "four"][k], 13, GREY, "middle", italic=True))
    b.append(f'<line x1="{x0}" y1="160" x2="{x1}" y2="160" stroke="{INK}" stroke-width="1.5"/>')
    b.append(f'<polygon points="{x1},160 {x1-9},155 {x1-9},165" fill="{INK}"/>')
    b.append(t(x0, 182, "time →   at 84 BPM, each beat lasts about 0.7 seconds; one bar of four beats lasts about 2.9 seconds", 12, INK))
    return _svg(W, 192, "".join(b))


def drum_grid(rows, steps=16, labels=True, highlight_beats=True, title=None, W=600):
    """rows: list of (name, set_of_step_indices, colour)."""
    b = []
    lw = 70
    gx0 = lw + 10
    gw = W - gx0 - 10
    cw = gw / steps
    rh = 34
    top = 30 if labels else 8
    if labels:
        for s in range(steps):
            per_beat = steps // 4 if steps <= 16 else steps // 8
            if steps == 16:
                lab = ["1", "e", "+", "a"][s % 4]
                if s % 4 == 0:
                    lab = str(s // 4 + 1)
            elif steps == 8:
                lab = str(s // 2 + 1) if s % 2 == 0 else "+"
            else:
                lab = ""
            bold = 700 if (lab.isdigit()) else 400
            col = INK if lab.isdigit() else GREY
            b.append(t(gx0 + s * cw + cw / 2, 20, lab, 12, col, "middle", bold))
    for r, (name, hits, col) in enumerate(rows):
        y = top + r * (rh + 6)
        b.append(t(lw, y + rh / 2 + 5, name, 13, INK, "end", 700))
        for s in range(steps):
            beat_start = (s % (steps // 4) == 0) if steps in (8, 16) else False
            bg = LIGHT if (s // (steps // 4)) % 2 == 0 else "#efe8da"
            b.append(f'<rect x="{gx0+s*cw+1.5}" y="{y}" width="{cw-3}" height="{rh}" rx="4" fill="{bg}"/>')
            if s in hits:
                b.append(f'<rect x="{gx0+s*cw+4}" y="{y+4}" width="{cw-8}" height="{rh-8}" rx="3" fill="{col}"/>')
    H = top + len(rows) * (rh + 6) + 4
    return _svg(W, H, "".join(b))


def quantise_fig():
    b = []
    W = 600
    def lane(y, label, xs, snapped):
        out = [t(10, y + 6, label, 13, INK, weight=700)]
        x0, x1 = 120, 590
        out.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{GREY}" stroke-width="1.5"/>')
        for k in range(9):
            gx = x0 + k * (x1 - x0) / 8
            out.append(f'<line x1="{gx}" y1="{y-16}" x2="{gx}" y2="{y+16}" stroke="{GREY}" stroke-width="{2 if k%2==0 else 1}" stroke-dasharray="{"" if k%2==0 else "3 3"}"/>')
        for x in xs:
            out.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{ORANGE if snapped else INK}"/>')
        return "".join(out)
    played = [128, 247, 352, 476]
    grid = [120 + 0 * 58.75, 120 + 2 * 58.75, 120 + 4 * 58.75, 120 + 6 * 58.75]
    b.append(lane(40, "As played", played, False))
    for p, g in zip(played, grid):
        b.append(f'<line x1="{p}" y1="52" x2="{g}" y2="98" stroke="{ORANGE}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    b.append(lane(110, "Quantised", grid, True))
    b.append(t(120, 150, "Each note moves to the nearest line of the grid. The grid spacing is the Q value.", 12, INK))
    return _svg(W, 160, "".join(b))


def waveform_fig(markers=True, title_left="loud", W=600):
    import math, random
    random.seed(4)
    b = []
    x0, x1, mid = 30, 580, 85
    pts_top, pts_bot = [], []
    n = 220
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        p = i / n
        env = (min(1, p / 0.03)) * math.exp(-p * 3.2) * 0.95 + 0.04
        a = env * 62 * (0.75 + 0.25 * random.random())
        pts_top.append((x, mid - a))
        pts_bot.append((x, mid + a))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts_top) + " L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in reversed(pts_bot)) + " Z"
    b.append(f'<line x1="{x0}" y1="{mid}" x2="{x1}" y2="{mid}" stroke="{GREY}" stroke-width="1"/>')
    b.append(f'<path d="{d}" fill="{INK}" opacity=".85"/>')
    if markers:
        for x, lab, col in ((105, "START", ORANGE), (420, "END", ORANGE)):
            b.append(f'<line x1="{x}" y1="12" x2="{x}" y2="160" stroke="{col}" stroke-width="2.5"/>')
            b.append(f'<rect x="{x-26}" y="0" width="52" height="18" rx="3" fill="{col}"/>')
            b.append(t(x, 13, lab, 11, "#fff", "middle", 700, 1))
        b.append(f'<rect x="{x0}" y="10" width="75" height="150" fill="{PAPER}" opacity=".72"/>')
        b.append(f'<rect x="420" y="10" width="{x1-420}" height="150" fill="{PAPER}" opacity=".72"/>')
        b.append(t(262, 182, "only the part between START and END plays", 12, INK, "middle", italic=True))
    b.append(t(x0 + 6, 175 if not markers else 200, "", 1))
    return _svg(W, 192 if markers else 170, "".join(b))


def waveform_explainer():
    import math
    b = []
    W = 600
    # zoomed wave on left: loud vs quiet
    def wave(x0, x1, y, amp, cycles, col):
        pts = []
        for i in range(201):
            p = i / 200
            pts.append((x0 + (x1 - x0) * p, y - amp * math.sin(p * cycles * 2 * math.pi)))
        return f'<path d="M{" L".join(f"{x:.1f},{yy:.1f}" for x, yy in pts)}" fill="none" stroke="{col}" stroke-width="3"/>'
    b.append(f'<line x1="20" y1="60" x2="280" y2="60" stroke="{GREY}"/>')
    b.append(wave(20, 280, 60, 42, 3, INK))
    b.append(t(150, 125, "tall wave = loud", 13, INK, "middle", 700))
    b.append(f'<line x1="320" y1="60" x2="580" y2="60" stroke="{GREY}"/>')
    b.append(wave(320, 580, 60, 14, 3, INK))
    b.append(t(450, 125, "short wave = quiet", 13, INK, "middle", 700))
    b.append(f'<line x1="20" y1="185" x2="280" y2="185" stroke="{GREY}"/>')
    b.append(wave(20, 280, 185, 30, 2, ORANGE))
    b.append(t(150, 245, "slow wiggles = low pitch", 13, INK, "middle", 700))
    b.append(f'<line x1="320" y1="185" x2="580" y2="185" stroke="{GREY}"/>')
    b.append(wave(320, 580, 185, 30, 7, ORANGE))
    b.append(t(450, 245, "fast wiggles = high pitch", 13, INK, "middle", 700))
    return _svg(W, 255, "".join(b))


def envelope_fig():
    b = []
    W = 600
    panels = [
        ("PLUCK", "Attack 0, short Decay", [(0, 0), (0.02, 1), (0.35, 0), (1, 0)]),
        ("DRUM HIT", "the natural shape", [(0, 0), (0.01, 1), (0.6, 0), (1, 0)]),
        ("SWELL", "slow Attack, long Decay", [(0, 0), (0.55, 1), (1, 0.15)]),
    ]
    pw = 180
    for i, (name, sub, pts) in enumerate(panels):
        x0 = 15 + i * (pw + 15)
        y0, h = 30, 100
        b.append(f'<rect x="{x0}" y="{y0-8}" width="{pw}" height="{h+16}" rx="8" fill="{LIGHT}"/>')
        d = "M" + " L".join(f"{x0+10+p[0]*(pw-20):.1f},{y0+h-p[1]*h+0:.1f}" for p in pts)
        fillpath = d + f" L{x0+10+(pw-20):.1f},{y0+h} L{x0+10},{y0+h} Z"
        b.append(f'<path d="{fillpath}" fill="{ORANGE}" opacity=".18"/>')
        b.append(f'<path d="{d}" fill="none" stroke="{ORANGE}" stroke-width="3.5" stroke-linejoin="round"/>')
        b.append(t(x0 + pw / 2, 162, name, 13, INK, "middle", 700, 1))
        b.append(t(x0 + pw / 2, 180, sub, 12, GREY, "middle", italic=True))
    b.append(t(15, 14, "VOLUME", 10, GREY, weight=700, ls=2))
    b.append(t(585, 14, "TIME →", 10, GREY, "end", 700, 2))
    return _svg(W, 190, "".join(b))


def filter_fig():
    b = []
    W = 600
    def curve(x0, kind):
        out = []
        out.append(f'<rect x="{x0}" y="10" width="270" height="130" rx="8" fill="{LIGHT}"/>')
        if kind == "lp":
            d = f"M{x0+12},50 L{x0+120},50 C{x0+150},50 {x0+150},28 {x0+162},38 C{x0+180},55 {x0+200},120 {x0+258},128"
            cut = x0 + 160
        else:
            d = f"M{x0+12},128 C{x0+70},120 {x0+90},55 {x0+108},38 C{x0+120},28 {x0+120},50 {x0+150},50 L{x0+258},50"
            cut = x0 + 110
        out.append(f'<path d="{d}" fill="none" stroke="{ORANGE}" stroke-width="3.5"/>')
        out.append(f'<line x1="{cut}" y1="18" x2="{cut}" y2="136" stroke="{INK}" stroke-dasharray="4 3"/>')
        out.append(t(cut, 155, "CUTOFF", 11, INK, "middle", 700, 1))
        out.append(t(x0 + 14, 135, "low", 11, GREY))
        out.append(t(x0 + 256, 135, "high", 11, GREY, "end"))
        return "".join(out)
    b.append(curve(15, "lp"))
    b.append(curve(315, "hp"))
    b.append(t(150, 178, "LOW-PASS (LPF): lows pass, highs fade", 12, INK, "middle", 700))
    b.append(t(450, 178, "HIGH-PASS (HPF): highs pass, lows fade", 12, INK, "middle", 700))
    b.append(t(300, 198, "the little bump at the cutoff is resonance (Reso)", 12, GREY, "middle", italic=True))
    return _svg(W, 205, "".join(b))


def levels_map():
    """16 Levels Tune: only what the User Guide documents. Pad 4 plays the
    original pitch; lower pads are lower, higher pads are higher. No interval
    values are printed, because the spacing is not yet confirmed."""
    b = []
    W = 600
    cell = 92
    x0, y0 = 20, 10
    for n in range(1, 17):
        col = (n - 1) % 4
        row = 3 - (n - 1) // 4
        x = x0 + col * (cell + 8)
        y = y0 + row * (cell + 8)
        if n == 4:
            fill, lab, tc = ORANGE, "original", "#fff"
        elif n < 4:
            fill, lab, tc = "#d6ccb9", "lower", INK
        else:
            fill, lab, tc = LIGHT, "higher", INK
        b.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="9" fill="{fill}" stroke="{INK}" stroke-width="{2 if n == 4 else 1}"/>')
        b.append(t(x + 10, y + 22, f"PAD {n}", 11, tc, weight=700, ls=1))
        arrow = "" if n == 4 else ("\u2193" if n < 4 else "\u2191")
        b.append(t(x + cell / 2, y + 62, arrow or "\u25CF", 26 if arrow else 20, tc, "middle", 700))
        b.append(t(x + cell / 2, y + 82, lab, 12, tc, "middle", italic=True))
    b.append(t(430, 40, "Documented by Akai", 13, ORANGE, weight=700))
    b.append(t(430, 62, "Pad 4 plays the", 13, INK))
    b.append(t(430, 80, "original pitch.", 13, INK))
    b.append(t(430, 106, "Pads below 4 play", 13, INK))
    b.append(t(430, 124, "lower; pads above", 13, INK))
    b.append(t(430, 142, "4 play higher.", 13, INK))
    b.append(t(430, 184, "Not yet confirmed", 13, ORANGE, weight=700))
    b.append(t(430, 206, "How far apart the", 13, INK))
    b.append(t(430, 224, "pads are. Explore", 13, INK))
    b.append(t(430, 242, "them by ear.", 13, INK))
    return _svg(W, 410, "".join(b))


def bass_pattern():
    b = []
    W = 600
    lw, steps = 70, 16
    gx0 = lw + 10
    cw = (W - gx0 - 10) / steps
    notes = {0: "B1", 4: "B1", 8: "B2", 12: "B3"}
    for s in range(steps):
        lab = str((s % 8) // 2 + 1) if s % 2 == 0 else "+"
        b.append(t(gx0 + s * cw + cw / 2, 34, lab, 12, INK if s % 2 == 0 else GREY, "middle", 700 if s % 2 == 0 else 400))
    b.append(t(gx0 + 4, 14, "BAR 1", 11, GREY, weight=700, ls=2))
    b.append(t(gx0 + 8 * cw + 4, 14, "BAR 2", 11, GREY, weight=700, ls=2))
    y = 44
    b.append(t(lw, y + 26, "Bass", 13, INK, "end", 700))
    for s in range(steps):
        bg = LIGHT if (s // 2) % 2 == 0 else "#efe8da"
        b.append(f'<rect x="{gx0+s*cw+1.5}" y="{y}" width="{cw-3}" height="40" rx="4" fill="{bg}"/>')
    for s, n in notes.items():
        b.append(f'<rect x="{gx0+s*cw+3}" y="{y+3}" width="{cw*2.6}" height="34" rx="5" fill="{ORANGE}"/>')
        b.append(t(gx0 + s * cw + 10, y + 26, f"PAD {n}", 12, "#fff", weight=700))
    b.append(t(gx0, y + 66, "B1 home, B1 home, B2 dark (3 above), B3 step down (2 below), then round again", 12, GREY, italic=True))
    return _svg(W, y + 74, "".join(b))


def arrangement_fig():
    b = []
    W = 600
    secs = [("INTRO", 2, 0.25), ("MAIN", 1, 0.8), ("MAIN", 1, 0.8), ("BREAK", 3, 0.4), ("LIFT", 5, 0.65), ("MAIN", 1, 0.85), ("OUTRO", 4, 0.2)]
    x0, x1 = 20, 580
    w = (x1 - x0) / len(secs)
    base = 150
    pts = []
    for i, (name, seq, e) in enumerate(secs):
        x = x0 + i * w
        col = ORANGE if name == "MAIN" else (AMBER if name in ("LIFT",) else ("#b9ad99" if name in ("BREAK",) else "#d6ccb9"))
        h = 20 + e * 100
        b.append(f'<rect x="{x+2}" y="{base-h}" width="{w-4}" height="{h}" rx="5" fill="{col}"/>')
        b.append(t(x + w / 2, base + 20, name, 11, INK, "middle", 700, 1))
        b.append(t(x + w / 2, base + 37, f"Seq {seq}", 11, GREY, "middle"))
        pts.append((x + w / 2, base - h - 10))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    b.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="5 4"/>')
    b.append(t(x0, 18, "ENERGY", 10, GREY, weight=700, ls=2))
    b.append(t(x1, 222, "each block = one 4-bar sequence, about 11 seconds at 84 BPM", 12, GREY, "end", italic=True))
    return _svg(W, 230, "".join(b))


def sections_fig():
    """Which parts play in each sequence."""
    b = []
    W = 600
    parts = ["Kick", "Snare", "Hats", "Haze", "Bass", "Mug"]
    seqs = [("SEQ 1", "Main", {0, 1, 2, 3, 4, 5}), ("SEQ 2", "Intro", {2, 3}), ("SEQ 3", "Break", {3, 4, 5}), ("SEQ 4", "Outro", {3}), ("SEQ 5", "Lift", {1, 2, 3, 4, 5})]
    lw = 120
    cw = (W - lw - 10) / len(parts)
    for j, p in enumerate(parts):
        b.append(t(lw + j * cw + cw / 2, 18, p, 12, INK, "middle", 700))
    for i, (s, name, on) in enumerate(seqs):
        y = 30 + i * 38
        b.append(t(10, y + 21, s, 12, ORANGE, weight=700, ls=1))
        b.append(t(62, y + 21, name, 12, INK, italic=True))
        for j in range(len(parts)):
            x = lw + j * cw
            b.append(f'<rect x="{x+3}" y="{y}" width="{cw-6}" height="30" rx="5" fill="{INK if j in on else LIGHT}"/>')
    return _svg(W, 30 + len(seqs) * 38 + 4, "".join(b))


def chop_fig():
    import math, random
    random.seed(9)
    b = []
    W = 600
    x0, x1, mid = 20, 580, 70
    hits = [0.02, 0.2, 0.37, 0.55, 0.74]
    pts_t, pts_b = [], []
    n = 260
    for i in range(n + 1):
        p = i / n
        a = 3
        for h in hits:
            if p >= h:
                a += 52 * math.exp(-(p - h) * 26)
        a *= 0.8 + 0.2 * random.random()
        x = x0 + (x1 - x0) * p
        pts_t.append((x, mid - a)); pts_b.append((x, mid + a))
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts_t) + " L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in reversed(pts_b)) + " Z"
    b.append(f'<path d="{d}" fill="{INK}" opacity=".85"/>')
    for k, h in enumerate(hits):
        x = x0 + (x1 - x0) * h - 3
        b.append(f'<line x1="{x}" y1="8" x2="{x}" y2="135" stroke="{ORANGE}" stroke-width="2.5"/>')
        b.append(f'<rect x="{x}" y="140" width="56" height="26" rx="5" fill="{ORANGE}"/>')
        b.append(t(x + 28, 158, f"PAD {k+1}", 11, "#fff", "middle", 700))
    b.append(t(300, 192, "Threshold chopping places slices where it hears new sounds start", 12, GREY, "middle", italic=True))
    return _svg(W, 200, "".join(b))


def signal_flow():
    b = []
    W = 600
    boxes = [
        (10, "SAMPLE", "on a pad"),
        (125, "PAD SETTINGS", "tune, filter, envelope"),
        (240, "KNOB FX", "on the pads you choose"),
        (355, "WHOLE-MIX FX", "Pad FX, Flex Beat, Compressor"),
        (470, "OUTPUT", "speaker, PHONES"),
    ]
    for x, a, s in boxes:
        b.append(f'<rect x="{x}" y="20" width="110" height="64" rx="8" fill="{LIGHT}" stroke="{INK}" stroke-width="1.5"/>')
        b.append(t(x + 55, 47, a, 11, INK, "middle", 700, 0.5))
        words = s.split(", ")
        line = s if len(s) < 18 else None
        if line:
            b.append(t(x + 55, 67, s, 10, GREY, "middle", italic=True))
        else:
            mid = len(words) // 2 or 1
            b.append(t(x + 55, 64, ", ".join(words[:mid]) + ",", 10, GREY, "middle", italic=True))
            b.append(t(x + 55, 77, ", ".join(words[mid:]), 10, GREY, "middle", italic=True))
    for x in (120, 235, 350, 465):
        b.append(f'<polygon points="{x+1},46 {x+4},52 {x+1},58" fill="{INK}"/>')
    b.append(f'<path d="M525,84 L525,118 L65,118 L65,90" fill="none" stroke="{ORANGE}" stroke-width="2.5" stroke-dasharray="6 4"/>')
    b.append(f'<polygon points="65,86 59,98 71,98" fill="{ORANGE}"/>')
    b.append(t(300, 138, "RESAMPLE: record what a sequence plays onto a new pad", 12, ORANGE, "middle", 700))
    b.append(t(300, 156, "a simplified picture; Akai doesn’t say which effects RESAMPLE captures", 11, GREY, "middle", italic=True))
    return _svg(W, 162, "".join(b))


def layering_fig():
    b = []
    W = 600
    layers = [("PAD 5  Haze", "low and slow, filtered", 0), ("PAD 6  Glow", "an octave up, quieter", 1)]
    for i, (a, s, k) in enumerate(layers):
        y = 15 + i * 52
        b.append(f'<rect x="20" y="{y}" width="300" height="42" rx="8" fill="{LIGHT if i else "#e9c9b5"}" stroke="{INK}" stroke-width="1.5"/>')
        b.append(t(36, y + 18, a, 13, INK, weight=700))
        b.append(t(36, y + 34, s, 11, GREY, italic=True))
    b.append(f'<path d="M330,36 C370,36 370,60 400,62 M330,88 C370,88 370,64 400,62" fill="none" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<rect x="405" y="38" width="175" height="48" rx="8" fill="{ORANGE}"/>')
    b.append(t(492, 59, "ONE BIGGER", 12, "#fff", "middle", 700, 1))
    b.append(t(492, 76, "SOUND", 12, "#fff", "middle", 700, 1))
    b.append(t(20, 132, "Pad Link makes one tap play both pads together.", 12, GREY, italic=True))
    return _svg(W, 140, "".join(b))


def versions_fig():
    b = []
    W = 600
    names = ["HELLO1", "GENTLY2", "GENTLY3", "GENTLY4", "GENTLY5", "GENTLY6", "GENTLY7", "GENTLY8"]
    w = 66
    for i, n in enumerate(names):
        x = 12 + i * (w + 7)
        col = ORANGE if i == len(names) - 1 else (LIGHT if i else "#d6ccb9")
        b.append(f'<rect x="{x}" y="14" width="{w}" height="86" rx="5" fill="{col}" stroke="{INK}" stroke-width="1.2"/>')
        b.append(f'<rect x="{x+10}" y="22" width="{w-20}" height="8" rx="2" fill="{INK}" opacity=".25"/>')
        b.append(t(x + w / 2, 70, n, 10, "#fff" if i == len(names) - 1 else INK, "middle", 700))
        b.append(t(x + w / 2, 118, f"Lesson {i+1}", 10, GREY, "middle"))
    return _svg(W, 126, "".join(b))


def screen_buttons_fig():
    """How B1-B3 and K1-K3 relate to the screen. Conceptual."""
    b = []
    W = 600
    b.append(f'<rect x="150" y="45" width="300" height="170" rx="10" fill="#1d1c1b"/>')
    for i, lab in enumerate(["page", "page", "page"]):
        x = 165 + i * 95
        b.append(f'<rect x="{x}" y="58" width="80" height="20" rx="3" fill="#3a3835"/>')
        b.append(t(x + 40, 72, "B" + str(i + 1) + " label", 10, "#d8cfbd", "middle"))
        b.append(f'<rect x="{x}" y="180" width="80" height="22" rx="3" fill="#3a3835"/>')
        b.append(t(x + 40, 195, "K" + str(i + 1) + " value", 10, "#d8cfbd", "middle"))
    b.append(t(300, 135, "conceptual drawing, not a screenshot", 11, "#8c847a", "middle", italic=True))
    for i in range(3):
        x = 165 + i * 95 + 40
        b.append(f'<rect x="{x-24}" y="8" width="48" height="22" rx="4" fill="#5b5852"/>')
        b.append(t(x, 23, f"B{i+1}", 12, CREAM, "middle", 700))
        b.append(f'<line x1="{x}" y1="31" x2="{x}" y2="56" stroke="{ORANGE}" stroke-width="2"/>')
        b.append(f'<circle cx="{x}" cy="252" r="18" fill="#5b5852"/>')
        b.append(t(x, 257, f"K{i+1}", 12, CREAM, "middle", 700))
        b.append(f'<line x1="{x}" y1="203" x2="{x}" y2="233" stroke="{ORANGE}" stroke-width="2"/>')
    b.append(t(470, 70, "← the top labels say", 12, INK))
    b.append(t(470, 86, "what B1–B3 do here", 12, INK))
    b.append(t(470, 190, "← the bottom labels say", 12, INK))
    b.append(t(470, 206, "what K1–K3 change", 12, INK))
    return _svg(W, 280, "".join(b))


def bass_grid():
    return drum_grid([
        ("Bass", {0, 8}, ORANGE),
    ], steps=16)


# ---------------------------------------------------------------------------
# v3 diagrams
# ---------------------------------------------------------------------------

def five_words_fig():
    b = []
    W = 600
    # project outer box
    b.append(f'<rect x="6" y="6" width="588" height="196" rx="10" fill="none" stroke="{INK}" stroke-width="2"/>')
    b.append(t(20, 28, "PROJECT", 12, ORANGE, weight=700, ls=2))
    b.append(t(120, 28, "everything, saved under one name", 12, GREY, italic=True))
    # banks
    b.append(f'<rect x="20" y="42" width="330" height="148" rx="8" fill="{LIGHT}"/>')
    b.append(t(32, 62, "BANKS A–H", 11, INK, weight=700, ls=1.5))
    b.append(t(140, 62, "8 sets of 16 pads", 11, GREY, italic=True))
    letters = "ABCDEFGH"
    for k in range(3):
        x0 = 34 + k * 104
        b.append(f'<rect x="{x0}" y="74" width="94" height="104" rx="6" fill="{CREAM}" stroke="{INK}" stroke-width="1.2"/>')
        b.append(t(x0 + 8, 90, f"BANK {letters[k]}", 10, INK, weight=700))
        for n in range(16):
            c, r = n % 4, 3 - n // 4
            px, py = x0 + 9 + c * 20, 98 + r * 19
            hit = (k == 0 and n in (0, 1, 2, 4, 5))
            b.append(f'<rect x="{px}" y="{py}" width="16" height="15" rx="2" fill="{ORANGE if hit else "#b9b2a6"}"/>')
    b.append(t(345, 120, "…", 18, GREY, "end"))
    # sample callout
    b.append(f'<line x1="57" y1="153" x2="57" y2="196" stroke="{ORANGE}" stroke-width="1.5"/>')
    # sequences
    b.append(f'<rect x="364" y="42" width="216" height="148" rx="8" fill="{LIGHT}"/>')
    b.append(t(376, 62, "SEQUENCES", 11, INK, weight=700, ls=1.5))
    b.append(t(474, 62, "when pads play", 11, GREY, italic=True))
    for r in range(3):
        y = 76 + r * 36
        b.append(f'<rect x="376" y="{y}" width="192" height="28" rx="5" fill="{CREAM}" stroke="{INK}" stroke-width="1.2"/>')
        b.append(t(384, y + 18, f"SEQ {r+1}", 10, ORANGE, weight=700))
        for s in range(8):
            if (r == 0 and s in (0, 2, 4, 6)) or (r == 1 and s in (1, 3, 5, 7)) or (r == 2 and s in (0, 4)):
                b.append(f'<rect x="{430 + s*16}" y="{y+8}" width="10" height="12" rx="2" fill="{INK}"/>')
    b.append(t(300, 222, "a SAMPLE is one sound on one PAD", 12, INK, "middle", 700))
    return _svg(W, 230, "".join(b))


def record_flow_fig():
    steps = [("1", "SEQ", "Sequence Mode"), ("2", "PAD", "choose the sequence"), ("3", "BPM · LENGTH · Q", "set it up"),
             ("4", "SEQ REC", "arm (it flashes)"), ("5", "PLAY", "play sample pads"), ("6", "AGAIN", "overdub layers"),
             ("7", "SEQ REC", "disarm and listen"), ("8", "SAVE", "save the project")]
    b = []
    W = 600
    bw, bh, gx = 134, 66, 14
    for i, (n, key, sub) in enumerate(steps):
        row, col = i // 4, i % 4
        x = 8 + col * (bw + gx)
        y = 10 + row * (bh + 34)
        fill = ORANGE if i in (3, 4, 5) else (LIGHT if i < 3 else "#d6ccb9")
        tc = "#fff" if i in (3, 4, 5) else INK
        b.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="8" fill="{fill}"/>')
        b.append(f'<circle cx="{x+18}" cy="{y+18}" r="11" fill="{INK}"/>')
        b.append(t(x + 18, y + 22.5, n, 12, CREAM, "middle", 700))
        b.append(t(x + 36, y + 23, key, 12 if len(key) < 12 else 10, tc, weight=700))
        b.append(t(x + 12, y + 50, sub, 11.5, tc, italic=True))
        if col < 3:
            ax = x + bw + 2
            b.append(f'<polygon points="{ax},{y+bh/2-5} {ax+9},{y+bh/2} {ax},{y+bh/2+5}" fill="{INK}"/>')
    # wrap arrow row1 -> row2
    b.append(f'<path d="M{8+3*(bw+gx)+bw/2},{10+bh+2} C{8+3*(bw+gx)+bw/2},{10+bh+22} {8+bw/2},{10+bh+12} {8+bw/2},{10+bh+30}" fill="none" stroke="{INK}" stroke-width="1.5"/>')
    b.append(f'<polygon points="{8+bw/2-5},{10+bh+27} {8+bw/2},{10+bh+34} {8+bw/2+5},{10+bh+27}" fill="{INK}"/>')
    # overdub loop over step 6
    x6 = 8 + 1 * (bw + gx); y2 = 10 + bh + 34
    b.append(f'<path d="M{x6+bw-20},{y2+bh+2} C{x6+bw-20},{y2+bh+20} {x6-bw+40},{y2+bh+20} {x6-bw+40},{y2+bh+2}" fill="none" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="5 4"/>')
    b.append(t(x6 - 8, y2 + bh + 30, "repeat steps 5 and 6 for each layer", 11, ORANGE, "middle", italic=True))
    b.append(t(8, y2 + bh + 52, "Steps 1–3: pads choose sequences.   Steps 4–6: recording is armed and pads play sounds.", 11, GREY, italic=True))
    return _svg(W, y2 + bh + 60, "".join(b))


def storage_fig():
    b = []
    W = 600
    def box(x, y, w, h, title, sub, items, fill):
        o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{INK}" stroke-width="1.5"/>',
             t(x + 14, y + 24, title, 13, INK, weight=700, ls=1.5), t(x + 14, y + 42, sub, 11, GREY, italic=True)]
        for k, it in enumerate(items):
            o.append(f'<rect x="{x+14}" y="{y+56+k*28}" width="{w-28}" height="22" rx="4" fill="{CREAM}"/>')
            o.append(t(x + 24, y + 71 + k * 28, it, 11.5, INK))
        return "".join(o)
    b.append(box(8, 8, 270, 228, "INTERNAL DRIVE", "8 GB, about 2 GB of factory content",
                 ["Factory samples, demos, kits", "Your saved projects (User)", "Your saved samples", "Background save of current project", "Exported audio? (not documented)"], LIGHT))
    b.append(box(322, 8, 270, 172, "microSD CARD", "optional, bought separately",
                 ["Sample packs", "Backups and extra projects", "Files to and from a computer"], "#efe3cf"))
    # computer
    b.append(f'<rect x="392" y="208" width="130" height="62" rx="6" fill="{INK}"/>')
    b.append(f'<rect x="402" y="216" width="110" height="40" rx="3" fill="#4a4743"/>')
    b.append(t(457, 241, "COMPUTER", 11, CREAM, "middle", 700, 1.5))
    b.append(f'<line x1="457" y1="181" x2="457" y2="206" stroke="{ORANGE}" stroke-width="3"/>')
    b.append(f'<polygon points="451,188 457,180 463,188" fill="{ORANGE}"/><polygon points="451,199 457,207 463,199" fill="{ORANGE}"/>')
    b.append(t(470, 197, "SD Card Access", 11, ORANGE, weight=700))
    b.append(f'<line x1="282" y1="238" x2="388" y2="238" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    b.append(t(12, 258, "Akai describes no computer route to this drive", 11, GREY, italic=True))
    return _svg(W, 276, "".join(b))


# ---------------------------------------------------------------------------
# Cover: line-art "technical drawing" of the top panel, in the style of the
# GitHub hero. Uses the same verified coordinates as panel(). Labels are only
# those printed on the panel and used elsewhere in this book.
# ---------------------------------------------------------------------------
COVER_LABELS = {  # secondary (SHIFT) labels used in the book
    "SAMPLE": "INPUT CONFIG", "SEQ": "STEP EDIT", "KNOBFX": "FX SELECT",
    "CHOP": "NOTE ON", "MUTE": "UNMUTE ALL", "LOOP": "REVERSE", "16LEVELS": "TYPE",
    "SAMPLESELECT": "SAVE SAMPLE", "ERASE": "COPY", "MINUS": "UNDO",
    "SEQRECORD": "RECALL",
}
COVER_PADS = {1: "FULL LEVEL", 3: "DOUBLE SEQ", 4: "COUNT-IN", 5: "COMPRESSOR",
              9: "FADER", 11: "RESAMPLE", 12: "SONG", 13: "TRIM SAMPLE",
              14: "TIME CORRECT", 15: "WARP", 16: "PROJECT"}
COVER_NAMES = {"16LEVELS": "16 LEVELS", "SAMPLESELECT": "SAMPLE SELECT",
               "NOTEREPEAT": "NOTE REPEAT", "SAMPLERECORD": "SAMPLE RECORD",
               "SEQRECORD": "SEQ RECORD", "PADFX": "PAD FX", "KNOBFX": "KNOB FX",
               "PADBANK": "PAD BANK", "TAPTEMPO": "TAP TEMPO", "MINUS": "−", "PLUS": "+"}


def cover_blueprint():
    import math
    LN = "#E8D9BC"          # line colour (cream on the dark cover)
    DIM = "#8f8679"
    MONO = "'IBM Plex Mono', monospace"
    X0, Y0, SC = 64, -3, 0.15  # mm placement of the panel on the cover
    W, H = 905 - OX, 955 - OY
    o = ['<svg class="blueprint" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 244" '
         'style="position:absolute;left:0;top:0;width:160mm;height:244mm">',
         '<defs><pattern id="hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<line x1="0" y1="0" x2="0" y2="9" stroke="{LN}" stroke-opacity=".22" stroke-width="1.4"/></pattern>'
         '<clipPath id="page"><rect x="0" y="0" width="160" height="244"/></clipPath></defs>',
         '<g clip-path="url(#page)">']
    # faint drafting grid behind the drawing
    for gx in range(0, 161, 8):
        o.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="112" stroke="{LN}" stroke-opacity=".035" stroke-width=".2"/>')
    for gy in range(0, 113, 8):
        o.append(f'<line x1="0" y1="{gy}" x2="160" y2="{gy}" stroke="{LN}" stroke-opacity=".035" stroke-width=".2"/>')

    def P(ux, uy):  # panel units -> mm
        return X0 + ux * SC, Y0 + uy * SC

    g = [f'<g transform="translate({X0},{Y0}) scale({SC})" fill="none" stroke="{LN}" stroke-width="2.6" '
         f'font-family="{MONO}" stroke-linejoin="round">']
    txt = lambda x, y, s, fs=12, col=LN, anc="middle", w=500, ls=1.5: (
        f'<text x="{x}" y="{y}" text-anchor="{anc}" font-size="{fs}" font-weight="{w}" letter-spacing="{ls}" '
        f'fill="{col}" stroke="none">{s}</text>')
    # body + top band (hatched)
    g.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="34" fill="#2f2e2b" stroke-width="3.4"/>')
    g.append(f'<rect x="12" y="12" width="{W-24}" height="{335-OY-12}" rx="18" fill="url(#hatch)"/>')
    # display
    dx, dy, dw, dh = R(457, 180, 640, 318)
    g.append(f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" rx="5" fill="#2B2A28"/>')
    for i, s in enumerate(("Trim", "Tune", "Filter")):
        g.append(txt(dx + 30 + i * 62, dy + 20, s, 11, LN, w=400, ls=.5))
    g.append(f'<line x1="{dx+10}" y1="{dy+28}" x2="{dx+52}" y2="{dy+28}" stroke="{ORANGE}" stroke-width="2.4"/>')
    g.append(f'<line x1="{dx+8}" y1="{dy+40}" x2="{dx+dw-8}" y2="{dy+40}" stroke-dasharray="3 3" stroke-width="1"/>')
    for row, yc in enumerate((dy + 64, dy + 94)):
        pts = []
        for k in range(0, 160):
            x = dx + 12 + k * (dw - 24) / 159
            a = 11 * (0.55 + 0.45 * abs(math.sin(k * 0.37 + row))) * (1 if k % 2 else -1) * (0.6 + 0.4 * math.sin(k * 1.7) ** 2)
            pts.append(f"{x:.1f},{yc + a:.1f}")
        g.append(f'<polyline points="{" ".join(pts)}" stroke="{ORANGE}" stroke-width="1.6"/>')
    g.append(f'<line x1="{dx}" y1="{dy+dh-22}" x2="{dx+dw}" y2="{dy+dh-22}" stroke-width="1.4"/>')
    for i, s in enumerate(("Start", "End", "Loop")):
        g.append(txt(dx + 24 + i * 62, dy + dh - 7, s, 11, LN, w=400, ls=.5))
    # meters
    for mx in (672, 690):
        for k in range(5):
            f = ORANGE if k < 2 else "none"
            g.append(f'<rect x="{mx-OX}" y="{185-OY+k*27}" width="13" height="20" rx="2" fill="{f}" stroke="{ORANGE if k < 2 else LN}" stroke-width="1.8"/>')
    # speaker
    sx, sy, sw, sh = R(735, 182, 862, 305)
    g.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="12" fill="#2B2A28"/>')
    for gy in range(int(sy) + 12, int(sy + sh) - 6, 12):
        for gx in range(int(sx) + 12, int(sx + sw) - 6, 12):
            g.append(f'<circle cx="{gx}" cy="{gy}" r="2" fill="{LN}" stroke="none"/>')
    # bank indicator and logo text in the band
    g.append(f'<rect x="{352-OX}" y="{212-OY}" width="30" height="34" rx="4" fill="#2B2A28" stroke-width="2"/>')
    g.append(txt(367 - OX, 236 - OY, "A", 18, LN, w=500, ls=0))
    # knobs
    def knob(cx, cy, r, ticks=True):
        if ticks:
            for k in range(11):
                a = math.radians(-225 + k * 27)
                g.append(f'<line x1="{cx + (r+14)*math.cos(a):.1f}" y1="{cy + (r+14)*math.sin(a):.1f}" '
                         f'x2="{cx + (r+22)*math.cos(a):.1f}" y2="{cy + (r+22)*math.sin(a):.1f}" stroke-width="1.8"/>')
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r+7}" fill="#2B2A28" stroke-width="2"/>')
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke-width="2.6"/>')
        g.append(f'<line x1="{cx}" y1="{cy-r+3}" x2="{cx}" y2="{cy-4}" stroke-width="3" stroke-linecap="round"/>')
    for key, ((cx, cy), r, lab) in KNOBS.items():
        if key == "ENCODER":
            for k in range(36):
                a = math.radians(k * 10)
                g.append(f'<line x1="{cx + r*math.cos(a):.1f}" y1="{cy + r*math.sin(a):.1f}" '
                         f'x2="{cx + (r+8)*math.cos(a):.1f}" y2="{cy + (r+8)*math.sin(a):.1f}" stroke-width="1.6"/>')
            g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#2B2A28"/>')
            g.append(f'<circle cx="{cx}" cy="{cy}" r="{r-10}" stroke-width="1.6"/>')
            continue
        knob(cx, cy, r)
        if key == "MAINVOL":
            g.append(txt(cx, cy + r + 40, "MAIN VOLUME", 12))
        else:
            g.append(txt(cx + r + 14, cy + r + 6, lab, 13, anc="start", ls=1))
    # mode / pad-play captions
    for cx, s in ((284 - OX, "MODE"), (810 - OX, "PAD PLAY")):
        g.append(txt(cx, 356 - OY, s, 12, DIM, ls=2))
        g.append(f'<line x1="{cx-80}" y1="{352-OY}" x2="{cx-40}" y2="{352-OY}" stroke="{DIM}" stroke-width="1.4"/>')
        g.append(f'<line x1="{cx+40}" y1="{352-OY}" x2="{cx+80}" y2="{352-OY}" stroke="{DIM}" stroke-width="1.4"/>')
    # buttons
    for key, ((x, y, w, h), lab) in BUTTONS.items():
        if key in ("B1", "B2", "B3"):
            g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#2B2A28" stroke-width="2.2"/>')
            continue
        hot = key in ("PADFX", "KNOBFX")
        g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{ORANGE if hot else "#2f2e2b"}" '
                 f'stroke="{ORANGE if hot else LN}" stroke-width="2.4"/>')
        name = COVER_NAMES.get(key, lab if key not in ("STOP", "PLAY") else "")
        if key == "STOP":
            g.append(f'<rect x="{x+w/2-6}" y="{y+h/2-6}" width="12" height="12" fill="{LN}" stroke="none"/>')
        elif key == "PLAY":
            g.append(f'<path d="M{x+w/2-6},{y+h/2-8} l14,8 l-14,8z" fill="{LN}" stroke="none"/>')
        else:
            words = name.split(" ")
            fs = 22 if name in ("−", "+") else 9.5
            col = "#FBF7EE" if hot else LN
            if len(words) == 2 and len(name) > 7:
                g.append(txt(x + w / 2, y + h / 2 - 1.5, words[0], fs, col, ls=.6))
                g.append(txt(x + w / 2, y + h / 2 + 9.5, words[1], fs, col, ls=.6))
            else:
                g.append(txt(x + w / 2, y + h / 2 + fs * .36, name, fs, col, ls=.6))
        if key in COVER_LABELS:
            g.append(txt(x + w / 2, y + h + 10.5, COVER_LABELS[key], 8, DIM, ls=.5))
    # fader
    fx, fy, fw, fh = R(262, 545, 326, 735)
    g.append(f'<rect x="{fx+fw/2-6}" y="{fy}" width="12" height="{fh}" rx="5" stroke-width="2"/>')
    g.append(f'<rect x="{fx+6}" y="{fy+70}" width="{fw-12}" height="40" rx="5" fill="#2f2e2b" stroke-width="2.6"/>')
    for k in (1, 2, 3):
        g.append(f'<line x1="{fx+14}" y1="{fy+70+k*10}" x2="{fx+fw-14}" y2="{fy+70+k*10}" stroke-width="1.4"/>')
    # pad well and pads
    g.append(f'<rect x="{366-OX}" y="{453-OY}" width="{737-366}" height="{825-453}" rx="6" fill="{LN}" fill-opacity=".09" stroke-width="5"/>')
    for n in range(1, 17):
        x, y, w, h = pad_rect(n)
        g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#2f2e2b" stroke-width="2.2"/>')
        g.append(txt(x + 2, y + h + 10, str(n), 8, LN, anc="start", ls=.3))
        if n in COVER_PADS:
            g.append(txt(x + w - 1, y + h + 10, COVER_PADS[n], 6.2, DIM, anc="end", ls=.3))
    # mic glyph
    for ddx, ddy in ((-5, -9), (5, -9), (-5, 0), (5, 0)):
        g.append(f'<circle cx="{869-OX+ddx}" cy="{548-OY+ddy}" r="3" fill="{LN}" stroke="none"/>')
    # palm rest
    px, py, pw, ph = R(200, 838, 893, 945)
    g.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="url(#hatch)" stroke-width="2"/>')
    g.append('</g>')
    o += g
    # drafting centre lines (dash-dot), through K2 and between pad rows 2 and 3
    k2x, _ = P(547 - OX, 0)
    o.append(f'<line x1="{k2x}" y1="0" x2="{k2x}" y2="112" stroke="{ORANGE}" stroke-opacity=".7" stroke-width=".28" stroke-dasharray="4 1.2 .6 1.2"/>')
    _, hy = P(0, 732 - OY + 38)
    o.append(f'<line x1="40" y1="{hy}" x2="160" y2="{hy}" stroke="{ORANGE}" stroke-opacity=".7" stroke-width=".28" stroke-dasharray="4 1.2 .6 1.2"/>')
    # leader lines with dots, like the hero
    leaders = [
        ((457 - OX, 192 - OY), None),            # screen
        ((412 - OX - 20, 410 - OY - 18), 31.5),    # K1 (with a bend)
        ((220 - OX, 426 - OY), None),            # PAD FX
        ((375 - OX, 553 - OY), None),            # pad 13
        ((262 - OX + 6, 545 - OY + 90), None),   # fader cap
    ]
    for (ux, uy), bend in leaders:
        tx, ty = P(ux, uy)
        ly = bend if bend else ty
        lx = 40
        o.append(f'<circle cx="{lx}" cy="{ly:.2f}" r=".9" fill="{ORANGE}"/>')
        if bend:
            o.append(f'<polyline points="{lx},{ly:.2f} {tx-6:.2f},{ly:.2f} {tx:.2f},{ty:.2f}" fill="none" stroke="{ORANGE}" stroke-width=".32"/>')
        else:
            o.append(f'<line x1="{lx}" y1="{ly:.2f}" x2="{tx:.2f}" y2="{ty:.2f}" stroke="{ORANGE}" stroke-width=".32"/>')
        o.append(f'<circle cx="{tx:.2f}" cy="{ty:.2f}" r=".55" fill="{ORANGE}"/>')
    o.append('</g></svg>')
    return "".join(o)
