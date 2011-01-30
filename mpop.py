#!/usr/bin/env python 

import pymongo 
import sys

def add_measurement( collection, measurement ):
	docs=[]
	for m in measurement:
		docs.append({'timestamp': m[0] ,
               		     'detector' : m[1] ,
               		     'data'     : m[2] })
	sys.stdout.write("=")
	sys.stdout.flush()	
	collection.insert(docs)	


def main(argv):
	server = pymongo.Connection()
	db  = server.daq
        collection = db.bees 	
	f=open(argv[1])
	m=[]
	for line in f:
		measurement=line.split(',')
		m.append([int(measurement[0]),
			  measurement[1].strip(),
		          float(measurement[2])])
		if(len(m) == 1000):
			add_measurement( collection, m)
			m=[]		
	if( len(m) != 0 ):
		add_measurement( collection, m)
	f.close()
	print 'All done'

main(sys.argv)
