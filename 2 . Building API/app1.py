from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int

# normal dictionary
@app.get("/")
def get_data():
    '''
        - **Return** : Json Object
            - **Name** : Anish
            - **age** : 22
    '''
    
    
    return {"name": "anish", "age": 22}


# returning wrong data type 
@app.get("/user-wrong" ,response_model=User)
def get_user_wrong():
    return {"name": 1234, "age": 22}


# returning in correct instance of User class
@app.get("/user-correct" , response_model=User)
def get_user_correct():
    return {"name": "anish", "age": 22.5}


# returning in correct instance of User class
@app.get("/user-correct2" , response_model=User)
def get_user_correct2():
    return User(name="anish", age=22)


## What happens when use pydantic 
## Validation is done on the client side by pydantic model
## and on the server side by fastapi checks the response_model and validates the data



