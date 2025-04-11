# db/mysql.py

import mysql.connector

class MySQL:
    def __init__(self, host, username, password, database, port=3306):
        self.config = {
            'host': host,
            'user': username,
            'password': password,
            'database': database,
            'port': port
        }
        self.connection = None

    def connect(self):
        if not self.connection or not self.connection.is_connected():
            self.connection = mysql.connector.connect(**self.config)

    def execute_query(self, query):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def execute_query_dict(self, query):
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
