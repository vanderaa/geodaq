#!/usr/bin/env python
import tornado.ioloop
import tornado.web
from urlparse import parse_qs as qs_decode
from urllib import urlencode as qs_encode
from tornado import escape
from plot import plotter
from tsdb import TSDb

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_status(200)
        self.set_header("Content-Type", "image/svg+xml")
        db = TSDb('lego.xe.be',4242)
        det = ['ohain.temp','ohain.weight{id=1}','ohain.weight{id=2}','ohain.weight{id=0}']
        query = qs_decode(self.request.query)
        print query['start']
        data = db.query(query['start'][0],None,det,'sum','10m-avg')
#        print data


        self.finish(plotter(data))

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8080,'0.0.0.0')

    print("localhost:8080")

    tornado.ioloop.IOLoop.instance().start()
