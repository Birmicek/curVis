import os
import csv
import psycopg2
import datetime

#defining the .csv files and user
home_dir = os.popen("echo $HOME").read().strip()
source_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data.csv")
mid_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data_mid.csv")
output_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data_updated.csv")
user = os.popen("echo $USER").read().strip()

#defing class that saves the data and prepare them for DB insertion
class csv_constructor():
    def __init__(self):
        #file = open(source_file, "r")
        #global csv_file
        #csv_file = csv.reader(file, delimiter=",")
        with open(source_file,"r") as source:
            with open(output_file,"w") as out:
                writer=csv.writer(out)
                for row in csv.reader(source, delimiter=","):
                    writer.writerow(row[:-1])
        
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

        

    def __del__(self):
        self.conn.close()
        
    #check if table $USER exists and if not, create it
    def create_table(self):
        new_table = f"""CREATE TABLE {user} (
                    id SERIAL PRIMARY KEY,
                    Date text,
                    USD	text,
                    JPY	text,
                    BGN	text,
                    CYP	text,
                    CZK	text,
                    DKK	text,
                    EEK	text,
                    GBP	text,
                    HUF	text,
                    LTL	text,
                    LVL	text,
                    MTL	text,
                    PLN	text,
                    ROL	text,
                    RON	text,
                    SEK	text,
                    SIT	text,
                    SKK	text,
                    CHF	text,
                    ISK	text,
                    NOK	text,
                    HRK	text,
                    RUB	text,
                    TRL	text,
                    TRY	text,
                    AUD	text,
                    BRL	text,
                    CAD	text,
                    CNY	text,
                    HKD	text,
                    IDR	text,
                    ILS	text,
                    INR	text,
                    KRW	text,
                    MXN	text,
                    MYR	text,
                    NZD	text,
                    PHP	text,
                    SGD	text,
                    THB	text,
                    ZAR	text);"""
        self.cur.execute(new_table)

    #load the data in CSV file into $USER table
    def load_csv_file(self):
        with open(output_file, "r") as f:
            src = csv.reader(f, delimiter=",")
            col_names = list(src)[0]
        with open(output_file, "r") as f:
            next(f)   #skip the header
            self.cur.copy_from(f, user, sep=",", columns=col_names)

    def add_new_values(self):
        #check the last date in DB table
        date_query = f"SELECT date FROM osboxes ORDER BY id DESC LIMIT 1;"
        self.cur.execute(date_query)
        last_date_in_table = self.cur.fetchone()[0]

        with open(output_file, "r") as f:
            last_date_in_csv = list(csv.reader(f))[-1][0]

        with open(output_file, "r") as f:
            last_row_in_csv = list(csv.reader(f))[-1]
            last_row_in_csv = "', '".join(last_row_in_csv)

        if last_date_in_table == last_date_in_csv:
            print("The DB table is already updated with latest values of currency rates")
        else:
            print("Inserting new values into DB")
            insert_query = f"INSERT INTO {user} VALUES (default, '{last_row_in_csv}');"
            self.cur.execute(insert_query)
            print("New values inserted into DB table")

    
if __name__ == "__main__":
    try:
        db_connect().create_table()
        db_connect().load_csv_file()
        print(f"Created table \"{user}\" and loaded data into it")
    
    except psycopg2.errors.DuplicateTable:
        print(f"Table \"{user}\" already exists")
        db_connect().add_new_values()