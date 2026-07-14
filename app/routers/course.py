from fastapi import APIRouter
from schema.course import Courses
from repositories.course import(
    add_courses,
    update_courses,
    delete_courses,
    get_courses

)

router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("")
def list_courses():
    courses=get_courses()
    return courses


@router.post("")
def register_courses(course:Courses):
    add_courses(course.course_name, course.course_acronyms, course.course_id, course.department)
    return {"message":"course registered","course":course}

router.put("")
def update_courses(course_id:int, course:Courses):
    update_courses(course_id, course.course_acronyms, course.course_name)
    return {
        "message":f"course {course_id} details updated successfully",
        "newcourse_name":course.course_name,
        "newcourse_acronyms":course.course_acronyms
    }

router.delete("")
def remove_course(course_id:int):
    delete_courses(course_id)
    return{"message": f"Course {course_id} has been deleted"}