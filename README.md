Currency Visualization - curVis

Runs on every Unix/Linux OS based system
This program downloads data of currency rates of EUR upon other world currencies from ECB official webpage. The data is being collected from the beginning of 1999 up to this day. After that the data is initially pushed into Postgresql DB.
Upon this DB, there is Java application which will then view this data.

Prerequisities:
1. python3 required
2. psycopg2 python library required   #library that allows interaction of python with Postgresql DB

Example on Ubuntu:
sudo pip3 install psycopg2


3. install Postgresql

Example on Ubuntu:
sudo apt install postgresql postgresql-contrib
	
4. login to postgres DB and set "postgres" password for postgres user:

Example:
osboxes@osboxes: sudo -u postgres psql
psql (11.7 (Ubuntu 11.7-0ubuntu0.19.10.1))
Type "help" for help.

postgres=# 
postgres=# 
postgres=# ALTER USER postgres PASSWORD 'postgres';
ALTER ROLE
postgres=# 

5. once this repositoru is cloned, run these 2 scripts:
$HOME/curVis/dataCol/bin/dataCollector.sh  #this will initially download the source file
$HOME/curVis/dataMan/bin/dataManager.py	   #this will initially load the data into DB

6. add these scripts to run within crontab once a day to update the DB each day with new values
$HOME/curVis/dataCol/bin/dataCollector.sh   #needs to run first
$HOME/curVis/dataMan/bin/dataManager.py     #will add new values from CSV file if any

