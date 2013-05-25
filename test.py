from irctools import ircbot
from irctools.defines import *

class bot(ircbot.bot):
	nick = "Jesen"
	debug = True
	channel = "#FaceHunter"
	
	def lolcakes(self, info):
		print info
		print info["channel"]
		self.sendTo(info["channel"],str(info))
		
	def onStartup(self):
		self.registerCommand("test", self.lolcakes, PRIVMSG)
	
bot("irc.rizon.net")