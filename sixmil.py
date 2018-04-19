import sys
import socket
import string

HOST="irc.rizon.net"
PORT=6697
NICK="sixmil"
IDENT="6milliondollarbot"
REALNAME="Steve Austin"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER 6milliondollarbot garage.console bla :Steve Austin\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN #bots\r\n")

while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )

    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)

        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])
