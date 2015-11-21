#!/bin/bash
LOCK=/var/tmp/push.lock
if [ -f $LOCK ]; then
    echo Job is already running\!
    exit 6
fi

touch $LOCK
# do some work
whome=$HOME/geodaq/web
$HOME/geodaq/genplot.py 1w-ago $whome/img/plot_1w.svg
$HOME/geodaq/genplot.py 30d-ago $whome/img/plot_1m.svg
$HOME/geodaq/genplot.py 1d-ago $whome/img/plot_1d.svg
$HOME/geodaq/genplot.py 1y-ago $whome/img/plot_1y.svg
#wget -O $whome/img/plot_1w.svg http://127.0.0.1:8080/?start=1w-ago
#wget -O $whome/img/plot_1m.svg http://127.0.0.1:8080/?start=30d-ago
#wget -O $whome/img/plot_1d.svg http://127.0.0.1:8080/?start=1d-ago
#wget -O $whome/img/plot_1y.svg http://127.0.0.1:8080/?start=1y-ago
s3cmd  put -P --recursive $whome/* s3://ruches.xe.be/
rm $LOCK
