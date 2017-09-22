#!/usr/bin/env python3
import zipfile
from PIL import Image, ImageColor

if __name__ == "__main__":

    im = Image.open('index.png')

    rgb_im = im.convert('RGB')

    last = ()
    chars = ''
    for pxl in im.getdata():
        if pxl[0] == pxl[1] and pxl[0] == pxl[2] and last != pxl:
            last = pxl
            chars += chr(pxl[0])



    print (chars)
    first = chars.index("[")
    values = (chars[first+1:-1]).split(", ")

    for member in values:
        print(chr(int(member)))
