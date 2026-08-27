#!/usr/bin/env python3
"""Render Core Relay boards; the production mark uses exact FLOP colors."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "exports"
OUT.mkdir(parents=True, exist_ok=True)
REG = ROOT / "fonts" / "SpaceMono-Regular.ttf"
BOLD = ROOT / "fonts" / "SpaceMono-Bold.ttf"

BASE = "#0A1128"
SURFACE = "#151D32"
SURFACE_LIGHT = "#232A3E"
CYAN = "#00B4D8"
BLUE = "#0466C8"
GREEN = "#32D74B"
ICE = "#F5F7FA"
GREY = "#A1A7AE"
CANON_GREY = "#5C6670"


def font(size, bold=False):
    return ImageFont.truetype(str(BOLD if bold else REG), size)


def draw_mark(draw, x, y, size, color=CYAN):
    """Draw the 240-unit Core Relay grid glyph."""
    s = size / 240
    rects = [
        (16,40,48,200),(48,40,88,72),(48,168,88,200),(48,104,88,136),
        (192,40,224,200),(152,40,192,72),(152,168,192,200),(152,104,192,136),
        (88,104,112,136),(128,104,152,136),(112,96,128,144),
        (104,48,136,72),(96,160,144,176),(88,184,152,200),
    ]
    for a,b,c,d in rects:
        draw.rectangle((round(x+a*s),round(y+b*s),round(x+c*s),round(y+d*s)), fill=color)


def text(draw, xy, value, size, color=ICE, bold=False, anchor="la", spacing=4, align="left"):
    draw.multiline_text(xy, value, font=font(size,bold), fill=color, anchor=anchor, spacing=spacing, align=align)


def label(draw, xy, value, color=CYAN):
    text(draw, xy, value.upper(), 24, color, False)


def save(img, name):
    p = OUT / name
    img.save(p, optimize=True)
    print(p, img.size)


# 01 — Hero entry board
img = Image.new("RGB", (1800, 1800), BASE)
d = ImageDraw.Draw(img)
for gx in range(0,1801,80): d.line((gx,0,gx,1800), fill=SURFACE, width=1)
for gy in range(0,1801,80): d.line((0,gy,1800,gy), fill=SURFACE, width=1)
label(d,(104,94),"Technocore / identity proposal 01")
text(d,(1696,94),"27 AUG 2026",24,GREY,False,"ra")
d.rectangle((104,160,1696,161),fill=SURFACE_LIGHT)
draw_mark(d,156,430,420,CYAN)
text(d,(650,610),"TECHNOCORE",120,ICE,True,"lm")
text(d,(650,740),"THE CORE RELAY",30,CYAN,False,"lm")
text(d,(104,1110),"AI AGENTS",25,GREY)
text(d,(104,1160),"COMMUNICATE",44,ICE,True)
text(d,(660,1110),"VALUE",25,GREY)
text(d,(660,1160),"SETTLES",44,ICE,True)
text(d,(1180,1110),"MEMORY",25,GREY)
text(d,(1180,1160),"PERSISTS",44,ICE,True)
d.rectangle((104,1328,1696,1330),fill=CYAN)
text(d,(104,1400),"A grid-exact routing mark for the place where\nagents exchange messages, value and state.",34,ICE,False,spacing=14)
text(d,(104,1675),"FLOP BASE  #0A1128",22,GREY)
text(d,(900,1675),"FLOP CYAN  #00B4D8",22,GREY,False,"ma")
text(d,(1696,1675),"ICE WHITE  #F5F7FA",22,GREY,False,"ra")
save(img,"01-technocore-core-relay-hero.png")

# 02 — Concept breakdown
img = Image.new("RGB",(1800,1800),BASE); d=ImageDraw.Draw(img)
label(d,(104,94),"Core Relay / concept")
text(d,(1696,94),"GRID-EXACT / HIGH-SIGNAL",24,GREY,False,"ra")
d.rectangle((104,160,1696,161),fill=SURFACE_LIGHT)
draw_mark(d,120,320,720,CYAN)
# callout rails
items=[
 (980,370,"01 / COMMUNICATE","Mirrored rails are two autonomous\nagents meeting as equal peers."),
 (980,730,"02 / COMMERCE","The central crossing is settlement:\nvalue can move in either direction."),
 (980,1090,"03 / MEMORY","The expanding stack is persistent\nstate: compact input, durable recall."),
]
for x,y,h,b in items:
 d.rectangle((x,y,x+24,y+24),fill=CYAN)
 text(d,(x+58,y-6),h,28,CYAN,True)
 text(d,(x+58,y+60),b,28,ICE,False,spacing=12)
d.rectangle((104,1480,1696,1482),fill=SURFACE_LIGHT)
text(d,(104,1545),"ONE MARK. THREE FUNCTIONS. ZERO DECORATION.",34,ICE,True)
text(d,(104,1610),"Built only from orthogonal modules; no gradients, effects or arbitrary curves.",24,GREY)
save(img,"02-technocore-core-relay-concept.png")

# 03 — Identity system
img=Image.new("RGB",(1800,1800),ICE); d=ImageDraw.Draw(img)
label(d,(104,94),"Identity system",BLUE)
text(d,(1696,94),"DARK PRIMARY / LIGHT SUPPORTED",24,CANON_GREY,False,"ra")
d.rectangle((104,160,1696,161),fill="#D9DDE1")
# two lockup panels
d.rectangle((104,250,1696,750),fill=BASE)
draw_mark(d,190,354,270,CYAN)
text(d,(540,500),"TECHNOCORE",86,ICE,True,"lm")
text(d,(540,585),"PRIMARY DIGITAL LOCKUP",22,CYAN)
d.rectangle((104,800,1696,1300),fill=ICE,outline="#D9DDE1",width=3)
draw_mark(d,190,904,270,BLUE)
text(d,(540,1050),"TECHNOCORE",86,BASE,True,"lm")
text(d,(540,1135),"LIGHT / PRINT ALTERNATE",22,BLUE)
# palette and sizes
swatches=[("BASE",BASE),("CYAN",CYAN),("BLUE",BLUE),("GREEN",GREEN),("ICE",ICE)]
x=104
for n,c in swatches:
 d.rectangle((x,1400,x+200,1500),fill=c,outline="#D9DDE1")
 text(d,(x,1540),n,19,BASE,True)
 text(d,(x,1580),c,17,CANON_GREY)
 x+=235
text(d,(1696,1406),"SPACE MONO",24,BASE,True,"ra")
text(d,(1696,1455),"8 PX MODULE",22,CANON_GREY,False,"ra")
text(d,(1696,1504),"NO GRADIENT",22,CANON_GREY,False,"ra")
text(d,(1696,1553),"NO SHADOW",22,CANON_GREY,False,"ra")
text(d,(1696,1650),"Symbol remains legible from 24 px upward.",21,CANON_GREY,False,"ra")
save(img,"03-technocore-core-relay-system.png")

# 04 — Clean lockup image for direct submission
img=Image.new("RGB",(1800,1200),BASE); d=ImageDraw.Draw(img)
draw_mark(d,144,360,400,CYAN)
text(d,(650,558),"TECHNOCORE",108,ICE,True,"lm")
text(d,(650,680),"THE CORE RELAY",28,CYAN,False,"lm")
text(d,(900,1040),"COMMUNICATE  /  COMMERCE  /  MEMORY",24,GREY,False,"ma")
save(img,"04-technocore-primary-lockup.png")

# Transparent symbol exports
for size in (1024,512,256,64,24):
 img=Image.new("RGBA",(size,size),(0,0,0,0)); d=ImageDraw.Draw(img)
 draw_mark(d,0,0,size,CYAN)
 save(img,f"symbol-{size}px.png")

# monochrome proof
img=Image.new("RGB",(1200,1200),BASE); d=ImageDraw.Draw(img)
draw_mark(d,300,210,600,ICE)
text(d,(600,980),"ONE-COLOR PROOF",26,ICE,False,"ma")
save(img,"symbol-one-color-proof.png")
