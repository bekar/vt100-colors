# vt100-colors

Since there is enough packages in [pipy][pipy] dealing with the color output in terminal which i found after my own implimentation and found mine is cooler!

![screenshot][screenshot]

## HOW-TO-RUN

```bash
$ make
```

### Technical [:link:][ecma]

SGR is used to establish one or more graphic rendition aspects for
subsequent text.  The established aspects remain in effect until the
next occurrence of SGR in the data stream, depending on the setting of
the GRAPHIC RENDITION COMBINATION MODE (GRCM). Each graphic rendition
aspect is specified by a parameter value:


0	 default, cancels any preceding SGR regardless GRCM
1	 bold or increased intensity
2	 faint, decreased intensity or second colour
3	 italicized
4	 singly underlined
5	 slowly blinking (less then 150 per minute)
6	 rapidly blinking (150 per minute or more)
7	 negative image
8	 concealed characters
9	 crossed-out
10	 primary (default) font
11	 first alternative font
12	 second alternative font
13	 third alternative font
14	 fourth alternative font
15	 fifth alternative font
16	 sixth alternative font
17	 seventh alternative font
18	 eighth alternative font
19	 ninth alternative font
20	 Fraktur (Gothic)
21	 doubly underlined
22	 normal colour or normal intensity (neither bold nor faint)
23	 not italicized, not fraktur
24	 not underlined (neither singly nor doubly)
25	 steady (not blinking)
26	 reserved for proportional spacing
27	 positive image
28	 revealed characters
29	 not crossed out
30	 black display
31	 red display
32	 green display
33	 yellow display
34	 blue display
35	 magenta display
36	 cyan display
37	 white display
38	 reserved for future standardization
39	 default display colour
40	 black background
41	 red background
42	 green background
43	 yellow background
44	 blue background
45	 magenta background
46	 cyan background
47	 white background
48	 reserved for future standardization
49	 default background colour
50	 reserved
51	 framed
52	 encircled
53	 overlined
54	 not framed, not encircled
55	 not overlined
56	 reserved
57	 reserved
58	 reserved
59	 reserved
60	 ideogram underline or right side line
61	 ideogram double underline or double line on the right side
62	 ideogram overline or left side line
63	 ideogram double overline or double line on the left side
64	 ideogram stress marking
65	 cancels the effect of the rendition aspects established by parameter values 60 to 64

[ecma]: http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
[pipy]: https://pypi.python.org/pypi
[screenshot]: https://raw.github.com/haude/vt100-colors/dump/images/screenshot.png
