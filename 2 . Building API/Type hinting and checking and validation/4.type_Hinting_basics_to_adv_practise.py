name :  str = "John"
age :  int = 30


def create_user(first_name: str, last_name: str, age: int | None = None) -> dict[str , str | int | None]:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
    }



# type checking using mypy + type hinting by python itself 

# u1 : dict = create_user("John", "Doe", "30") # but it will still run without errors  but the static analyzer will show errors by mypy

# print(u1)



##  age: int | None = None before 3.10 we had to use Optional[int] but now we can use int | None 

# example :

# from typing import Optional
# def create_user(first_name: str, last_name: str, age: Optional[int] = None) -> dict:
#     email = f"{first_name.lower()}.{last_name.lower()}@example.com"
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "age": age,
#         "email": email,
#     }


## with litbut more complex data 
## this def create_user(first_name: str, last_name: str, age: int | None = None) -> dict[str , str | int | None]
## might get really messy and hard to read and understand  and crowed the fucion code


### solution :  type alias 

## Type Alias : this is a way to give a name to a type made up of other types



user_type = dict[str , str | int | None]

def create_user_2(first_name: str, last_name: str, age: int | None = None) -> user_type:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
    }


# a newer syntax for type alias is the following (for explicit shoiwing this is a type alias) :

# Python 3.12+ PEP 695:  type User = dict[str, str | int | None]
# mypy may not support that yet, so use TypeAlias (works with mypy):

## newer syntax for type alias is the following (for explicit shoiwing this is a type alias) :
        ## syntax : type Name: Type = Value
        ## example :
        ## type RGB: tuple[int, int, int] = (255, 0, 0)
        ## type HSL: tuple[int, int, int] = (0, 0, 0)
        ## type User: dict[str, str | int | None] = {
        ##     "first_name": "John",
        ##     "last_name": "Doe",
        ##     "age": 30,
        ##     "email": "john.doe@example.com",
        ## }

        
from typing import TypeAlias

RGB: TypeAlias = tuple[int, int, int]
HSL: TypeAlias = tuple[int, int, int]

def get_rgb_value(rgb: RGB) -> dict[str , int]:
    return {
        "red": rgb[0],
        "green": rgb[1],
        "blue": rgb[2],
    }

user_type_2: TypeAlias = dict[str , str | int | None | RGB]

def create_user_3(first_name: str, last_name: str, age: int | None = None , fav_color : RGB | HSL | None = None) -> user_type_2:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
        "fav_color" : fav_color,
    }

print(create_user_3("John", "Doe", 30, (255, 0, 0)))



## suppose our code base has also HSL values :
# HSL already defined above with TypeAlias
# aour develor by mistake passes hsl value to the create_user_3 which is incorrect type but still will not show errors by mypy

hsl_value = (0, 0, 0)

print(create_user_3("John", "Doe", 30, hsl_value)) # this will not show errors by mypy



## solution : NewType of typing module  ::  create a new type from an existing type

from typing import NewType


RGB_1 = NewType("RGB_1", tuple[int , int , int])
HSL_1 = NewType("HSL_1", tuple[int , int , int])


user_type_3 = dict[str , str | int | None | RGB_1]

def create_user_4(first_name: str, last_name: str, age: int | None = None , fav_color : RGB_1| None = None) -> user_type_3:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
        "fav_color" : fav_color,
    }


# print(create_user_4("John", "Doe", 30, (255, 0, 0))) ## showing errors by mypy 
# print(create_user_4("John", "Doe", 30, (0, 0, 0))) ## showing errors by mypy

## why ? 

## because NewType is a subclass of the original type and not a type itself
## so (255, 0, 0) is not a RGB_1 or HSL_1 but a tuple[int , int , int]
## so we need to use type union to allow both RGB_1 and HSL_1

## for correct syntax 
print(create_user_4("John", "Doe", 30, RGB_1((255, 0, 0)))) ## specify the type of the value --  Type casting to RGB_1

## this will not show errors by mypy

## NewType is a powerful tool to create new types from existing types
## it is a subclass of the original type and not a type itself
## so it is a type itself
## so it can be used to create new types from existing types
## it is a type itself
## so it can be used to create new types from existing types





## now lets say during some oprtaion in process we chaning the value of age to a string  

def create_user_5(first_name: str, last_name: str, age: str | None = None , fav_color : RGB_1  | None = None) -> user_type_3:
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    
    age = str(age) ## to show mid way change of type of age
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
        "fav_color" : fav_color,
    }


# how to fix that  ::  TypedDict from typing module

from typing import TypedDict

class User(TypedDict):
    first_name: str
    last_name: str
    age: int | None
    email: str
    fav_color: RGB_1 | None


def create_user_6(first_name: str, last_name: str, age: int | None = None , fav_color : RGB_1  | None = None) -> User:
    
    # age = str(age) ## to show mid way change of type of age to string :: capture by mypy
    
    return User(
        first_name=first_name,
        last_name=last_name,
        age=age,
        email=f"{first_name.lower()}.{last_name.lower()}@example.com",
        fav_color=fav_color,
    )

# u6 : User = create_user_6("anish", "bharti", 30, HSL_1((255, 0, 0))) :: showing errors by mypy as HSL_1 is not a valid type for fav_color
u6 : User = create_user_6("anish", "bharti", 30, RGB_1((255, 0, 0)))
print(u6) ## showing errors by mypy as age is int but we are passing string







## data classses ::  a class that is used to store data and is immutable used mainly for data transfer objects (DTOs)
## and for the purpose of data validation and transformation

from dataclasses import dataclass

@dataclass
class User_data_class:
    first_name: str = "John"
    last_name: str = "Doe"
    age: int | None = 10
    email: str = "example@example.com"
    fav_color: RGB_1 | None = RGB_1((0,0,0))



def create_user_7 (first_name: str, last_name: str, age: int | None = None , fav_color : RGB_1  | None = None) -> User_data_class:
    return User_data_class(
        first_name=first_name,
        last_name=last_name,
        age=age,
        email=f"{first_name.lower()}.{last_name.lower()}@example.com",
        fav_color=fav_color,
    )


# u7 : User_data_class = create_user_7("anish", "bharti", 30, RGB_1((255, 0, 0)))
# print(u7)


# u8 : User_data_class = create_user_7("anish", "bharti", "30", (255, 0, 0))
# print(u8)
# print(u8.first_name , u8.last_name , u8.age , u8.email , u8.fav_color)

