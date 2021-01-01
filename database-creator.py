import sqlite3

class DatabaseCreator:
    def create_database(self):
        try:
            # Create/Connect the database
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE addresses(
                    forename text NOT NULL,
                    surname text NOT NULL,
                    address_line_1 text NOT NULL,
                    address_line_2 text NOT NULL,
                    city text NOT NULL,
                    county text NOT NULL,
                    country text NOT NULL,
                    postcode text NOT NULL,
                    phone_number text NOT NULL,
                    email text NOT NULL
                );
            """)

            connection.commit()
            connection.close()
            print("Database Created")

        except Exception as e:
            print("The database could not be created.")
            print(f"Error Message: {e}")

DatabaseCreator().create_database()