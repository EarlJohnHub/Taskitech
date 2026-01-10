from datetime import datetime
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class User(BaseModel):
    user_id: int
    email: EmailStr
    fullname: str

    model_config = {
        "from_attributes" : True
    }


class UserCreate(BaseModel):
    fullname: str
    email:  EmailStr
    password: str
    
    @field_validator("password")
    @classmethod
    def validate_account_password(cls, value):
        if len(value) < 8:
            raise ValueError("password must be greater than 8 characters")
        return value

# I have created a base schema for task
# So that I wont have to repeat things over&over
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: bool
    priority: int


class Task(TaskBase):
    id: int
    owner_id: int
    model_config = {
        "from_attributes" : True
    }

class CreateTask(TaskBase):
    pass

class UpdateTask(TaskBase):
    title: Optional[int] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    priority: Optional[int] = None
    due_date: Optional[datetime] = None
