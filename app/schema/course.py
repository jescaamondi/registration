from pydantic import BaseModel

#courses
class Courses(BaseModel):
    course_name:str
    course_acronyms:str
    course_id:int
    department:str