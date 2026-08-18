from pydantic import BaseModel, EmailStr , AnyUrl , Field
from typing import List, Dict , Optional


class Patient(BaseModel):
    name: str
    age: int = 18
    weight: float 
    married: Optional[bool] = False 
    email: EmailStr
    linkedin_url: AnyUrl
    allergies: List[str]
    contact_deactials: Dict[str, str]


def insert_patient_data(patient : Patient):
    print(patient)
    print("Patient data inserted successfully")



patient_info = {
    "name": "ankit",
    "age": 20,
    "weight": 70.5,
    # "married": True,
    "email": "ankit@example.com",
    "linkedin_url": "https://www.linkedin.com/in/ankit",
    "allergies": ["penicillin", "latex"],
    "contact_deactials": {
        "phone": "+91 9876543210",
    }
}


patient = Patient(**patient_info)

insert_patient_data(patient)




## now towards data validation 


## way 1  ::  by pydantic by custom Datatypes which internally uses field_validator

## example of custom datatype , EmailStr is a custom datatype
## for URL validation we can use AnyUrl   datatype
## for Phone number validation we can use PhoneNumberStr   datatype
#etc ... 





## way 2  ::  by pydantic by Field() (for custom validators)
class Student(BaseModel): 
    name: str = Field(min_length=3, max_length=100 , default="StudentName")  ## with a default value of Name is "StudentName"
    age : int = Field(gt=18 , lt=100 , description="Age must be between 18 and 100" ,)  ## with a description of Age must be between 18 and 100
    weight : float = Field(gt=50 , lt=100 , description="Weight must be between 50 and 100" , strict=True)
    email : EmailStr = Field(default="student@example.com")
    linkedin_url : AnyUrl = Field(default="https://www.linkedin.com/in/studentname")
    allergies : List[str] = Field(default=["penicillin", "latex"])
    contact_deactials : Dict[str, str] = Field(default={
        "phone": "+91 9876543210",
        "email": "student@example.com"
    })



### Annotated vs Field() — related, but NOT the same
#
# Field()  → Pydantic function. Does the real work: constraints, default, description, alias, strict, etc.
#   age: int = Field(gt=18, lt=100, description="...")
#
# Annotated → from typing. Only a wrapper that attaches metadata to a type.  syntax -- Annotated[TYPE, METADATA]
#   Pydantic reads that metadata (often Field(...) inside Annotated).
#   from typing import Annotated
#   age: Annotated[int, "must be positive"]  ## The important point is that Annotated itself doesn't perform validation. It essentially says: The type is int, and I'm attaching some additional metadata to it.

#
# Style A (Field as default)          →  name: str = Field(min_length=3)
# Style B (Annotated + Field)         →  name: Annotated[str, Field(min_length=3)]
# Same validation when Field is used. Newer Pydantic docs prefer Annotated.
# Defaults:  age: int = Field(default=18)  OR  age: Annotated[int, Field(gt=18)] = 18
#
#



## Example of using Annotated with Field() for validation

# from typing import Annotated
# from pydantic import BaseModel, Field

# class User(BaseModel):
#     username : Annotated[str , Field(min_length=3 , max_length=50 , description="Username must be between 3 and 50 characters")]
#     age : Annotated[int , Field(gt=18 , lt=100 , description="Age must be between 18 and 100")]
#     roll : Annotated[int , Field(gt=1 , lt=1000 , description="Roll number must be between 1 and 1000")]
#     email : Annotated[EmailStr , Field(description="Email must be a valid email address")]
#     address : Annotated[Dict[str , str] , Field(description="Address must be a dictionary with keys 'street', 'city', 'state', 'zip'" , default={"street": "123 Main St", "city": "Anytown", "state": "CA", "zip": "12345"})]



# user_info = {
#     "username": "john_doe",
#     "age": 25,
#     "roll": 123,
#     "email": "john.doe@example.com"
# }

# user1 : User = User(**user_info)
# print(user1)


### Suppress type conversion with strict=True inside Field()
# By default Pydantic coerces types: age="20" (str) → int 20  (allowed)
# With strict=True, that conversion is blocked — value must already be the correct type.
#
#   class StrictStudent(BaseModel):
#       age: int = Field(gt=18, lt=100, strict=True)
#       # OR with Annotated:
#       # age: Annotated[int, Field(gt=18, lt=100, strict=True)]
#
#   StrictStudent(age=20)      # OK — already int
#   StrictStudent(age="20")    # ERROR — str will NOT be converted to int
