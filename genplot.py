#!/usr/bin/env python
import tornado.ioloop
import tornado.web
from urlparse import parse_qs as qs_decode
from urllib import urlencode as qs_encode
from tornado import escape
from plot import plotter
from tsdb import TSDb
import sys 

if __name__ == "__main__":
    print sys.argv
    db = TSDb('lego.xe.be',4242)
    det = ['ohain.temp','ohain.weight{id=1}','ohain.weight{id=2}','ohain.weight{id=0}']
    data = db.query(sys.argv[1],None,det,'sum','10m-avg')
    plotter(data,sys.argv[2])
