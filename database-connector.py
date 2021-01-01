import sqlite3

class DatabaseConnector:
    def __init__(self):
        self.connection = sqlite3.connect("address_book.db")