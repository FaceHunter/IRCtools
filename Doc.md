IRC bot documantation
=============
Step by step guide
-------------
Creating a bot wich pongs on command

<b>Make sure you installed everything correctly</b>

start by importing the module

    from irctools import ircbot

Create a class with any name

    class MyBot(ircbot.bot):
    
Define some required vars

    nick = "MyBot"
    channel = "#MyChannel" #or ["#MyFirstChannel","MyOtherChannel"]

Create an onStartup() function where we can register our commands

    def onStartup():
    
For this example we will register the command !ping

> self.registerCommand(command, function, scope=None)

    self.registercommand("ping", self.ping, PRIVMSG)
    
>command: the command without prefix
>function: the function wich will be called when command occurs (without ())
>scope: PRIVMSG/NOTICE wether the function will be called upon privmsg or notice, leave open when you want both


Now with that done we can start creating our function!

    def ping(self, info): #as we registered that at self.registerCommand()
        nick = info["user"]["nick"] #Gets the nick from the info dict
        channel = info["channel"] #Gets the channel from the info dict
        self.sendTo(channel, "pong "+' '.join(info["args"]) #returns all given args
        
<b>The info object:<b/>

    {
        'args': [], #Arguments go in here word by word (list is empty when no args)
        'command': '', #Command used
        'user': #WARNING nested
            {
            'nick': '', #The nickname of the user executing the command
            'realname': '', #The real name of the user executing the command
            'hostmask': '' #The hostmask of the user executing the command
            }, 
        'channel': '' #channel in wich the command is executed
    }
    
Finally at the bottom of the script we have to start everything

    MyBot("irc.rizon.net",6667)
