import socket
from threading import Thread
from defines import *


class notSetError(Exception):
	pass
	
class dafuq(Exception):
	pass

class bot:
	debug = False
	enableConsoleInput = False
	channel = None
	prefix = "!"
	def __init__(self, server, port=6667, passwd = None):
		print "starting bot"
		self.commandList = {"PRIVMSG":{},"NOTICE":{}}
		self.serverIsSet = False
		self.port = port
		self.server = server
		self.passwd = passwd
		self.connect()
	
		if self.nick == None:
			raise notSetError, "You have to set a nick"
			
	def onStartup(self):
		pass
			
	def registerCommand(self,command,function, scope=""):
		if scope == "":
			
			self.commandList["PRIVMSG"][command] = function
			self.commandList["NOTICE"][command] = function
		elif scope is not "PRIVMSG" and scope is not "NOTICE":
			raise dafuq("Invalid scope when registering command ("+scope+")")
		else:
			self.commandList[scope][command] = function
				
		print "[DEBUG] Registered command "+self.prefix+command
		
	def getPrivmsgInfo(self, text):
		info = {}
		#>> :FaceHunter_!~FaceHunte@124DE4BB.C03EAC25.3A3F4334.IP PRIVMSG #FaceHunter :!lolcakes test test test
		info["command"] = text.split(PRE)[2].split()[0]
		info["user"] = {}
		info["user"]["nick"] = text.split(PRE)[1].split("!")[0]
		info["user"]["realname"] = text.split(PRE)[1].split("!")[1].split("@")[0]
		info["user"]["hostmask"] = text.split(PRE)[1].split()[0].split("@")[1]
		info["args"] = []
		try:
			print str(text.split(info["command"])[1].split("\r\n")[0].split())
			for arg in text.split(info["command"])[1].split("\r\n")[0].split():
				print "adding arg "+arg
				info["args"].append(arg)
		except IndexError:
			info["args"] = None
		info["channel"] = text.split()[2]
		return info
		
	def joinChan(self,channel):
		self.sock.send("JOIN "+channel+"\n")
		
	def sendTo(self,channel,text):
		self.sock.send("PRIVMSG "+channel+" :"+text+"\r\n")
		
	def noticeTo(self,nick,text):
		self.sock.send("NOTICE "+nick+" :"+text+"\r\n")
		
	def funcExec(self,function, args):
		function(args)
		
	def Connection(self):
		self.onStartup()
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.server,self.port))
		if self.passwd:
			self.sock.send("PASS "+self.passwd+"\n")
		self.sock.send("NICK "+self.nick+"\n")
		self.sock.send("USER "+self.nick+" "+self.nick+" "+self.nick+" "+self.nick+"\n")
		self.motd = False
		
		if type(self.channel).__name__ == 'str':
			self.joinChan(self.channel)
		elif type(self.channel).__name__ == 'list':
			for x in self.channel:
				self.joinchan(x)
		else:
			raise dafuq("yo dawg what are you doing? it should be str or list")
		
		while 1:
			text = self.sock.recv(2048)
			text=text.split("\r\n")
			for line in text:
				if line.startswith("PING"):
					sub = line.split("PING ")[1]
					self.sock.send("PONG "+sub)
				if not line.startswith(":"): #==rubbish
					continue

				if self.debug == True:
					print line
					
				try:
					serveraction = line.split()[1]
				except:
					print "error "+line
					
				if serveraction == PRIVMSG:
			# if "PRIVMSG" in text and not text.startswith(":irc."):
					if line.split(PRE)[2].startswith(self.prefix):
						info = self.getPrivmsgInfo(line)
						if info["command"].strip(self.prefix) in self.commandList["PRIVMSG"]:
							func = self.commandList["PRIVMSG"][info["command"].strip(self.prefix)]
							print "[DEBUG] Found command %s, executing function %s" % (info["command"].strip(self.prefix), func.__name__)
							function = Thread(target=self.funcExec, args = (func,info) )
							function.start()
						else:
							print "[DEBUG] Command %s not in list!" % info["command"]
							print str(self.commandList["PRIVMSG"])
		
	def connect(self):
		if not self.server:
			raise notSetError( "You must execute this command with a valid IRC server" )
		self.conn = Thread(target=self.Connection)
		self.conn.start()
