#export TERM=xterm-256color

current: 256colors

256colors:
	TERM=xterm-256color ./main.py

8colors:
	./main.py

python2:
	sed '/print/s/end=""//g' main.py > color2.py
