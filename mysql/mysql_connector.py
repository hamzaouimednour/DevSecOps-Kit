import mysql.connector

def check_mysql_connection():
    # Replace these values with your MySQL database connection details
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'dev',
        'port': '3306'
    }

    try:
        # Attempt to establish a connection
        connection = mysql.connector.connect(**db_config)

        # Check if the connection is successful
        if connection.is_connected():
            print("Connected to the MySQL database!")
    except mysql.connector.Error as e:
        print(f"Connection failed. Error: {e}")
    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    check_mysql_connection()
