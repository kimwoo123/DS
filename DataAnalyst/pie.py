from psycopg2 import connect, Error, OperationalError
from matplotlib import pyplot


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
        raise

def execute_sql_file(conn, file_path):
    try:
        with open(file_path, "r") as sql_file:
            sql_query = sql_file.read()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        conn.commit()

        result = cursor.fetchall()
        cursor.close()

        return result

    except FileNotFoundError as fnf_err:
        print(f"File not found: {fnf_err}")
        raise
    except Error as err:
        print(f"Error while executing SQL: {err}")
        raise

def make_graph(data):
    data.sort(key=lambda x: -x[1])
    event_types, count = zip(*data)
    pyplot.pie(
        count,
        explode=[0.01, 0.01, 0.01, 0.01],
        labels=event_types,
        autopct='%1.1f%%',
        # ('view', 'cart', 'remove_from_cart', 'purchase')
        colors=['blue', 'orange', 'green', 'red'],
        )
    pyplot.title('my pie')
    pyplot.show()


def csv_to_data():
    conn = connect_db()
    data = execute_sql_file(conn, "pie.sql")
    make_graph(data)
    conn.close()

if __name__ == "__main__":
    csv_to_data()