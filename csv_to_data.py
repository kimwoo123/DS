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
        return conn
    except OperationalError as err:
        print("Error while connecting to the database:", err)
        return None

def migrate(conn):
    cursor = conn.cursor()

    # CREATE TABLE
    create_table_query = """
    CREATE TABLE IF NOT EXISTS data_2022_oct (
        event_time TIMESTAMP,
        event_type VARCHAR(50),
        product_id INT,
        price FLOAT,
        user_id INT,
        user_session VARCHAR(50)
    );
    """
    try:
        cursor.execute(create_table_query)
        conn.commit()  # 테이블 생성 후 커밋
        print("Table created successfully.")
    except Error as err:
        print("Error while creating table:", err)

    # INSERT DATA
    csv_file_path = "/Users/zingvely/Downloads/subject/customer/data_2022_dec.csv"
    try:
        with open(csv_file_path, 'r') as f:
            cursor.copy_expert("COPY data_2022_oct FROM STDIN WITH CSV HEADER", f)
        conn.commit()  # 데이터 삽입 후 커밋
        print("Data inserted successfully.")
    except FileNotFoundError as fnf_err:
        print(f"File not found: {fnf_err}")
    except Error as err:
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