#!/usr/bin/env python
import time
from urlparse import parse_qs as qs_decode
from urllib import urlencode as qs_encode
from tornado import escape
from plot import plotter
from tsdb import TSDb
import sys 


def tocsv( l ):
    x=''
    for e in l[:-1]:
        x=x+str(e)+','
    x = x+str(l[-1])
    return x

if __name__ == "__main__":
    db = TSDb('lego.xe.be',4242)
    det = ['ohain.weight{id=1}','ohain.weight{id=2}','ohain.weight{id=0}']
    name = ["r1","r2","r3"]
    data = db.query(sys.argv[1],None,det,'sum','10m-avg')
    l=[]
    for d in det:
        l.append(len(data[d][0]))
    min_l = min(l)
    print tocsv(['Date','r1','r2','r3'])
    for k in range(min_l):
        epo = data[det[0]][0][k]
        t = time.strftime('%Y/%m/%d %H:%M:%S',time.gmtime(epo))
        line = []
        line.append(t)
        for d in det:
            line.append(data[d][1][k])
        print tocsv(line)
