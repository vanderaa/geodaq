from StringIO import StringIO
import matplotlib
import datetime
matplotlib.use('Agg') # So we can run this headless

import matplotlib.pyplot as plt
from matplotlib import dates
from matplotlib import rc
#from matplotlib import gridspec 

#rc('text',usetex=True)
#rc('font',family='serif')

def plotter( data ):

    xy = data['ohain.temp{id=0}']

    fig = plt.figure()
 #   gs = gridspec.GridSpec(1, 2,width_ratios=[2,1])
    #p1 = fig.add_subplot(2,1,1)
    p1 = plt.subplot2grid((3,1),(0,0))
    #p2 = fig.add_subplot(2,1,2) 
    p2 = plt.subplot2grid((3,1),(1,0),rowspan=2)
    p1.plot_date(dates.epoch2num(xy[0]),xy[1],'r-',tz=None,xdate=True,ydate=False,aa=False,lw=0.5)
    p1.set_ylim(0,35)
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
    xy = data['ohain.weight{id=1}']
    p2.plot_date(dates.epoch2num(xy[0]),xy[1],'g-',tz=None,xdate=True,ydate=False,aa=True,lw=0.5)
    xy = data['ohain.weight{id=2}']
    p2.plot_date(dates.epoch2num(xy[0]),xy[1],'b-',tz=None,xdate=True,ydate=False,aa=True,lw=0.5)
    xy = data['ohain.weight{id=0}']
    p2.plot_date(dates.epoch2num(xy[0]),xy[1],'m-',tz=None,xdate=True,ydate=False,aa=True,lw=0.5)
    p2.set_ylabel('Weight (kg)')
    p2.grid(True)
    leg=p2.legend(['1','2','3'],'upper left', labelspacing=0.2)
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

    

    f = StringIO()

    fig.savefig(f, format="png")

    buff = f.getvalue()

    f.close()

    return buff
