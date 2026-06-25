import sqlite3
from contextlib import contextmanager

sqlite_file_name="school.db"

@contextmanager
def get_db_connection():
    connection=sqlite3.connect(sqlite_file_name)
    connection.row_factory=sqlite3.Row

    try: #create a connection
        yield connection
        connection.commit()
    finally:
        connection.close() 

def create_table():
    with get_db_connection() as connection: #avoid creating dublicate tables
        connection.execute(''' CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    country TEXT NOT NULL,
                    id_number INTEGER NOT NULL
                )''')

        connection.execute(''' CREATE TABLE IF NOT EXISTS Teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    id_number INTEGER NOT NULL,
                    course TEXT NOT NULL
                )''')
        connection.execute(''' CREATE TABLE IF NOT EXISTS Courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_name TEXT NOT NULL,
                    course_acronyms TEXT NOT NULL,
                    course_id INTEGER NOT NULL,
                    department TEXT NOT NULL
                )''')


#students
def add_student(name, age, email, country,id_number):
     with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students(name, age, email, country,id_number) VALUES(?,?,?,?,?,?)',
            (name, age, email, country,id_number,),
        )

def get_students():
     with get_db_connection() as connection:
        return connection.execute('SELECT*FROM students').fetchall()
        
def update_student(student_id, new_email,new_country):
     with get_db_connection() as connection:
        connection.execute(
            'UPDATE students SET email=?,country=? WHERE id=?',
            (new_email,new_country, student_id)
        )
def delete_student(student_id):
    with get_db_connection() as connection:
        connection.execute(
            'DELETE FROM students WHERE id =?', (student_id,)
        )



#teacher
def add_teacher(full_name, email,id_number, course):
     with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO students(full_name, email,id_number,course) VALUES(?,?,?,?)',
            (full_name, email,id_number,course),
        )

def get_teachers():
     with get_db_connection() as connection:
        return connection.execute('SELECT*FROM teachers').fetchall()
        
def update_teachers(teacher_id, new_email,new_course):
     with get_db_connection() as connection:
        connection.execute(
            'UPDATE students SET email=?,course=? WHERE id =?',
            (teacher_id, new_email,new_course)
        )
def delete_teacher(teacher_id):
    with get_db_connection() as connection:
        connection.execute(
            'DELETE FROM teachers WHERE id =?', (teacher_id,)
        )


#courses
def add_courses(course_name, course_acronyms,course_id, department):
     with get_db_connection() as connection:
        connection.execute(
            'INSERT INTO Courses(course_name, course_acronyms, course_id,department) VALUES(?,?,?,?)',
            (course_name, course_acronyms, course_id,department),
        )

def get_courses():
     with get_db_connection() as connection:
        return connection.execute('SELECT*FROM courses').fetchall()
        
def update_courses(course_id, newcourse_name,newcourse_acronyms):
     with get_db_connection() as connection:
        connection.execute(
            'UPDATE courses SET course_acronyms=?,course_name=? WHERE id =?',
            (course_id, newcourse_name,newcourse_acronyms)
        )
def delete_courses(course_id):
    with get_db_connection() as connection:
        connection.execute(
            'DELETE FROM courses WHERE id =?', (course_id,)
        )