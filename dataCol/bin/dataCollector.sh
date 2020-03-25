#!/bin/bash

#related directories and files
BASE=$HOME/curVis/dataCol
LOG_DIR=$BASE/logs
DATA_DIR=$BASE/data
OUT_LOG=$LOG_DIR/dataCol_output.log
DATA_FILE=$DATA_DIR/data.zip
UNZIPPED_DATA=$DATA_DIR/currency_data.csv
UNZIP=`which unzip`
CURL=`which curl`

#make sure the BASE, LOG_DIR & DATA_DIR directories exist and if not, create them
mkdir -p $LOG_DIR $DATA_DIR

#delete data.zip and currency_data.csv files if exist
if [ -f $DATA_FILE ] || [ -f $UNZIPPED_DATA ]
then
	rm -f $DATA_FILE $UNZIPPED_DATA
fi

#put timestamp into output.log
echo `date`: >> $OUT_LOG
echo >> $OUT_LOG

#download the zip file from ECB webpage
$CURL -L "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip?ee318a8fef4b64837f6f7f900275b4c7" > $DATA_FILE 2>> $OUT_LOG

#visual distinguisher in output.log
echo "==============================================" >> $OUT_LOG

#Unzip data.zip and rename the file
$UNZIP $DATA_FILE -d $DATA_DIR > /dev/null 2>&1 && mv $DATA_DIR/`echo $(unzip -lqq $DATA_FILE | awk '{print $NF}')` $UNZIPPED_DATA
