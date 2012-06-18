#!/bin/sh
HH=/home/vanderaa/SW/TINI/tini1.02b
java -classpath $HH/bin/tini.jar BuildDependency -f build -o bin/test.tini -d $HH/bin/tini.db -p $HH/bin/owapi_dependencies_TINI_001.jar -add OneWireContainer10
