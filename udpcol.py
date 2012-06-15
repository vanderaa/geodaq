#!/usr/bin/env python

import socket
import json
import telnetlib
import time 

socks = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socks.bind(('',9876))

queue = []

def publish(host, port, z ):
    t = telnetlib.Telnet(host, port)
    for q in z:
        ts = q[0]
        d  = q[1]
        ss = 'put cam.temp '+str(ts)+' '+str(d['TempCambridge'])+' id=0\n'
        t.write(ss);
#        print ss, 
    t.close()
    z[:] = []


while True:
    data,addr = socks.recvfrom(1024)
    data = json.loads(data)
    ts = int(time.time())
    queue.append((ts,data))
    print '.', 
    if(len(queue) > 20 ):
        print 'P'
        publish('localhost',4242,queue)
