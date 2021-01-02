from database_connector import DatabaseConnector
from database_creator import DatabaseCreator

class DatabaseFunctionManager:
    def __init__(self):
        self.connection = DatabaseConnector().connection
        self.cursor = DatabaseConnector().cursor

    def create(self):
        DatabaseCreator().create_database(self.connection, self.cursor)
