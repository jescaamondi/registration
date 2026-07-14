from models import students,teacher, course

def create_table():
    students.create_table()
    teacher.create_table()
    course.create_table()