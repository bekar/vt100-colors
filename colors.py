#!/usr/bin/python

# SGR - SELECT GRAPHIC RENDITION
# http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
# Section 8.3.117; Pg 61

# program has been written in python3
# for python2 run sed command as
# sed '/print/s/, \?end="")/),/g' colors.py > color2.py


# from os import environ as env
# TERM=env["TERM"]

fstyle = [
    'r', #0 regular
    'b', #1 bold
    'f', #2 faint
    'i', #3 italic
    'u', #4 underline
    'w', #5 blink
    'y', #6 blink2
    'n', #7 negative
    's', #8 concealed
    'x', #9 crossed
]

pallet = [
    "black",   # 30
    "red",     # 31
    "green",   # 32
    "yellow",  # 33
    "blue",    # 34
    "magenta", # 35
    "cyan",    # 36
    "white",   # 37
    "magic",   # 38 enable 256 color
    "def",     # 39 default foreground color
]

restore=["", 'r', ""]

def mix(color1, color2=restore):
    style=""
    for s1 in color1[1]:
        if s1 in color2[1]: continue;
        style+=s1

    style+=color2[1]

    return [color1[0], style, color2[0]]

def paint(c=restore):
    if c=="": return ""

    def getcode(c, shift):
        if isinstance(c, int): return str("%d;5;%d"%(8+shift, c))
        if c== "" or c=="def": return ""
        return str(pallet.index(c)+shift)

    fg=getcode(c[0], 30)
    color=fg
    bg=getcode(c[2], 40)
    if color and bg: color+=';'
    color+=bg

    style=""
    for i in c[1]:
        style+=str(fstyle.index(i))+';'

    if color and style: color+=';'
    return '\x1b['+color+style[:-1]+'m'

def pick(bg="def", style="", fg=""):
    # TODO: error handeling
    # try:
    #     pallet[bg]
    # except e:
    #     Exception("No color found")
    # if 0<=c<=255:
    return [bg,style,fg]

def colortable8():
    for i in range(8):
        for j in range(8):
            color=pick(pallet[i], "b", pallet[7-j])
            print("%s%8s"%(paint(color), pallet[i]), end="")
        print(paint())

def colortable256():
    count=1
    for i in range(16):
        color=pick("black", "", i)
        print("%s%4d"%(paint(color), i), end="")
        if count==8: print(paint()); count=0
        count+=1

    for i in range(16,256):
        color=pick("black", "", i)
        print("%s%4d"%(paint(color), i), end="")
        if count==6: print(paint()); count=0
        count+=1

def colortest():
    color1=pick("green", 'f')
    print(color1, paint(color1), "hello", paint(), "world")
    color1=pick("green", 'b')
    print(color1, paint(color1), "hello", paint(), "world")
    color1=pick("green")
    print(color1, paint(color1), "hello", paint(), "world")

    color2=pick("red", "b")
    print(color2, paint(color2), "colorful", paint(), "world")
    color3=mix(color2, color1)
    print(color3, paint(color3), "mixed", paint(), "world")
    color4=mix(pick("cyan", "iub"), pick("red", "iux"))
    print(color4, paint(color4), "mixed", paint(), "world")
    color5=pick(31)
    print(color5, paint(color5), "mixed", paint(), "world")


if __name__=="__main__":
    colortest()
    colortable8()
    colortable256()
