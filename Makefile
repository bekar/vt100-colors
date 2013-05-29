#export TERM=xterm-256color

current: 256colors

256colors:
	TERM=xterm-256color ./colors.py

8colors:
	./colors.py

python2:
	sed '/print/s/end=""//g' colors.py > color2.py
