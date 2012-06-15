from StringIO import StringIO
import matplotlib
import datetime

matplotlib.use('Agg') # So we can run this headless

from matplotlib import pyplot
from matplotlib import dates

def plotter( data ):
    fig = pyplot.figure()

    plt = fig.add_subplot(211)

    xy = data['ohain.temp{id=0}']
    plt.plot_date(dates.epoch2num(xy[0]),xy[1],'r.-',tz=None,xdate=True,ydate=False,aa=True,lw=1)
    plt.set_ylim(0,25)
    majloc = dates.AutoDateLocator()
    majform = dates.AutoDateFormatter(majloc)
    plt.xaxis.set_major_locator(majloc)
    plt.xaxis.set_major_formatter(majform)
    plt.grid(True)
    plt = fig.add_subplot(212)
    xy = data['ohain.adc{id=14}']
    plt.plot_date(dates.epoch2num(xy[0]),xy[1],'g.-',tz=None,xdate=True,ydate=False,aa=True,lw=1)
    fig.autofmt_xdate()
#    plt.set_xlabel('time')

#    plt.set_ylabel('value')

#    plt.set_title('ADC values')

    

    f = StringIO()

    fig.savefig(f, format="svg",transparent=True)

    buff = f.getvalue()

    f.close()

    return buff