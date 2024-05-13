import mysql.connector

class DB:
    def __init__(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="shop"
        )
        self.db = db