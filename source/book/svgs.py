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
    """16 Levels Tune: pad 4 = original pitch (User Guide). Semitone offsets
    shown as the conventional MPC layout; the book asks the reader to check."""
    b = []
    W = 600
    off = {n: n - 4 for n in range(1, 17)}
    names = {4: "HOME", 7: "dark", 9: "lift", 11: "strong", 16: "octave", 2: "step down"}
    cell = 92
    x0 = 20
    y0 = 10
    for n in range(1, 17):
        col = (n - 1) % 4
        row = 3 - (n - 1) // 4
        x = x0 + col * (cell + 8)
        y = y0 + row * (cell + 8)
        key = n in names
        fill = ORANGE if n == 4 else (AMBER if key else LIGHT)
        b.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="9" fill="{fill}" stroke="{INK}" stroke-width="{2 if key else 1}"/>')
        b.append(t(x + 10, y + 22, f"PAD {n}", 11, INK if n != 4 else "#fff", weight=700, ls=1))
        o = off[n]
        s = "±0" if o == 0 else (f"+{o}" if o > 0 else f"−{-o}")
        b.append(t(x + cell / 2, y + 60, s, 26, INK if n != 4 else "#fff", "middle", 700))
        if key:
            b.append(t(x + cell / 2, y + 82, names[n], 12, INK if n != 4 else "#fff", "middle", italic=True))
    b.append(t(430, 40, "PAD 4 = original", 14, ORANGE, weight=700))
    b.append(t(430, 58, "confirmed by Akai", 12, GREY, italic=True))
    b.append(t(430, 96, "IF each pad is one", 13, INK, weight=700))
    b.append(t(430, 114, "semitone, as on", 13, INK))
    b.append(t(430, 132, "classic MPCs, the", 13, INK))
    b.append(t(430, 150, "numbers show the", 13, INK))
    b.append(t(430, 168, "distance from home.", 13, INK))
    b.append(t(430, 206, "Not yet confirmed", 13, ORANGE, weight=700))
    b.append(t(430, 224, "for MPC Sample:", 13, INK))
    b.append(t(430, 242, "check by ear with", 13, INK))
    b.append(t(430, 260, "the octave test.", 13, INK))
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
    b.append(t(gx0, y + 66, "B1 home (0), B1 home, B2 dark (+3), B3 step down (−2), then round again", 12, GREY, italic=True))
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
    b.append(t(300, 192, "Threshold chopping puts a slice wherever a new sound starts", 12, GREY, "middle", italic=True))
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
