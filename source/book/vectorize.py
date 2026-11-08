import sys, numpy as np, potrace
from PIL import Image
def vec(png, out, color='#000'):
    im = Image.open(png).convert('L')
    w,h = im.size
    big = im.resize((w*3,h*3), Image.LANCZOS)
    arr = np.array(big) <= 127
    bmp = potrace.Bitmap(arr)
    path = bmp.trace(turdsize=4, alphamax=1.0, opticurve=True, opttolerance=0.2)
    parts=[]
    for curve in path:
        sp = curve.start_point
        d = [f"M{sp.x:.1f},{sp.y:.1f}"]
        for seg in curve.segments:
            if seg.is_corner:
                d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
            else:
                d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        d.append("Z"); parts.append("".join(d))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w*3} {h*3}"><path fill="{color}" fill-rule="evenodd" d="{" ".join(parts)}"/></svg>'
    open(out,'w').write(svg); print(out, len(svg))
for n in ['akai','mpcsample']:
    vec(f'{n}_mask.png', f'{n}.svg')
