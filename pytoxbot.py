#!/usr/bin/env python
import socket

network = 'irc.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK pytoxbot\r\n')
irc.send ( 'USER pytoxbot pytoxbot pytoxbot :pytox bottykins\r\n' )
irc.send ( 'JOIN #python-forum\r\n' )
while True:
    data = irc.recv ( 4096 )
    if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    if data.find ( '?pytoxbot quit' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :Fine, if you dont want me\r\n' )
      irc.send ( 'QUIT\r\n' )
    if data.find ( '?hi pytoxbot' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :I already said hi...\r\n' )
    if data.find ( '?KICK' ) != -1:
      irc.send ( 'JOIN #python-forum\r\n' )
    if data.find ( '?pie' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :WHERE!!!!!!\r\n' )
    if data.find ( '?spam pytoxbot' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
    if data.find ( '?joke' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :Knock Knock\r\n')
    if data.find ( 'whos there' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :Canoe\r\n')
    if data.find ( 'canoe who') != -1:
      irc.send ( 'PRIVMSG #python-forum :Canoe let me in\r\n' )
    if data.find ( '?commands' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :PING, ?hi pytoxbot, ?quit pytoxbot, ?pie, ?spam pytoxbot, ?joke, ?source, ?help\r\n')
    if data.find ( '?source' ) != -1:
      irc.send ( 'PRIVMSG #python-forum :http://code.google.com/p/pytoxbot/\r\n' )
    if data.find ( '?help' ) !=-1:
      irc.send ( 'PRIVMSG #python-forum :If you need help on one of my commands please type help yourcommand\r\n' )
    if data.find ( 'help pytoxbot quit' ) !=-1:
      irc.send ( 'PRIVMSG #python-forum :command that makes me quit\r\n' )
    if data.find ( 'help hi pytoxbot' ) !=-1:
      irc.send ( 'PRIVMSG #python-forum :a command that says hello to me\r\n' )
    if data.find ( 'help pie' ) !=-1:
      irc.send ( 'PRIVMSG #python-forum :a command that is absolutely useless\r\n' )
    if data.find ( 'help spam pytoxbot' )!=-1:
      irc.send ( 'PRIVMSG #python-forum :a command that makes me say something random\r\n' )
    if data.find ( 'help joke' )!=-1:
      irc.send ( 'PRIVMSG #python-forum:a command that makes me say a joke\r\n' )
    if data.find ( 'help commands' )!=-1:
      irc.send ( 'PRIVMSG #python-forum :function that lists or my commands\r\n' )
    if data.find ( 'help source' )!=-1:
      irc.send ( 'PRIVMSG #python-forum :function that lists the link to my source\r\n' )
    print data

    
    

