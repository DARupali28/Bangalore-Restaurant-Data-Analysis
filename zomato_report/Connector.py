import mysql.connector
from getpass import getpass

class my_sql_connector:
    def __init__(self):

        mysql_password = getpass("Enter MySQL password: ")

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=mysql_password,
            database="bangalore_restaurants"
        )

    def get_connection(self):
        return self.connection

    def close(self):
        if self.connection.is_connected():
            self.connection.close()