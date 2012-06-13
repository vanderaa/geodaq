import gviz_api
import pymongo 
import sys
import json
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.web.static import File
import datetime 
import time

class BeQuery(Resource):
    isLeaf = True
    def __init__(self, bees):
        Resource.__init__(self)
        self.bees=bees
    def render_GET(self, request):
        print request.args
        start=request.args['start'][0]
        stop=request.args['stop'][0]
        tqx=request.args['tqx'][0]
        reqID=tqx.split(':')[1]
#        print start
#        stop=self.get_argument('stop')
        print start, stop, reqID
        data=[]
        st=datetime.datetime.strptime(start,'%d-%m-%Y')
        et=datetime.datetime.strptime(stop,'%d-%m-%Y')
        sepoch = time.mktime(st.timetuple())
        eepoch = time.mktime(et.timetuple())
 	description = {"time": ("datetime", "time"),
        	       "value": ("number", "value")} 
        query={"timestamp": {"$gt": sepoch, "$lt": eepoch}, 'detector':'Ruche 6'}
        opt={'timestamp':1,'data':1}
        for m in self.bees.find(query,opt):
	    epoch = datetime.datetime.fromtimestamp(m['timestamp'])
	    data.append({'time':epoch,'value':m['data']})
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)
        request.setHeader("Content-Type", "text/plain; charset=utf-8")
        return data_table.ToJSonResponse(columns_order=("time", "value"), order_by="time", req_id=reqID)

class Publish(Resource):
    ifLeaf = True
    def __init__(self):
        Resource.__init__(self)
    def render_GET(self,request):
        print 'publish request ' , request.args
        if( request.args.has_key('data') ):
            rawstr=request.args["data"][0]
            data = json.loads(rawstr)
            print data
        return 'ok'

server = pymongo.Connection()
db  = server.daq
root = Resource()
root.putChild( "static", File("./static") )
root.putChild( "query", BeQuery(db.bees) )
root.putChild( "publish", Publish() )
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
