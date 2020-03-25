#!/bin/bash

#related directories and files
BASE=$HOME/app/curVis
LOG_DIR=$BASE/logs
OUT_LOG=$LOG_DIR/output.log
DATA_FILE=$BASE/data.zip

#make sure the BASE & LOG_DIR directory exists and if not, create it
mkdir -p $LOG_DIR

#delete data.zip file if exists
if [ -f $DATA_FILE ]
then
	rm -f $DATA_FILE
fi

#put timestamp into output.log
echo "==============================================" >> $OUT_LOG
echo `date`: >> $OUT_LOG
echo >> $OUT_LOG

#download the zip file from ECB webpage
curl -L "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip?ee318a8fef4b64837f6f7f900275b4c7" > $DATA_FILE 2>> $OUT_LOG
