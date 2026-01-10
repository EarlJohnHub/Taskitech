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

@app.post("/create-tasks/", response_model=schemas.Task)
def create_task(user: int, task: schemas.CreateTask, db: Session = Depends(get_db)):
    return controller.create_task(db=db, task=task, user_id=user)

@app.get("/get-task/",response_model=schemas.Task)
def get_task(user: int ,db: Session = Depends(get_db)):
    return controller.get_task(db=db, current_user_id=user)

@app.patch("/update-task/{task}", response_model=List[schemas.Task])
def update_task(task: int, user: int, task_update: schemas.UpdateTask, db: Session = Depends(get_db)):

    db_task = controller.update_task(db=db, current_task=task, current_owner=user, task_update=task_update)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Something went wrong")
    # This is lacking we have to handle the errors when there are no task to update
    return db_task

@app.delete("/delete-task/{task}", response_model=schemas.Task)
def delete_task(task: int, user: int, db: Session = Depends(get_db)):

    db_task = controller.delete_task(db=db, current_task=task, current_owner=user)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Unable to delete task or Somethings where not ment to be gone awit")

    return db_task