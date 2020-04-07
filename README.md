Currency Visualization - curVis

Runs on every Unix/Linux OS based system
This program downloads data of currency rates of EUR upon other world currencies from ECB official webpage. The data is being collected from the beginning of 1999 up to this day. After that the data is initially pushed into Postgresql DB.
Upon this DB, there is Java application which can visualize this data based on user's desire.

Prerequisities:
1. python3 required
2. psycopg2 python library required   #library that allows interaction of python with Postgresql DB

Example on Ubuntu:
sudo pip3 install psycopg2


3. install Postgresql DB

Example on Ubuntu:
sudo apt install postgresql postgresql-contrib
	
4. login to postgres DB and set "postgres" password for postgres user:

Example:
osboxes@osboxes: sudo -u postgres psql
psql (11.7 (Ubuntu 11.7-0ubuntu0.19.10.1))
Type "help" for help.

postgres=# ALTER USER postgres PASSWORD 'postgres';

5. java JDBC driver   "allows to interact Java (curVis) application with Postgresql DB"

6. once this repository is cloned to your HOME directory, run these 2 scripts:
$HOME/curVis/dataCol/bin/dataCollector.sh  #this will initially download the source file
$HOME/curVis/dataMan/bin/dataManager.py	   #this will initially load the data into DB

7. add these 2 scripts to run within crontab once a day to update the DB each day with new values
$HOME/curVis/dataCol/bin/dataCollector.sh   #needs to run first
$HOME/curVis/dataMan/bin/dataManager.py     #will add new values from CSV file if any

8. the curVis application itself can be run with command:
cd $HOME/curVis/dataVis && javac bin/CurVis.java && java bin.CurVis
