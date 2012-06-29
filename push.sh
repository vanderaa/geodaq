#!/bin/bash
whome=$HOME/geodaq/web
wget -O $whome/img/plot_1w.svg http://lego.xe.be:8080/?start=1w-ago
wget -O $whome/img/plot_1m.svg http://lego.xe.be:8080/?start=30d-ago
wget -O $whome/img/plot_1d.svg http://lego.xe.be:8080/?start=1d-ago
wget -O $whome/img/plot_1y.svg http://lego.xe.be:8080/?start=1y-ago
s3cmd  put -P --recursive $whome/* s3://ruches.xe.be/
