# -*- coding: utf-8 -*-
import re
from PIL import Image, ImageDraw, ImageFont
import sys
import os

css = open('css\\font-awesome.css').read()
regex = re.compile(r'\.([a-zA-Z-]+)[\s\S]+?\\(\w+)')
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
    max = len(fonts)
    i = 0
    print('正在转换..')
    for k,v in fonts.items():
        image = Image.new("RGBA", (s,s), (0,0,0,0))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("fonts\\fontawesome-webfont.ttf", s-2)
        draw.text((1,1),v, font=font, fill=c)
        box = image.getbbox()
        print(box)
        # image.save(dir + "\\" + k + ".png")
        # i += 1
        # myprint(i, max)
    print("\nDone")

def myprint(i, max):
    a = i * 100 // max
    b = (max - i) * 100 // max
    s = str(i) + " of " + str(max)
    l = len(s)
    sys.stdout.write('' * 130 + '\r')
    sys.stdout.flush()
    sys.stdout.write('%s[%s%s]'%(s, '*' * a, ' ' * b))
    sys.stdout.flush()




if __name__ == "__main__":
    print("搜索 575904952 领个红包吧")
    main(sys.argv)
