from fastapi import APIRouter
from schema.student import Student
from repositories.student import(
    add_student,
    get_students,
    update_student,
    delete_student
)

router = APIRouter(prefix="/students", tags=["students"])

@router.get("")
def list_students():
    students=get_students()
    return students


@router.post("")
def register_student(student:Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number)
    return {"message":"student registered","student":student}

@router.put("")
def update_profile(student_id:int, student:Student):
    update_student(student_id, student.email, student.country)
    return {
        "message":f"Student {student_id} profile updated successfully",
        "new_email":student.email,
        "new_country":student.country
    }

@router.delete("")
def remove_student(student_id:int):
    delete_student(student_id)
    return{"message": f"Student {student_id} has been deleted"}

