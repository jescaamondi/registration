from database import get_connection


def add_courses(course_name, course_acronyms,course_id, department):
     with get_connection() as connection:
        connection.execute(
            'INSERT INTO Courses(course_name, course_acronyms, course_id,department) VALUES(?,?,?,?)',
            (course_name, course_acronyms, course_id,department),
        )

def get_courses():
     with get_connection() as connection:
        return connection.execute('SELECT*FROM courses').fetchall()
        
def update_courses(course_id, newcourse_name,newcourse_acronyms):
     with get_connection() as connection:
        connection.execute(
            'UPDATE courses SET course_acronyms=?,course_name=? WHERE id =?',
            (course_id, new_course_name,new_course_acronyms)
        )
def delete_courses(course_id):
    with get_connection() as connection:
        connection.execute(
            'DELETE FROM courses WHERE id =?', (course_id,)
        )