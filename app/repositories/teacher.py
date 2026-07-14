from database import get_connection

def add_teacher(full_name, email,id_number, course):
     with get_connection() as connection:
        connection.execute(
            'INSERT INTO students(full_name, email,id_number,course) VALUES(?,?,?,?)',
            (full_name, email,id_number,course),
        )

def get_teachers():
     with get_connection() as connection:
        return connection.execute('SELECT*FROM teachers').fetchall()
        
def update_teachers(teacher_id, new_email,new_course):
     with get_connection() as connection:
        connection.execute(
            'UPDATE students SET email=?, course=? WHERE id =?',
            (teacher_id, new_email,new_course)
        )
def delete_teacher(teacher_id):
    with get_connection() as connection:
        connection.execute(
            'DELETE FROM teachers WHERE id =?', (teacher_id,)
        )
