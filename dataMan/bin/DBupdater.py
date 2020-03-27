import os
import csv
import psycopg2

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


class db_connect():
    def __init__(self):
        #create conenction to DB
        global conn
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")
        global cur
        cur = conn.cursor()

        #removes the last column = empty column in CSV and reverse the lines in CSV file
        with open(source_file,"r") as source:
            with open(mid_file, "w") as mid:
                src = csv.reader(source, delimiter=",")
                writer = csv.writer(mid, delimiter=",")
                for row in src:
                    writer.writerow(row[:-1])

        with open(mid_file, "r") as mid:
            with open(output_file, "w") as out:
                src = csv.reader(mid, delimiter=",")
                writer = csv.writer(out, delimiter=",")      
                writer.writerow(next(src))  # write header
                writer.writerows(reversed(list(src)))
               

        global file
        file = open(output_file, "r")
        
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
        cur.execute(new_table)
        conn.commit()

    #load the data in CSV file into $USER table
    def load_csv_file(self):
        next(file)
        cur.copy_from(file, user, sep=",", columns=['Date', 'USD', 'JPY', 'BGN', 'CYP', 'CZK', 'DKK', 'EEK', 'GBP', 'HUF', 'LTL', 'LVL', 'MTL', 'PLN', 'ROL', 'RON', 'SEK', 'SIT', 'SKK', 'CHF', 'ISK', 'NOK', 'HRK', 'RUB', 'TRL', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR'])
        conn.commit()
        

       
if __name__ == "__main__":
    try:
        db_connect().create_table()
        db_connect().load_csv_file()
        print(f"Created table \"{user}\" and loaded data into it")
    
    except psycopg2.errors.DuplicateTable:
        db_connect().load_csv_file()
        print(f"Table \"{user}\" already exists")