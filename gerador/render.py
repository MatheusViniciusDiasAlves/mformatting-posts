import json, sys, os
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1350
BG=(13,17,23); FG=(240,244,248); MUTED=(139,148,158); ACC=(34,211,238); CARD=(22,27,34); LINE=(33,38,45)
P="/usr/share/fonts/truetype/google-fonts/"; I="/usr/share/fonts/opentype/inter/"
f_title=ImageFont.truetype(P+"Poppins-Bold.ttf",76)
f_item=ImageFont.truetype(I+"Inter-Medium.otf",38)
f_num=ImageFont.truetype(P+"Poppins-Bold.ttf",34)
f_tag=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",30)
f_foot=ImageFont.truetype(P+"Poppins-Medium.ttf",32)
f_small=ImageFont.truetype(I+"Regular.otf" if False else I+"Inter-Regular.otf",26)
def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines
def render(p,out):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    for x in range(0,W,54): d.line([(x,0),(x,H)],fill=(17,22,29))
    for y in range(0,H,54): d.line([(0,y),(W,y)],fill=(17,22,29))
    M=84
    d.rectangle([0,0,W,10],fill=ACC)
    d.text((M,92),p["tag"],font=f_tag,fill=ACC)
    y=150
    for ln in wrap(d,p["title"],f_title,W-2*M):
        d.text((M,y),ln,font=f_title,fill=FG); y+=94
    y+=40
    for i,it in enumerate(p["items"],1):
        lines=wrap(d,it,f_item,W-2*M-150)
        h=max(110,40+len(lines)*50)
        d.rounded_rectangle([M,y,W-M,y+h],radius=22,fill=CARD,outline=LINE,width=2)
        cx,cy=M+58,y+h//2
        d.ellipse([cx-32,cy-32,cx+32,cy+32],fill=ACC)
        n=str(i); tw=d.textlength(n,font=f_num); d.text((cx-tw/2,cy-25),n,font=f_num,fill=BG)
        ty=y+(h-len(lines)*50)//2+2
        for ln in lines: d.text((M+120,ty),ln,font=f_item,fill=FG); ty+=50
        y+=h+20
    d.line([(M,H-130),(W-M,H-130)],fill=LINE,width=2)
    d.text((M,H-105),"@mformatting",font=f_foot,fill=FG)
    t="Rolândia · PR"; d.text((W-M-d.textlength(t,font=f_small),H-97),t,font=f_small,fill=MUTED)
    assert y < H-150, (p["slug"], y)
    im.save(out,optimize=True)
posts=json.load(open(sys.argv[1])); os.makedirs(sys.argv[2],exist_ok=True)
for p in posts: render(p,os.path.join(sys.argv[2],p["slug"]+".png")); print("ok",p["slug"])
