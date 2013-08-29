# vt100-colors

Since there is enough packages in [pipy][pipy] dealing with the color output in terminal which I discovered after my own implimentation and found mine was cooler!

![screenshot][screenshot]

#### HOW-TO-RUN

Run it in the the terminal supporting [vt100][vt100] (i.e. `gnome-terminal`, `xterm`, `lxterminal`) and execute the word given below:

```bash
$ make
```

**NOTE**: Some of the mode are not supported in `yakuake`, `konsole` & `emacs shell`

#### Technical

SGR is used to establish one or more graphic rendition aspects for subsequent text. The established aspects remain in effect until the
next occurrence of SGR in the data stream, depending on the setting of the GRAPHIC RENDITION COMBINATION MODE (GRCM).


#### Read more

 - [ANSI codes][ansi]
 - [Ecma-048][ecma]
 - [VT100][vt100]

[vt100]: http://en.wikipedia.org/wiki/VT100
[ecma]: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
[pipy]: https://pypi.python.org/pypi
[screenshot]: https://raw.github.com/haude/vt100-colors/dump/images/screenshot.png
[ansi]: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
