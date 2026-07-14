from fastapi import APIRouter
from schema.teacher import Teachers
from repositories.teacher import(
    add_teacher,
    get_teachers,
    update_teachers,
    delete_teacher

)
router = APIRouter(prefix="/teacher", tags=["teacher"])


@router.get("")
def list_teachers():
    teachers=get_teachers()
    return teachers


@router.post("")
def register_teachers(teacher:Teachers):
    add_teacher(teacher.full_name, teacher.email, teacher.id_number, teacher.course)
    return {"message":"teacher registered","teacher":teacher}

@router.put("")
def update_profile_teacher(teacher_id:int, teacher:Teachers):
    update_teacher(teacher_id, teacher.email, teacher.course)
    return {
        "message":f"Teacher {teacher_id} profile updated successfully",
        "new_email":teacher.email,
        "new_course":teacher.course
    }

@router.delete("")
def remove_teacher(teacher_id:int):
    delete_teacher(teacher_id)
    return{"message": f"Teacher {teacher_id} has been deleted"}

