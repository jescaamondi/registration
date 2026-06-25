from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table, add_student, get_students, update_student, delete_student, add_teacher,add_courses, get_teachers, get_courses, update_teachers,update_courses,delete_courses,delete_teacher

app=FastAPI()

@app.get("/")
def home():
    return {"message":"welcome to my first server"}


#students
class Student(BaseModel):
    name:str # this formart of code writing is called type hint
    age:int
    email:str
    country:str
    id_number:int

@app.get("/students")
def list_students():
    students=get_students()
    return students


@app.post("/students")
def register_student(student:Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message":"student registered","student":student}

@app.put("/students")
def update_profile(student_id:int, student:Student):
    update_student(student_id, student.email, student.country)
    return {
        "message":f"Student {student_id} profile updated successfully",
        "new_email":student.email,
        "new_country":student.country
    }

@app.delete("/students")
def remove_student(student_id:int):
    delete_student(student_id)
    return{"message": f"Student {student_id} has been deleted"}


#teachers
class Teachers(BaseModel):
    full_name:str
    email:str
    id_number:int
    course:str

@app.get("/teachers")
def list_teachers():
    teachers=get_teachers()
    return teachers


@app.post("/teachers")
def register_teachers(teacher:Teachers):
    add_teacher(teacher.full_name, teacher.email, teacher.id_number, teacher.course)
    return {"message":"teacher registered","teacher":teacher}

@app.put("/teachers")
def update_profile_teacher(teacher_id:int, teacher:Teachers):
    update_teachers(teacher_id, teacher.email, teacher.course)
    return {
        "message":f"Teacher {teacher_id} profile updated successfully",
        "new_email":teacher.email,
        "new_course":teacher.course
    }

@app.delete("/teachers")
def remove_teacher(teacher_id:int):
    delete_teacher(teacher_id)
    return{"message": f"Teacher {teacher_id} has been deleted"}



#courses
class Courses(BaseModel):
    course_name:str
    course_acronyms:str
    course_id:int
    department:str

@app.get("/courses")
def list_courses():
    courses=get_courses()
    return courses


@app.post("/courses")
def register_courses(courses:Courses):
    add_courses(courses.course_name, courses.course_acronyms, courses.course_id, courses.department)
    return {"message":"course registered","course":course}

@app.put("/courses")
def update_course(course_id:int, course:Courses):
    update_course(course_id, course.course_acronyms, course.course_name)
    return {
        "message":f"course {course_id} details updated successfully",
        "newcourse_name":course.course_name,
        "newcourse_acronyms":course.course_acronyms
    }

@app.delete("/courses")
def remove_course(course_id:int):
    delete_courses(course_id)
    return{"message": f"Course {course_id} has been deleted"}

