from database import get_connection

def create_table():
    with get_connection() as connection: #avoid creating dublicate tables
        connection.execute(''' CREATE TABLE IF NOT EXISTS Courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT NOT NULL,
                    course_acronyms TEXT NOT NULL,
                    course_id INTEGER NOT NULL,
                    department TEXT NOT NULL
                )''')