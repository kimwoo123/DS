from psycopg2 import connect, Error, OperationalError


def connect_db():
    db_info = {
        "host": "localhost",
        "dbname": "piscineds",
        "user": "wooseoki",
        "password": "mysecretpassword",
    }
    try:
        conn = connect(**db_info)
        return conn
    except OperationalError as err:
        print("Error while connecting to the database:", err)
        return None

def join_all_tables(conn):
    try:
        with open("join_tables.sql", "r") as sql_file:
            sql_query = sql_file.read()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        conn.commit()
        print("Data joined successfully.")
    except FileNotFoundError as fnf_err:
        print(f"File not found: {fnf_err}")
    except Error as err:
        print("Error while inserting data:", err)

def csv_to_data():
    conn = connect_db()
    if conn:
        join_all_tables(conn)
        conn.close()

if __name__ == "__main__":
    csv_to_data()