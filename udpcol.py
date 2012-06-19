#!/usr/bin/env python

import socket
import json
import telnetlib
import time 
import yaml

socks = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socks.bind(('',3001))
#socks.bind(('',9876))

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


def calibrate( fname, data ):
    f = open(fname,'r');
    cal = yaml.load(f)
    print cal
    f.close()
    # For each element in data se
    # if we have a element to calibrate
    if( cal ):
        # make sure there is no none
        for k,v in zip(cal.keys(),cal.values()):
            if( not v ):
                cal[k]={} 
        for metric in set(cal.keys()) & set(data.keys()):
            for idx in set(cal[metric]) & set(range(len(data[metric]))):
                f = lambda x: eval(cal[metric][idx])            
#            print metric,idx,cal[metric][idx],f
            # Now calibrate
                data[metric][idx]=f(data[metric][idx])
#            print data

while True:
    data,addr = socks.recvfrom(1024)
    data = json.loads(data)
    # We need to calibrate the data
    print data
    ts = int(time.time())
    calibrate('cal.yaml',data)
    print data
    queue.append((ts,data))
    print '.', 
    if(len(queue) > 20 ):
        print 'P'
#        publish('localhost',4242,queue)
