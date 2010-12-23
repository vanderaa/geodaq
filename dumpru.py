#!/usr/bin/env python
import MySQLdb 
import sys



db=None 
cursor=None


def listdet():
	global cursor	
	cursor.execute('Select DetName from asso');
	numrows=int(cursor.rowcount)
	result=cursor.fetchmany(numrows)
	for det in result:
		print det[0]	

def average((basetime,time_values)):
	average=0
	count=0
	for (time,value) in time_values:
		count=count+1
		average=average+value	
	average=average/count
	return (basetime,average)

def extrema((basetime,time_values),sign=1):
	ext=None
	for (time,value) in time_values:
		if(ext==None):
			ext=value
		elif(sign==1 and sign>ext):
			ext=value
		elif(sign==-1 and value<ext):
			ext=value
	return (basetime,ext)

def maxval((basetime,time_values)):
	return extrema([basetime,time_values],1)

def minval((basetime,time_values)):
	return extrema([basetime,time_values],-1)

def accumulate(time,value,interval,tvals):
	if(tvals[0]==None):
		tvals[0]=time
		tvals[1].append((time,value))	
	elif(time-time%interval != tvals[0]-tvals[0]%interval):
		ret_vals=list(tvals[1])
		ret_time=tvals[0]
		tvals[0]=time
		del(tvals[1][:])
		tvals[1].append((time,value))	
		return (ret_time-ret_time%interval,ret_vals)	
	else:
		tvals[1].append((time,value))	


		
def query((det,start_date,stop_date)):
	global cursor	
	cursor.execute("""select dta.utime,dta.calvalue from dta,asso  where dta.date > (%s) 
			  and dta.serialID=asso.serialID 
                          and dta.channelID=asso.channelID 
			  and dta.date < (%s)
			  and asso.DetName=(%s)""",(start_date,stop_date,det))
	numrows=int(cursor.rowcount)
	for x in range(numrows):
		x=list([])
		result=cursor.fetchone()
		time=int(result[0])
		try:
			value=float(result[1])
		except TypeError:
			None
		print time,',', det,',', value

def usage():
	print """usage: anaru.py -l [passwd]--> list detectors
                 -q [passwd] [detector] [start date] [end date] --> dump data"""


def main(args):
	global db
	global cursor	
	if(len(args)>1):		
		db=MySQLdb.connect(host="daq.local", user="rudaq", passwd=args[2],db="rudata")		
		cursor=db.cursor()		
		if(args[1]=='-l'):
			listdet()
		if(args[1]=='-q'):
			query((args[3:]))
		db.close()
	else: 
		usage()
		
	


main(sys.argv)	

