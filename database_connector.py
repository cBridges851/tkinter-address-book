import sqlite3

class DatabaseConnector:
    def __init__(self):
        self.connection = sqlite3.connect("address_book.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()