from StringIO import StringIO
import matplotlib
import datetime
matplotlib.use('Agg') # So we can run this headless

import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib import rc
import pytz
#from matplotlib import gridspec 

#rc('text',usetex=True)
#rc('font',family='serif')

def plotter( data, fname=None ):

    btz = pytz.timezone('UTC')
    try: 
        xy = data['ohain.temp{id=0}']

        fig = plt.figure(figsize=(14,8))
 #   gs = gridspec.GridSpec(1, 2,width_ratios=[2,1])
    #p1 = fig.add_subplot(2,1,1)
        p1 = plt.subplot2grid((3,1),(0,0))
        p1.set_title('Time is UTC')
    #p2 = fig.add_subplot(2,1,2) 
        p2 = plt.subplot2grid((3,1),(1,0),rowspan=2)
        p1.plot_date(dates.epoch2num(xy[0]),xy[1],'r-',tz=btz,xdate=True,ydate=False,aa=False,lw=0.5)
        p1.set_ylim(-10,35)
        majloc = dates.AutoDateLocator()
        majform = dates.AutoDateFormatter(majloc)
        majform.scaled[1.]='%d %b %Y'
        majform.scaled[1./24.] = '%d %b %H:%M'
        majform.scaled[2.]='%D'
        print majform.scaled
        p1.set_ylabel(r'Temperature (C)')
   # p1.xaxis.set_major_locator(majloc)
   # p1.xaxis.set_major_formatter(majform)
        p1.set_xticklabels([],visible=False)
        p1.grid(True)
      #  p1 = fig.add_subplot(212) 

        xy1 = data['ohain.weight{id=1}']
        p2.plot_date(dates.epoch2num(xy1[0]),xy1[1],'g-',tz=btz,xdate=True,ydate=False,aa=True,lw=0.5)
        #xy2 = data['ohain.weight{id=2}']
        #p2.plot_date(dates.epoch2num(xy2[0]),xy2[1],'b-',tz=btz,xdate=True,ydate=False,aa=True,lw=0.5)
        xy3 = data['ohain.weight{id=0}']
        p2.plot_date(dates.epoch2num(xy3[0]),xy3[1],'m-',tz=btz,xdate=True,ydate=False,aa=True,lw=0.5)
        xy4 = data['ohain.weight{id=3}']
        p2.plot_date(dates.epoch2num(xy4[0]),xy4[1],'r-',tz=btz,xdate=True,ydate=False,aa=True,lw=0.5)
        p2.set_ylabel('Weight (kg)')
        p2.grid(True)
        #leg=p2.legend(['B3R4','B2R6','B4R5','B1R7'],'upper left', labelspacing=0.2)
        leg=p2.legend(['B3R4','B4R5','B1R7'],'upper left', labelspacing=0.2)
        for l in leg.get_texts():
            l.set_fontsize('small')
            p2.xaxis.set_major_locator(majloc)
            p2.xaxis.set_major_formatter(majform)
        for l in p2.get_xticklabels():
            l.set_rotation(30)
            l.set_size(9)
#    plt.subplots_adjust(hspace=0.0)
#   plt.tick_params(axis='x', colors='red')
#
#    plt.tick_params(axis='x', labelsize=8)
#    p2.set_xlabel('time')
#    fig.autofmt_xdate(0.1)

#    plt.set_ylabel('value')

#    plt.set_title('ADC values')

    
        if( not fname ):
            f = StringIO()
            fig.savefig(f, format="svg")
            buff = f.getvalue()
            f.close()
            fig.clf()
            plt.close()
            return buff
        else:
            fig.savefig(fname, format="svg")
            fig.clf()
            plt.close()
    except KeyError:
        print "Invalid Key"
