"""
"
" WiFi Server for LinkIt One
"
" LTerminal.py
"
" Author: Muchiri John
" Feb 05 2015
"
"""
from libs.board import *

import socketserver
import sys
import time
import socket

s = scratch_n_sketch()

HOST, PORT = socket.gethostbyname(socket.gethostname()), 2215

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        try:
            self.data = str(self.rfile.readline().strip())
            #print("{} wrote:".format(self.client_address[0]))
            if len(self.data) < 0:
                return
            self.header = self.data#.indexOf(0, len(self.data))
            #print(self.header + '\n')
            gt = self.header.find('GET ')
            #print(gt)
            if (gt != 2):
                #print('This server only handles HTTP GET requests')
                return
            i = self.header.find('HTTP/1.1')
            if i < 0:
                return
            self.header = self.header[7 : (i - 1)]
            if len(self.header) == 0:
                self.doHelp()
            elif self.header == 'favicon.ico':
                return
            else:
                try:
                    hd = self.decodeUrl(str(self.header))
                    #if (not hd == 'poll'):
                    #self.client_address[0]
                    cr = time.strftime('%H:%M:%S', time.localtime())
                    console(str('{} --> {}'.format(cr, hd)))
                    #self.processCommands(self.header)
                    #self.sendResponse(hd)
                    if(hd == 'on'):
                        s.ledWrite(Red, On)
                        self.sendResponse('LED on')
                    elif(hd == 'off'):
                        s.ledWrite(Red, Off)
                        self.sendResponse('LED off')
                    else:
                        self.sendResponse('Connected')
                except:
                    self.sendResponse('Sorry. Message not understood by server')
        except:
            print('Error occured while reading request')

    #send response
    def sendResponse(self, response):
        crlf = '\r\n'
        httpResponse = 'HTTP/1.1 200 OK' + crlf
        httpResponse += 'Content-Type: text/html; charset=ISO-8859-1' + crlf
        httpResponse += 'Access-Control-Allow-Origin: *' + crlf
        httpResponse += crlf
        httpResponse += response + crlf
        self.wfile.write(bytes(httpResponse, 'utf8'))


    #process command
    def processCommands(self, command):
        #linkit commands
        response = 'Okay:'
        parts = info.split('/')
        cmd = command[0]
        cmdData = ''
        #send if data to linkit if a poll request is sent
        if cmd == 'poll': #reset
           pass
        #print command issued
        elif cmd == 'print':
            pass
        #println command issued
        elif cmd == 'println':
            pass
        #send a response to server [command]
        self.sendResponse(response)

    def doHelp(self):
        # Optional: return a list of commands understood by this server
        help = 'LinkIt SERVER'
        self.sendResponse(help)

    #do some url decoding
    def decodeUrl(self, url):
        try:
            data = url.split('%')
            str = ''
            ch = ''
            for x in range(0, len(data), 1):
                if (not (url.startswith('%'))) and x == 0:
                    str += data[x]
                else:
                    if (len(data[x]) >= 2):
                        ch = format('%c' % int(data[x][:2], 16))
                        if (len(data[x]) > 2):
                            str += ch + data[x][2:]
                        else:
                            str += ch
                    else:
                        str += data[x]
            return str
        except:
            print('failed to decode data')
            return ''

if __name__ == "__main__":
    #check if host defined
    try:
        host = str(sys.argv[1]);
        if((len(host) >= 9) and (len(host.split('.') == 4))):
            HOST = str(sys.argv[1])
    except:
        #if not defined use default
        pass

    try:
        # Create the server, binding to host on port 2215
        server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
        #connect Scratch_n_sketch
        s.connect()
        #print server status
        console('\n\n|-----------------------------|')
        console('\n--> Scratch_n_sketch Server')
        console('\n--> Terminal started at HOST: \n%s PORT : %s' % (HOST, PORT))
        console('\n|-------------------------------|')
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    except:
        console('\n-- Failed to connect.\n')
