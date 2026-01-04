import datetime
from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    # new_user = models.User(
    #     fullname = n_fullname,
    #     password = n_password,
    #     email = n_email
    # )
    # db.add(new_user)
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, email: str):

    # This will get the user with the same email 
    return db.query(models.User).filter(models.User.email == email).first()
    pass

def get_task(db: Session, current_user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == current_user_id).first()
    pass

def create_task(db: Session, task: schemas.CreateTask, user_id: int):
    # We call the schema for creating the task 
    db_task = models.Task(**task.model_dump(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, current_task: int, current_owner: int, task_update: schemas.UpdateTask):
    
    #We have to find the Task by using the task_id and owner_id
    db_task = db.query(models.Task).filter(
        models.Task.id == current_task,
        models.Task.owner_id == current_owner
    ).first()

    # If we found nothing we return nothing -malamang-
    if not db_task:
        return None
    
    update_data = task_update.model_dump(exclude_unset=True)
    # We loop through the entire schema and set
    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)

    return db_task


def delete_task(db: Session, current_task: int, current_owner: int):
    db_task = db.query(models.Task).filter(
        models.Task.id == current_task,
        models.Task.owner_id == current_owner
    ).first()

    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False
    

