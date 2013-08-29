#!/usr/bin/python3

fontstyle = [ #TODO Long names
    "default", "bold", "faint", "italic", "underline", "blink", "rapid-blink",
    "negative", "hide", "strike-out"
]

fstyle = [
    'r', 'b', 'f', 'i', 'u', 'w', 'y', 'n', 's',
    'x'
]

pallet8 = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
    "magic", "default", # magic: enable 256 color
]

restore=["", 'r', ""]

def mix(color1, color2=restore): #shifting colors
    style=""
    for s1 in color1[1]:
        if s1 in color2[1]: continue;
        style+=s1

    style+=color2[1]
    return [color1[2], style, color2[2]]

def modify(color, style=None, bg=None, fg=None):
    if fg: color[0]=fg
    if style: color[1]=style
    if bg: color[2]=style
    return color

def addstyle(color, style=None):
    if style: color[1]+=style
    return color

def paint(c=restore):
    if c=="": return ""

    def getcode(c, shift):
        if isinstance(c, int): return str("%d;5;%d"%(8+shift, c))
        if c== "" or c=="def": return ""
        return str(pallet8.index(c)+shift)

    fg=getcode(c[2], 30)
    color=fg
    bg=getcode(c[0], 40)
    if color and bg: color+=';'
    color+=bg

    style=""
    for i in c[1]:
        style+=str(fstyle.index(i))+';'

    if color and style: color+=';'
    return '\x1b['+color+style[:-1]+'m'

def pick(fg="", style="", bg=""):
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
            color=pick(pallet8[i], "b", pallet8[7-j])
            print("%s%8s"%(paint(color), pallet8[i]), end="")
        print(paint())

def colortable256():
    count=1
    for i in range(16):
        color=pick(bg=i)
        print("%s%4d"%(paint(color), i), end="")
        if count==8: print(paint()); count=0
        count+=1

    for i in range(16,256):
        color=pick(bg=i)
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
    color5=pick(31, "bx")
    print(color5, paint(color5), "mixed", paint(), "world")

if __name__=="__main__":
    colortest()
    colortable8()
    colortable256()
