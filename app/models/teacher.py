from database import get_connection

def create_table():
    with get_connection() as connection: #avoid creating dublicate tables
        connection.execute(''' CREATE TABLE IF NOT EXISTS Teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    id_number INTEGER NOT NULL,
                    course TEXT NOT NULL
                )''')