import socket
from threading import Thread

class notSetError(Exception):
	pass
	
class dafuq(Exception):
	pass

class bot:
	debug = False
	enableConsoleInput = False
	nick = None
	channel = None
	def __init__(self, server, port=6667, passwd = None)
		print "starting bot"
		self.commandList = {}
		self.debug = False
		self.serverIsSet = False
		self.port = port
		self.server = server
		self.passwd = passwd
		self.connect()
	
		if self.nick == None:
			raise notSetError, "You have to set a nick"
			
			
	def onStartup(self):
		"""all yo niggerdix should register stuffs here"""
		
	def joinChan(self,channel):
		self.sock.send("JOIN "+channel+"\n")
			
	def identText(self, text):
		channel = "#"+text.split("#")[1].split()[0]
		nick = text.split('!')[0].strip(':')
		command = text.split(":")[2].split()[0]
		args = text.split(command)[1].split("\r\n")[0].split()
		return channel, nick, command, args
		
	def Connection(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.server,self.port))
		if self.passwd:
			self.sock.send("PASS "+self.passwd+"\n")
		self.sock.send("NICK "+self.nick+"\n")
		self.sock.send("USER "+self.nick+" "+self.nick+" "+self.nick+" "+self.nick+"\n")
		
		if type(self.channel).__name__ == 'str':
			self.joinChan(self.channel)
		elif type(self.channel).__name__ == 'list':
			for x in self.channel:
				self.joinchan(x)
		else:
			raise dafuq("yo dawg what are you doing? it should be str or list")
		
		while 1:
			text = self.sock.recv(1024)
			if self.debug:
				print text
			if "PRIVMSG" in text:
				channel, nick, command, args = self.identText(text)
				if command in self.commandList:
					func = self.commandList[command]
					function = Thread(target=self.func, args = () )
					function.start()
		
	def connect(self):
		if not self.server:
			raise notSetError( "You must set execute this command with an valid IRC server" )
		self.conn = Thread(target=self.Connection)
		self.conn.start()
