"""Small SVG primitives shared by the book's grayscale teaching figures."""

from html import escape
from pathlib import Path

INK = '#292929'
MUTED = '#555555'
PALE = '#f2f2f2'
MID = '#dedede'
FONT = 'Noto Sans CJK SC,Source Han Sans CN,Microsoft YaHei,sans-serif'


class Figure:
    def __init__(self, title, description, height, width=720):
        self.width, self.height = width, height
        self.parts = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" width="150mm" '
            f'height="{150 * height / width:.2f}mm" viewBox="0 0 {width} {height}" '
            'role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title>',
            f'<desc id="desc">{escape(description)}</desc>',
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 Z" fill="{INK}"/></marker></defs>',
            f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        ]

    def rect(self, x, y, w, h, fill=PALE, dashed=False, radius=6):
        dash = ' stroke-dasharray="7 5"' if dashed else ''
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
                          f'rx="{radius}" fill="{fill}" stroke="{INK}" stroke-width="1.5"{dash}/>')

    def text(self, x, y, content, size=18, bold=False, anchor='middle', color=INK):
        weight = '700' if bold else '400'
        for i, line in enumerate(content.split('\n')):
            self.parts.append(f'<text x="{x}" y="{y + i * (size + 9)}" '
                              f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
                              f'text-anchor="{anchor}" fill="{color}">{escape(line)}</text>')

    def box(self, x, y, w, h, title, detail='', fill=PALE):
        self.rect(x, y, w, h, fill)
        self.text(x + w / 2, y + (h / 2 + 6 if not detail else 30), title, bold=True)
        if detail:
            self.text(x + w / 2, y + 61, detail, size=16)

    def path(self, points, arrow=True, dashed=False):
        d = 'M ' + ' L '.join(f'{x} {y}' for x, y in points)
        marker = ' marker-end="url(#arrow)"' if arrow else ''
        dash = ' stroke-dasharray="6 5"' if dashed else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.8"{marker}{dash}/>')

    def save(self, filename):
        root = Path(__file__).resolve().parents[2] / 'book' / 'images'
        (root / filename).write_text('\n'.join(self.parts + ['</svg>']) + '\n')
