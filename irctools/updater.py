import urllib
import os
def check(currversion):
	print os.getcwd()
	currversion = currversion.split(".")
	a=[]
	for x in currversion:
		a.append(int(x))
	currmain=a[0]
	currmajor=a[1]
	currminor=a[2]
	currfix=a[3]
	
	newversion = urllib.urlopen("https://raw.github.com/FaceHunter/IRCtools/master/version.txt").read().strip("\n").split(".")
	b=[]
	for x in newversion:
		b.append(int(x))
	newmain=b[0]
	newmajor=b[1]
	newminor=b[2]
	newfix=b[3]
	
	if newmain > currmain or newmajor > currmajor or newminor > currminor or newfix > currfix:
		print "A new version is available("+'.'.join(newversion)+")\nWould you like to download now?"
		while 1:
			ans = raw_input("Y/N: ").upper()
			if ans == "Y":
				update()
				break
			if ans == "N":
				break
			else:
				print "._."
				
def update():
	ircbot_py = urllib.urlopen("https://raw.github.com/FaceHunter/IRCtools/master/irctools/ircbot.py").read()
	print os.getcwd()
	f=open("irctools\ircbot.py","r")
	ircbot_py_r = f.read()
	f.close()
	if ircbot_py != ircbot_py_r:
		f = open("irctools\ircbot.py","w")
		f.write(ircbot_py)
		f.close()