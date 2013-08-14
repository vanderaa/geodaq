#!/usr/bin/env python

import socket
import json
import telnetlib
import time 
import yaml
import sys
import urllib

socks = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socks.bind(('',3001))
#socks.bind(('',9876))

queue = []
cnt =0
prev_addr = ''

def publish(host, port, ts, data ):
    t = telnetlib.Telnet(host, port)
    query =''
    for k in data.keys():
        i = 0
        for v in data[k]:
            query = query   + 'put ' + \
                    str(k)  + ' '    + \
                    str(ts) + ' '    + \
                    str(v)  + ' '    + \
                    'id='   + str(i) + '\n'
            i=i+1
    t.write(query)
    t.close()
    #print query
#    for q in z:
#        ts = q[0]
#        d  = q[1]
#        ss = 'put cam.temp '+str(ts)+' '+str(d['TempCambridge'])+' id=0\n'
#        t.write(ss);
#        print ss, 
#    t.close()
#    z[:] = []
def dns_update( addr, data ):
    global prev_addr
    addr = addr[0]
    name = data.keys()
    name = name[0].split('.')
    name = name[0]
    print 'name is',name
    print 'addr is',addr
    print 'prev_addr',prev_addr
    if( name == 'ohain' and addr!=prev_addr ):
        print 'updating dns with addr=', addr 
        try:
            p = urllib.urlencode({'':'SnhPeWtvYTZUVHVkM3JPN3VDbnQ6Nzc0OTA4MA==','address':addr})
            f = urllib.urlopen('http://freedns.afraid.org/dynamic/update.php?%s'%p)
            print f.read()
            prev_addr = addr
        except e:
            print e


def calibrate( fname, data ):
    f = open(fname,'r');
    cal = yaml.load(f)
#    print cal
    f.close()
    print data
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
    print data

while True:
    cnt = cnt+1
    data,addr = socks.recvfrom(1024)
    data = json.loads(data)
    # We need to calibrate the data
    print addr
    ts = int(time.time())
    calibrate('cal.yaml',data)
    publish('localhost',4242, ts, data)
    dns_update(addr,data)
    sys.stdout.write('.')
    sys.stdout.flush()
    if( cnt == 20 ):
        sys.stdout.write(str(ts)+'\n')
        cnt = 0
#    if(len(queue) > 20 ):
#        print 'P'
#        publish('localhost',4242,queue)
