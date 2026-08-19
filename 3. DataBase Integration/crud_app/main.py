from fastapi import FastAPI, HTTPException, Depends, Path
from sqlalchemy.orm import Session
from db import engine, SessionLocal, Base
from typing import List
import models, schemas, crud


## create the database tables
Base.metadata.create_all(bind=engine)
### Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
## application instance
app = FastAPI()

## Endpoints for CRUD operations on users

# 1. create a new user
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user : schemas.UserCreate , db: Session = Depends(get_db)):
    crud_user = crud.create_user(db, user)
    return crud_user


#2. get all users
@app.get("/users/", response_model=List[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_all_users(db)
    return users

# 3. get a user by id
@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int = Path(..., gt=0 , example=1), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# 4. update a user by id
@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int = Path(..., gt=0 , example=1), user: schemas.UserUpdate = ..., db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# 5. delete a user by id
@app.delete("/users/{user_id}", response_model=schemas.UserOut)
def delete_user(user_id: int = Path(..., gt=0, example=1), db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


