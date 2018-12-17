# -*- coding: utf-8 -*-
import re
from PIL import Image, ImageDraw, ImageFont
import sys
import os

css = open('css\\font-awesome.css').read()
regex = re.compile(r'\b(fa-[\w-]+)[\s\S]{22}\\(\w+)')
fonts = {}
for t in regex.findall(css):
    fonts[t[0]] = chr(int(t[1], 16))


def main(args):
    r = {'size':50, 'color':'#000000'}
    for arg in args[1:]:
        t = arg.split('=')
        r[t[0]] = t[1]
    s = int(r['size'])
    c = r['color']
    dir = "png_" + str(s) + "_" + str(c)
    os.mkdir(dir)
    length = len(fonts)
    i = 0
    print('正在转换..')
    for k,v in fonts.items():
        image = Image.new("RGBA", (s*3,s*3), (0,0,0,0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("fonts\\fontawesome-webfont.ttf", s)
        draw.text((s,s),v, font=font, fill=c)
        box = image.getbbox()

        w = box[2] - box[0]
        h = box[3] - box[1]
        l = max(w,h)
        nfs = s * s // l - 2
        image = Image.new("RGBA", (s*3,s*3), (0,0,0,0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("fonts\\fontawesome-webfont.ttf", nfs)
        draw.text((s,s),v, font=font, fill=c)
        box = image.getbbox()
        w = box[2] - box[0]
        h = box[3] - box[1]
        l = max(w,h)
        box = ( box[0] - ( s - w )//2,
                box[1] - ( s - h )//2,
                box[0] - ( s - w )//2 + s,
                box[1] - ( s - h )//2 + s)
        image = image.crop(box)
        image.save(dir + "\\" + k + '.png')
        i += 1
        myprint(i,length)

    print("\nDone")

def myprint(i, length):
    a = i * 100 // length
    b = (length - i) * 100 // length
    s = str(i) + " of " + str(length)
    l = len(s)
    sys.stdout.write('' * 130 + '\r')
    sys.stdout.flush()
    sys.stdout.write('%s[%s%s]'%(s, '*' * a, ' ' * b))
    sys.stdout.flush()




if __name__ == "__main__":
    print("搜索 575904952 领个红包吧")
    main(sys.argv)
