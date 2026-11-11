"""Build MPC, Gently: assembles content/*.html, inlines vector diagrams,
renders a PDF with WeasyPrint (bookmarks + internal links)."""
import re, glob, shutil, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import svgs
import weasyprint

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# --- assets -----------------------------------------------------------------
os.makedirs("assets", exist_ok=True)
for name, col in [("akai", "#FBF7EE"), ("mpcsample", "#C4572A"), ("mpcsample", "#FBF7EE"), ("akai", "#2B2A28")]:
    src = open(f"assets/{name}.svg").read()
    tag = {"#FBF7EE": "cream", "#C4572A": "orange", "#2B2A28": "ink"}[col]
    open(f"assets/{name}_{tag}.svg", "w").write(src.replace('fill="#000"', f'fill="{col}"'))
if not os.path.exists("assets/overview.png"):
    shutil.copy("/mnt/user-data/uploads/1794140154773_image.png", "assets/overview.png")
if not os.path.exists("fonts"):
    os.makedirs("fonts")
    for f in glob.glob("/home/claude/fonts/x_*/files/*latin-[0-9]*.woff2"):
        shutil.copy(f, "fonts/")


def cover_pads():
    S = svgs
    o = ['<svg class="padart" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" style="position:absolute;right:14mm;top:17mm;width:50mm">']
    lit = {6: S.ORANGE, 11: S.AMBER, 1: "#8C847A"}
    for n in range(16):
        c, r = n % 4, n // 4
        fill = lit.get(n, "#3a3835")
        o.append(f'<rect x="{c*100+6}" y="{r*100+6}" width="88" height="88" rx="10" fill="{fill}"/>')
    o.append("</svg>")
    return "".join(o)


FIGS = {
    "beats_bars": svgs.beats_bars,
    "drum_grid_l2": lambda: svgs.drum_grid([("Kick", {0, 4}, svgs.ORANGE), ("Snare", {2, 6}, svgs.INK), ("Hi-hat", set(range(8)), svgs.GREY)], steps=8),
    "drum_grid_l6": lambda: svgs.drum_grid([("Kick", {0, 4}, svgs.ORANGE), ("Snare", {2, 6}, svgs.INK), ("Hi-hat", set(range(8)), svgs.GREY), ("Mug low", {3}, svgs.AMBER), ("Mug high", {7}, svgs.AMBER)], steps=8),
    "quantise_fig": svgs.quantise_fig,
    "waveform_fig": svgs.waveform_fig,
    "waveform_explainer": svgs.waveform_explainer,
    "envelope_fig": svgs.envelope_fig,
    "filter_fig": svgs.filter_fig,
    "levels_map": svgs.levels_map,
    "bass_pattern": svgs.bass_pattern,
    "arrangement_fig": svgs.arrangement_fig,
    "sections_fig": svgs.sections_fig,
    "chop_fig": svgs.chop_fig,
    "signal_flow": svgs.signal_flow,
    "layering_fig": svgs.layering_fig,
    "versions_fig": svgs.versions_fig,
    "screen_buttons_fig": svgs.screen_buttons_fig,
    "cover_pads": cover_pads,
    "cover_blueprint": svgs.cover_blueprint,
    "five_words_fig": svgs.five_words_fig,
    "record_flow_fig": svgs.record_flow_fig,
    "storage_fig": svgs.storage_fig,
}


def fig_sub(m):
    name, _, cap = m.group(1).partition("|")
    svg = FIGS[name]()
    if name in ("cover_pads", "cover_blueprint"):
        return svg
    capt = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure class="diagram">{svg}{capt}</figure>'


def panel_sub(m):
    parts = m.group(1).split("|")
    keys = [k for k in parts[0].split(",") if k]
    pads = [int(p) for p in parts[1].split(",") if p] if len(parts) > 1 else []
    cap = parts[2] if len(parts) > 2 else ""
    svg = svgs.panel(keys, pads)
    return f'<table class="meetgrid"><tr><td class="mfig"><figure class="panelfig">{svg}<figcaption>{cap}</figcaption></figure></td><!--MEETSPLIT-->'


def chip(m):
    s = m.group(1)
    if s.startswith("@"):
        return f'<span class="kn">{s[1:]}</span>'
    if s.startswith("#"):
        return f'<span class="pd">PAD {s[1:]}</span>'
    if s.startswith("~"):
        return f'<span class="scr">{s[1:]}</span>'
    cls = "k shift" if s == "SHIFT" else "k"
    return f'<span class="{cls}">{s}</span>'


body = "\n".join(open(f).read() for f in sorted(glob.glob("content/*.html")))
body = re.sub(r"<!--FIG:(.*?)-->", fig_sub, body)
body = re.sub(r"<!--PANEL:(.*?)-->", panel_sub, body)
# pull the first <dl class="controls"> (or table) after each panel into the grid
def meet(m):
    return m.group(1) + '<td class="meetlist">' + m.group(2) + '</td></tr></table>'
body = re.sub(r'(<table class="meetgrid">.*?<!--MEETSPLIT-->)\s*((?:<p>.*?</p>\s*)?(?:<dl class="controls">.*?</dl>|<table class="ref">.*?</table>))', meet, body, flags=re.S)
def bm(m):
    tag, title = m.group(2), re.sub(r"<[^>]+>", "", m.group(3)).strip()
    label = (tag + ": " + title).replace('"', "&quot;")
    return f'<h2{m.group(1)} data-bm="{label}"><span class="tag">{tag}</span>{m.group(3)}</h2>'
body = re.sub(r'<h2([^>]*)><span class="tag">(.*?)</span>(.*?)</h2>', bm, body)
body = re.sub(r"\[\[(.+?)\]\]", chip, body)
body = re.sub(r'style="--start:(\d+)"', r'style="counter-reset: st \1"', body)

# typography guard: the learner asked for no em dashes anywhere
assert "—" not in body and "&#8212;" not in body and "&mdash;" not in body, "em dash found"

html = f"""<!doctype html><html lang="en-AU"><head><meta charset="utf-8">
<title>MPC, Gently</title>
<meta name="author" content="slowphase">
<meta name="description" content="An illustrated beginner's guide to the Akai MPC Sample">
<link rel="stylesheet" href="style.css"></head><body>
{body}
</body></html>"""
open("book.html", "w").write(html)

out = sys.argv[1] if len(sys.argv) > 1 else "MPC-Gently.pdf"
doc = weasyprint.HTML("book.html", base_url=ROOT).render()
print("pages:", len(doc.pages))
doc.write_pdf(out)
print("wrote", out, os.path.getsize(out) // 1024, "KB")
