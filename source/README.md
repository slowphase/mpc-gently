# MPC, Gently: editable source

This folder holds everything needed to rebuild the handbook, for example after hardware testing or a firmware update. You don't need any of it to *read* the book: the finished PDF is on the [Releases page](https://github.com/slowphase/mpc-gently/releases), along with this same source as a ZIP.

One manuscript, one edition (160 × 244 mm, sized for the iPad mini).

## What's where

| Path | What it is |
| --- | --- |
| `book/content/*.html` | The manuscript, in reading order: front matter, Lessons 1 to 8, then the reference pages. **Edit the words here.** |
| `book/build.py` | Assembles the manuscript, draws the diagrams into it, expands control "chips" and renders the PDF with bookmarks and links. |
| `book/svgs.py` | Draws the MPC Sample panel schematic and the teaching diagrams (Python that writes SVG). |
| `book/style.css` | The design system: palette, typography, page size, callouts and layout. |
| `book/vectorize.py` | Traced the logo artwork into SVG. Not needed for a normal build. |
| `book/assets/` | Logos and the top-panel diagram (Akai artwork, see [NOTICE](book/assets/NOTICE.md)). |
| `book/fonts/` | Michroma, Archivo, Source Serif 4 and IBM Plex Mono, latin subsets (SIL OFL 1.1). |
| `book/CHANGELOG.md` | Revision history of the manuscript before this repository existed. |

## Writing conventions

The manuscript uses short tokens that the build turns into the small labels you see in the book:

| You write | You get |
| --- | --- |
| `[[SEQ RECORD]]` | a button |
| `[[@K1]]` | a knob |
| `[[#4]]`, `[[#A5]]` | a pad, or a pad in a given bank |
| `[[~Save Project]]` | words on the MPC's screen |
| `<!--PANEL:...-->` | a lesson panel drawing, with controls and pads lit in orange |
| `<!--FIG:name\|caption-->` | a teaching diagram from `svgs.py` |

## Building

You'll need Python 3 with `weasyprint` (version 70 was used for v0.9). The build also needs `Pillow` only if you re-run `vectorize.py`.

```
cd source/book
pip install weasyprint
python3 build.py                 # writes MPC-Gently.pdf
python3 build.py other-name.pdf  # or choose the output name
```

A full build takes a few seconds. The build refuses to continue if an em dash slips into the text.

## Rules the build keeps

- Every hardware instruction restates something checked against Akai's official *MPC Sample User Guide* (firmware 1.3). When updating, check facts against the current official documentation, or against what you observed on a real MPC Sample, and say which in the changelog.
- Where the official guide is silent, the book says so rather than guessing.
- Sample Mode pages are always reached with "press B1/B2/B3 until the page appears", never a fixed number of presses.

## Licences

The original text, artwork and diagrams are CC BY-SA 4.0. The build scripts and stylesheet are MIT. The fonts are SIL OFL 1.1. The Akai artwork in `book/assets/` is not covered by this project's licences. Full details are in [LICENSE.md](../LICENSE.md).
