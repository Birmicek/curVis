import os
import csv
import psycopg2

#defining the .csv source file
home_dir = os.popen("echo $HOME").read().strip()
source_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data.csv")

#defing class that saves the data and prepare them for DB insertion
class csv_constructor():
    def __init__(self):
        file = open(source_file, "r")
        global csv_file
        csv_file = csv.reader(file, delimiter=",")
        
    def get_currency(self):
        currency = []
        column_name = next(csv_file, None)
        column_name = column_name[1:]
        for i in column_name:
            if i == "":
                continue
            else:
                i = "EUR/" + i
                currency.append(i)
        return currency

    def get_date(self):
        dates = []
        line_count = 0
        for row in csv_file:
            if line_count == 0:
                line_count += 1
                continue
            else:
                dates.append(row[0])
        return dates

    def get_values(self):
        final = {}
        item = {}
        column_count = 1
        dates = csv_constructor().get_date()
        currency = csv_constructor().get_currency()


class db_connect():
    def __init__(self):
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")


# csv_constructor().get_currency()
# print()
# csv_constructor().get_date()
#csv_constructor().get_values()


