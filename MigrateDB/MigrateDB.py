import logging
import pymysql
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    # Connect to MySQL
    logging.info("Connecting to MySQL...")
    mysql_conn = pymysql.connect(
        host="localhost",
        user="root",
        password="shakira",
        database="source_db"
    )
    logging.info("MySQL connection established.")

    # Connect to PostgreSQL
    logging.info("Connecting to PostgreSQL...")
    postgres_conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="shakisiru",
        database="target_db"
    )
    logging.info("PostgreSQL connection established.")

    # Step 3: Create SQLAlchemy engines
    mysql_engine = create_engine("mysql+pymysql://root:shakira@localhost/source_db")
    postgres_engine = create_engine("postgresql+psycopg2://postgres:shakisiru@localhost/target_db")


# Read data from MySQL
    logging.info("Reading data from MySQL...")
    query = "SELECT * FROM employees"
    df = pd.read_sql(query, mysql_engine)

    # Write data to PostgreSQL
    logging.info("Writing data to PostgreSQL...")
    df.to_sql("employees", postgres_engine, if_exists="append", index=False)
    logging.info("Data written to PostgreSQL.")

    # Verify Data Integrity
    postgres_cursor = postgres_conn.cursor()
    postgres_cursor.execute("SELECT COUNT(*) FROM employees")
    postgres_count = postgres_cursor.fetchone()[0]

    mysql_cursor = mysql_conn.cursor()
    mysql_cursor.execute("SELECT COUNT(*) FROM employees")
    mysql_count = mysql_cursor.fetchone()[0]

    if mysql_count == postgres_count:
        logging.info("Data migrated successfully with integrity!")
    else:
        logging.error("Data mismatch detected!")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Close connections
    if 'mysql_conn' in locals():
        mysql_conn.close()
    if 'postgres_conn' in locals():
        postgres_conn.close()
    if 'mysql_cursor' in locals():
        mysql_cursor.close()
    if 'postgres_cursor' in locals():
        postgres_cursor.close()