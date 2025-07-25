import csv
import mysql.connector
import os
# MySQL connection parameters
DB_CONFIG = {
    'user': os.environ.get('DBUSER', 'root'),
    'password': os.environ.get('DBPASS', 'Secret5555'),
    'host': os.environ.get('DBHOST', '127.0.0.1'),
    'database': os.environ.get('DBNAME', 'subscribers')
}

# CSV file path and target table details
CSV_FILE_PATH = 'subscribers.csv'
TABLE_NAME = 'subscriber'
# Ensure column names in the list match the order of columns in your CSV and the target table
COLUMN_NAMES = ['name', 'email', 'sign_up_date', 'interests'] 

try:
    # Establish MySQL connection
    cnx = mysql.connector.connect(**DB_CONFIG)
    cursor = cnx.cursor()

    # Construct the INSERT statement dynamically
    placeholders = ', '.join(['%s'] * len(COLUMN_NAMES))
    insert_sql = f"INSERT INTO {TABLE_NAME} ({', '.join(COLUMN_NAMES)}) VALUES ({placeholders})"

    # Open and read the CSV file
    with open(CSV_FILE_PATH, mode='r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row if your CSV has one

        # Iterate through each row in the CSV and insert into MySQL
        for row in csv_reader:
            print(row)
            cursor.execute(insert_sql, row)

    # Commit the changes to the database
    cnx.commit()
    print(f"Data from '{CSV_FILE_PATH}' successfully imported to '{TABLE_NAME}'.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'cnx' in locals() and cnx.is_connected():
        cnx.close()
