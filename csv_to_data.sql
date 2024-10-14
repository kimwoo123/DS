CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

CREATE TABLE IF NOT EXISTS data_2022_nov (
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

CREATE TABLE IF NOT EXISTS data_2022_dec (
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    product_id INT,
    price FLOAT,
    user_id INT,
    user_session VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS data_2023_jan (
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    product_id INT,
    price FLOAT,
    user_id INT,
    user_session VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS data_2023_feb (
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    product_id INT,
    price FLOAT,
    user_id INT,
    user_session VARCHAR(50)
);