import psycopg2
from psycopg2 import Error, OperationalError
from os import listdir
from profile import timefn

def connect_db():
    db_info = {
        "host": "localhost",
        "dbname": "piscineds",
        "user": "wooseoki",
        "password": "mysecretpassword",
    }
    try:
        conn = psycopg2.connect(**db_info)
        return conn
    except OperationalError as err:
        print("Error while connecting to the database:", err)
        return None

def migrate(conn):
    cursor = conn.cursor()

    # CREATE TABLE
    with open("csv_to_data.sql", "r") as sql_file:
        create_tables_query = sql_file.read()
    try:
        cursor.execute(create_tables_query)
        conn.commit()  # 테이블 생성 후 커밋
        print("Table created successfully.")
    except Error as err:
        conn.rollback()
        print("Error while creating table:", err)

    # INSERT DATA
    directory_path = "/Users/zingvely/Downloads/subject/customer/"
    for file in listdir(directory_path):
        if file.endswith(".csv"):
            table_name = file[:-4]
            try:
                with open(directory_path + file, 'r') as f:
                    print(table_name)
                    cursor.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)
                conn.commit()  # 데이터 삽입 후 커밋
                print("Data inserted successfully.")
            except FileNotFoundError as fnf_err:
                print(f"File not found: {fnf_err}")
            except Error as err:
                conn.rollback()
                print("Error while inserting data:", err)

    cursor.close()

@timefn
def csv_to_data():
    conn = connect_db()
    if conn:
        migrate(conn)
        conn.close()

if __name__ == "__main__":
    csv_to_data()