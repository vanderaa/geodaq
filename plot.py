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
    plt.plot_date(dates.epoch2num(xy[0]),xy[1],'r-',tz=None,xdate=True,ydate=False,aa=False,lw=0.5)
    plt.set_ylim(0,25)
    majloc = dates.AutoDateLocator()
    majform = dates.AutoDateFormatter(majloc)
    plt.xaxis.set_major_locator(majloc)
    plt.xaxis.set_major_formatter(majform)
    plt.grid(True)
    plt = fig.add_subplot(212)
    xy = data['ohain.weight{id=1}']
    plt.plot_date(dates.epoch2num(xy[0]),xy[1],'g-',tz=None,xdate=True,ydate=False,aa=False,lw=0.5)
    plt.grid(True)
    fig.autofmt_xdate()
    plt.xaxis.label.set_color('red')
    plt.tick_params(axis='x', colors='red')

#    plt.tick_params(axis='x', labelsize=8)
#    plt.set_xlabel('time')

#    plt.set_ylabel('value')

#    plt.set_title('ADC values')

    

    f = StringIO()

    fig.savefig(f, dpi=150, format="png")

    buff = f.getvalue()

    f.close()

    return buff
