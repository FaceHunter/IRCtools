from irctools import ircbot

class bot(ircbot.bot):
	nick = "Jesen"
	debug = True
	channel = "#FaceHunter"
	
bot("irc.rizon.net")