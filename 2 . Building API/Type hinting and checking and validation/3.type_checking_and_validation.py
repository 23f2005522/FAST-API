# Type checking is a way to which shows us if we are using the correct type of the variable in the code.
# as a squiggly line under the variable (static analysis)
# but still it will run the code. and the type are not enforced at runtime.
# for type checking we use various tools like mypy, pylint, flake8, etc.


## we wil use the mypy tool to do the type checking.


# name: str = 10 # this will show a squiggly line under the variable and it will not throw an error at runtime.

# print(name) # this will print the value of the variable.


####### 0r ############


def create_user(first_name: str , last_name : str , age : int) -> dict : 
    return {
        "first_name" : first_name,
        "last_name" : last_name,
        "age" : age
    }

u1 : dict = create_user("John" , "Doe" , 20) # this is correct type of the variable.
print(u1) # this will print the value of the variable.

# u2 : dict = create_user("Anand" , "Kumar" , "twenty") 
# this will show a squiggly line under the variable and it will not throw an error at runtime.
# print(u2) # this will print the value of the variable.


## we care doing on static type checking in the code. but not runtime type checking.









## data validation : process of checking if the data is valid and meets the requirements. if not then it will raise an error.
## type checking + type enforcement at runtime. = data validation.


## we will use the pydantic library to do the data validation. 
## and some other usecases like validation of the data in the database, type conversion if needed,
#  validation of the data in the file, validation of the data in the network, etc.



## manual data validation :

def adv_create_user(first_name: str , last_name : str , age : int) -> dict : 
    if not isinstance(first_name, str) :
        raise ValueError("First name must be a string")
    if not isinstance(last_name, str) :
        raise ValueError("Last name must be a string")
    if not isinstance(age, int) :
        raise ValueError("Age must be an integer")
    return {
        "first_name" : first_name,
        "last_name" : last_name,    
        "age" : age
    }


u3 : dict = adv_create_user("John" , "Doe" , 20) # this is correct type of the variable.
print(u3) # this will print the value of the variable.

# u4 : dict = adv_create_user("Anand" , "Kumar" , "twenty") 
# this will show a squiggly line under the variable and it will not throw an error at runtime.
# print(u4) # this will print the value of the variable.



## pydantic simplifies the data validation by using the pydantic model.


from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    age: int

u5 : User = User(first_name="John" , last_name="Doe" , age=20) # this is correct type of the variable.
print(u5) # this will print the value of the variable.

# u6 : User = User(first_name="Anand" , last_name="Kumar" , age="twenty") 
# error : age : Input should be a valid integer, unable to parse string as an integer



##type conversion if needed :

# u7 : User = User(first_name="John" , last_name="Doe" , age="20") 
# this is not correct type of the variable for age field.
# (but still give squiggly line under the variable due to the static type checking.)
# print(u7) # this will print the value of the variable.