from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, controller, repository
from .repository import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Taskitech API')


# Get the database
def get_db():
    db = repository.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the user exist
    db_user = controller.get_user(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email Already Exist")
    return controller.create_user(db=db, user=user)

@app.post("/tasks/", response_model=schemas.Task)
def create_task(user: int, task: schemas.CreateTask, db: Session = Depends(get_db)):
    return controller.create_task(db=db, task=task, user_id=user)