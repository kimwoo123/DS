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

def datetime_to_month(dt_list):
    return tuple(dt.strftime("%B") for dt in dt_list)

def draw_plot(axs, months, counts):
    axs[0].plot(months, counts)

def draw_bar(axs, months, counts):
    axs[1].bar(months, counts)

def draw_fill_between(axs, months, counts):
    axs[2].fill_between(months, counts)

def make_graph(data):
    dt_list, counts = zip(*data)
    months = datetime_to_month(dt_list)
    
    fig, axs = pyplot.subplots(1, 3, figsize=(12, 8))
    draw_bar(axs, months, counts)
    draw_plot(axs, months, counts)
    draw_fill_between(axs, months, counts)

    fig.suptitle("hi")
    pyplot.show()

    # data.sort(key=lambda x: -x[1])
    # event_types, count = zip(*data)
    # pyplot.pie(
    #     count,
    #     explode=[0.01, 0.01, 0.01, 0.01],
    #     labels=event_types,
    #     autopct='%1.1f%%',
    #     # ('view', 'cart', 'remove_from_cart', 'purchase')
    #     colors=['blue', 'orange', 'green', 'red'],
    #     )
    # pyplot.title('my chart')
    # pyplot.show()


def csv_to_data():
    conn = connect_db()
    data = execute_sql_file(conn, "chart.sql")
    make_graph(data)
    conn.close()

if __name__ == "__main__":
    csv_to_data()