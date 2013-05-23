IRC bot documantation
=============
Step by step guide
-------------
Creating a bot wich pongs on command and says hi on join

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
>scope: PRIVMSG/NOTICE/"" wether the function will be called upon privmsg, notice or both
