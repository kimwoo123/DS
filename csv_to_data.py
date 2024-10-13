import psycopg2
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
    except Error as err:
        print("Error while connecting db:", err)

    return conn

def migrate(conn):
    cursor = conn.cursor()

    # CREATE TABLE
    create_table_query = """
    CREATE TABLE IF NOT EXISTS events (
        event_time TIMESTAMP,
        event_type VARCHAR(50),
        product_id INT,
        price FLOAT,
        user_id INT,
        user_session VARCHAR(50)
    );
    """
    cursor.execute(create_table_query)

    # INSERT DATA
    csv_file_path = "/Users/zingvely/Downloads/subject/customer/data_2022_dec.csv"
    with open(csv_file_path, 'r') as f:
        cursor.copy_expert("COPY events FROM STDIN WITH CSV HEADER", f)

    # CLEAN
    conn.commit()
    cursor.close()

@timefn
def csv_to_data():
    conn = connect_db()
    migrate(conn)

if __name__ == "__main__":
    csv_to_data()