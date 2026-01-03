from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session):
    pass

def get_user(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

    pass

def get_task(db: Session):
    pass

def create_task(Session):
    pass

def update_task(Session):
    pass

def delete_task(Session):
    pass

