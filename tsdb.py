import urllib 


class TSDb:
    def __init__(self, host,port):
        self.host = host
        self.port = port
    def query(self, start, stop, metrics, aggr, filt=None):
        # Lets construct the query strucutre
        qry = [('ascii',''),('start',start)]
        if( stop ):
            qry.append(('end',stop))
        for m in metrics:
            if( filt ):
                qry.append( ('m',aggr+':'+filt+':'+m) )
            else:
                qry.append( ('m',aggr+':'+m) )
        #print qry
        url = urllib.urlencode(qry)
        # Now lets query the guy
        f = urllib.urlopen('http://'+self.host+':'+str(self.port)+'/q?%s' % url)
        # Check the status code 
#        print f.geturl()
        if( f.getcode() == 200 ):
            return self.parse_result(f)
        else:
            f.close()
            return None
        f.close()

    def parse_result(self, f):
        res = {}
        try:
            for line in f:
                atoms=line.split()
                ln = len(atoms)
                if( ln >= 3 ):
                    tstamp = int(atoms[1])
                    value  = float(atoms[2])
                    if( ln == 3 ):
                        key = atoms[0]
                    if( ln == 4 ):
                        key = atoms[0]+'{'+atoms[3]+'}'
                    try:
                        res[key][0].append(tstamp)
                        res[key][1].append(value)
                    except KeyError:
                        res[key]=([],[])
                        res[key][0].append(tstamp)
                        res[key][1].append(value)
        finally:
            f.close()
        return res
