import os
import csv
import psycopg2

#defining the .csv source file
home_dir = os.popen("echo $HOME").read().strip()
source_file = os.path.join(home_dir, "curVis/dataCol/data/currency_data.csv")
user = os.popen("echo $USER").read().strip()

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
        global conn
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
        global cur
        cur = conn.cursor()

    def create_table(self):
        new_table = f"""CREATE TABLE {user} (
                    id integer PRIMARY KEY,
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
        cur.execute(new_table)
        conn.commit()
        
        
if __name__ == "__main__":
    try:
        db_connect().create_table()
        print(f"Created table \"{user}\"")
    except psycopg2.errors.DuplicateTable:
        print(f"Table \"{user}\" already exists")
        pass

