"""Render the 1280x640 GitHub social preview card."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
BG = (13, 17, 23)
FG = (230, 237, 243)
MUTED = (139, 148, 158)
ACCENT = (255, 123, 114)
GREEN = (63, 185, 80)

F = "C:/Windows/Fonts/"
bold = lambda s: ImageFont.truetype(F + "segoeuib.ttf", s)
reg = lambda s: ImageFont.truetype(F + "segoeui.ttf", s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Accent bar down the left edge.
d.rectangle([0, 0, 10, H], fill=ACCENT)

x = 80
d.text((x, 92), "Modeling Contract Review", font=bold(62), fill=FG)
d.text((x, 172), "Free AI contract review for models and talent", font=reg(34), fill=MUTED)

# Risk chips: what it actually catches.
chips = [
    ("5-year exclusivity", ACCENT),
    ('"In perpetuity" image rights', ACCENT),
    ("Upfront fees", ACCENT),
    ("Hidden commission stacking", ACCENT),
]
cx, cy = x, 268
for i, (label, color) in enumerate(chips):
    w = d.textlength(label, font=reg(26)) + 44
    if i and i % 2 == 0:  # two chips per row keeps both rows balanced
        cx, cy = x, cy + 66
    d.rounded_rectangle([cx, cy, cx + w, cy + 50], radius=25, outline=color, width=2)
    d.text((cx + 22, cy + 11), label, font=reg(26), fill=color)
    cx += w + 16

d.text((x, cy + 92), "Photograph the pages. Know what to push back on before you sign.",
       font=reg(30), fill=FG)

# Footer.
d.text((x, H - 96), "github.com/CptRizzen/modeling-contract-review", font=reg(26), fill=MUTED)
d.text((x, H - 58), "Claude  ·  ChatGPT  ·  Cursor  ·  26+ tools     MIT",
       font=reg(24), fill=(88, 96, 105))

# "Not legal advice" tag, top right.
tag = "Not legal advice"
tw = d.textlength(tag, font=reg(24)) + 36
d.rounded_rectangle([W - 80 - tw, 92, W - 80, 136], radius=22,
                    fill=(22, 27, 34), outline=GREEN, width=1)
d.text((W - 80 - tw + 18, 101), tag, font=reg(24), fill=GREEN)

out = "C:/Users/shawn/Documents/modeling-contract-review/examples/social-preview.png"
img.save(out, optimize=True)
print(out, img.size)
