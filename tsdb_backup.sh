#!/bin/sh
HBASE_HOME=$HOME/SW/hbase-0.92.1/
BDIR=/tmp/tsdb_bkp
cdir=`pwd`
cd $HBASE_HOME
if [ -d $BDIR ]
then
    echo 'Removing content'
    rm -r $BDIR/*
    echo 'backing up tsdb data'
    ./bin/hbase org.apache.hadoop.hbase.mapreduce.Export tsdb $BDIR/tsdb
    echo 'backing up tsdb uid'
    ./bin/hbase org.apache.hadoop.hbase.mapreduce.Export tsdb-uid $BDIR/tsdb-uid
    s3cmd  put -P --recursive $BDIR s3://ruches.xe.be/
else
    echo directory $BDIR does not exist
fi
