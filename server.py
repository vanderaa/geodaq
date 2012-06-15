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
        self.set_header("Content-Type", "image/png")
        db = TSDb('lego.xe.be',4242)
        data = db.query('2011/06/09-12:00:00',None,['ohain.temp','ohain.adc{id=14}'],'sum','1h-avg')
        query = qs_decode(self.request.query)



        self.finish(plotter(data))

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8080)

    print("localhost:8080")

    tornado.ioloop.IOLoop.instance().start()
