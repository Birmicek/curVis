import psycopg2
import os
import datetime

#defining the .csv source file

home_dir = os.popen("echo $HOME").read().strip()
source_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data.csv")

#print(home_dir)
print(source_file)