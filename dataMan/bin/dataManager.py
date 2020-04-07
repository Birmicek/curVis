#!/usr/bin/env python3

import os
import csv
import psycopg2
import datetime

#defining the .csv files and user
home_dir = os.popen("echo $HOME").read().strip()
source_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data.csv")
mid_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data_mid.csv")
output_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data_updated.csv")
final_output = os.path.join(home_dir, "curVis/dataCol/data/currency_data_final.csv")
user = os.popen("echo $USER").read().strip()

class db_connect:
    def __init__(self):
        #create connection to DB
        self.conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

        #removes the last column = empty column in CSV 
        with open(source_file,"r") as source:
            with open(mid_file, "w") as mid:
                src = csv.reader(source, delimiter=",")
                writer = csv.writer(mid, delimiter=",")
                for row in src:
                    writer.writerow(row[:-1])
        #reverse the lines in CSV file
        with open(mid_file, "r") as mid:
            with open(output_file, "w") as out:
                src = csv.reader(mid, delimiter=",")
                writer = csv.writer(out, delimiter=",")      
                writer.writerow(next(src))  # write header
                writer.writerows(reversed(list(src)))

        with open(output_file, "r") as out:
            with open(final_output, "w") as final:
                src = csv.reader(out, delimiter=",")
                writer = csv.writer(final, delimiter=",")
                writer.writerow(next(src))

        with open(output_file, "r") as out:
            with open(final_output, "a") as final:      
                src = list(csv.reader(out, delimiter=","))[1:]
                writer = csv.writer(final, delimiter=",")
                for i in src:
                    i[0] = datetime.datetime.strptime(i[0], '%Y-%m-%d').date()
                    for y in i[1:]:
                        if y == 'N/A':
                            pass
                        else:
                            i[i.index(y)] = float(y)
                    writer.writerow(i)

    def __del__(self):
        self.conn.close()
        
    #checks if table $USER exists and if not, create it
    def create_table(self):
        new_table = f"""CREATE TABLE {user} (
                    id SERIAL PRIMARY KEY,
                    Date date,
                    USD	numeric,
                    JPY	numeric,
                    BGN	numeric,
                    CYP	numeric,
                    CZK	numeric,
                    DKK	numeric,
                    EEK	numeric,
                    GBP	numeric,
                    HUF	numeric,
                    LTL	numeric,
                    LVL	numeric,
                    MTL	numeric,
                    PLN	numeric,
                    ROL	numeric,
                    RON	numeric,
                    SEK	numeric,
                    SIT	numeric,
                    SKK	numeric,
                    CHF	numeric,
                    ISK	numeric,
                    NOK	numeric,
                    HRK	numeric,
                    RUB	numeric,
                    TRL	numeric,
                    TRY	numeric,
                    AUD	numeric,
                    BRL	numeric,
                    CAD	numeric,
                    CNY	numeric,
                    HKD	numeric,
                    IDR	numeric,
                    ILS	numeric,
                    INR	numeric,
                    KRW	numeric,
                    MXN	numeric,
                    MYR	numeric,
                    NZD	numeric,
                    PHP	numeric,
                    SGD	numeric,
                    THB	numeric,
                    ZAR	numeric);"""
        self.cur.execute(new_table)
        self.load_csv_file()
        print(f"Created table \"{user}\" and loaded data into it")

    #load the data in CSV file into $USER table
    def load_csv_file(self):
        with open(final_output, "r") as f:
            src = csv.reader(f, delimiter=",")
            col_names = list(src)[0]
        with open(final_output, "r") as f:
            next(f)   #skip the header
            self.cur.copy_from(f, user, sep=",", columns=col_names, null='N/A')

    def add_new_values(self):
        #check the last date in DB table
        date_query = f"SELECT date FROM osboxes ORDER BY id DESC LIMIT 1;"
        self.cur.execute(date_query)
        last_date_in_table = self.cur.fetchone()[0]

        with open(final_output, "r") as f:
            last_date_in_csv = datetime.datetime.strptime(list(csv.reader(f))[-1][0], '%Y-%m-%d').date()            

        if last_date_in_table == last_date_in_csv:
            print("The DB table is already updated with latest values of currency rates")
        else:
            print("Inserting new values into DB")
            last_line = os.path.join(home_dir, "curVis/dataCol/data/last_line.csv")
            with open(final_output, "r") as f:
                with open(last_line, "w") as line:
                    last_row_in_csv = list(csv.reader(f, delimiter=","))[-1]
                    writer = csv.writer(line, delimiter=",")
                    writer.writerow(last_row_in_csv)
            
            with open(final_output, "r") as f:
                with open(last_line, "r") as line:
                    src = csv.reader(f, delimiter=",")
                    col_names = list(src)[0]
                    self.cur.copy_from(line, user, sep=",", columns=col_names, null='N/A')

            print("New values inserted into DB table")


if __name__ == "__main__":
    try:
        db_connect().create_table()
    
    except psycopg2.errors.DuplicateTable:
        print(f"Table \"{user}\" already exists")
        db_connect().add_new_values()
