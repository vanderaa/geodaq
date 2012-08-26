#!/bin/bash
location=/home/vanderaa/SW/opentsdb
tsdtmp=${TMPDIR-'/tmp'}/tsd 
mkdir -p "$tsdtmp" 
"$location"/build/tsdb tsd --port=4242 --staticroot="$location"/build/staticroot --cachedir="$tsdtmp" 
