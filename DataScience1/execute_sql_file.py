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

def execute_sql_file(conn, file_path):
    try:
        with open(file_path, "r") as sql_file:
            sql_query = sql_file.read()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        conn.commit()
        print(f"SQL from {file_path} executed successfully.")
    except FileNotFoundError as fnf_err:
        print(f"File not found: {fnf_err}")
    except Error as err:
        print(f"Error while executing SQL: {err}")

def csv_to_data():
    conn = connect_db()
    if conn:
        execute_sql_file(conn, "remove_duplicates.sql")
        conn.close()

if __name__ == "__main__":
    csv_to_data()