#!/usr/bin/env python


import telnetlib 
import time
import socket


def acquire_onewire(c, serial, Type, idx, channel):
    # First of all get the connection parameters
    (host,port) = c.get_socket().getpeername()
    try:
        print 'acquiring'
        c.write('r1wd '+repr(idx)+' '+repr(channel)+'\n')
        tem = c.read_until('\n')
        tem = float(tem.split()[-1])
        return tem
    except EOFError:
        print 'could not acquire adding' 
        c.close()
        c = telnetlib.Telnet(host,port)
        ost = 'a1wd '+repr(serial)+' '+repr(Type)+' '+repr(idx)+'\n'
        print ost
        c.write(ost)
        tem = c.read_until('\n')
        if( tem ):
            c.write('r1wd '+repr(idx)+' '+repr(channel)+'\n')
            try:
                tem = c.read_until('\n')
                tem = float(tem.split()[-1])
                print 'got the data'
                return tem
            except EOFError:
                c = telnetlib.Telnet(host,port)
                print 'reconncet'
                return None

def acquire_data(host, port):
    try:
        c = telnetlib.Telnet(host,port)
        c.write('radc\n')
        adc = c.read_until('\n')
        adc = adc.split()
        adc = map(float,adc[1:])
        tem = acquire_onewire(c,'1234567','ds1920',0,0)
        # now read the temp sensor 
        #c.write('r1wd 0 0\n')
        #tem = c.read_until('\n')
        #tem = tem.split()
        #tem = float(tem[-1])
        c.close()
        return (adc,tem) 
    except socket.error:
        print 'socket timeout on acquire'
        return None

def store_data(host, port, (data, tem)):
    try:
        c = telnetlib.Telnet(host,port)
        t = int(time.time())
        for k in range(len(data)):
            request = "put ohain.adc"+" "+str(t)+" "+str(data[k])+" "+"id="+str(k)
            c.write(request+'\n')
#            print "put ohain.adc"+" "+str(t)+" "+str(data[k])+" "+"id="+str(k)
        if( tem )
            request = "put ohain.temp"+" "+str(t)+" "+str(tem)+" "+"id=0"
            c.write(request+'\n')
        c.close()
    except socket.error:
        print 'socket timeout on store'
        return


def main(args): 
    while(1):
        data = acquire_data('ohain.xe.be',3000)
        print data
        if( data ):
            store_data('127.0.0.1',4242,data)
        time.sleep(10)


main(None)
