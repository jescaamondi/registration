from pydantic import BaseModel

#students
class Student(BaseModel):
    name:str # this formart of code writing is called type hint
    age:int
    email:str
    country:str
    id_number:int