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
            print("password must be greater than 8 characters")
        return value

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: bool

    due_date: Optional[datetime] = None
    owner_id: int

    
    model_config = {
        "from_attributes" : True
    }

class CreateTask(BaseModel):
    title: str
    description: Optional[str] = None
    status: bool
    due_date: Optional[datetime] = None