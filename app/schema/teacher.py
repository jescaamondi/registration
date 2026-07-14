from pydantic import BaseModel

#teachers
class Teachers(BaseModel):
    full_name:str
    email:str
    id_number:int
    course:str