from pydantic import BaseModel , EmailStr , AnyUrl , Field ,field_validator , model_validator
from typing import List , Dict , Optional


## when pydantic own datatypes like EmailStr , AnyUrl , etc are not enough , 
# we can use pydantic validator Field() to validate the data in a whhich covers generally all basic senarios for valtivating a field
## but when our business requirements are more complex , we can use custom validators to validate the data



class Student(BaseModel): 
    name : str = Field(..., min_length=3)
    email : Optional[EmailStr] = None
    age : int 
    weight : float
    allergies : List[str]
    contact_details : Dict[str, str]
    marrried : bool = Field(default=False, description="Whether the student is married or not")


    ## use1 :: validation of data before creating the instance of the model
    @field_validator('email')
    @classmethod
    def validate_age(cls , value):   ## gets class object as cls and value as the value of the field for validation
        valid_domains = ['hdfc.com' , 'icici.com' , 'bankofindia.com']
        
        domain = value.split('@')[1] ## anish@hdfc.com --> hdfc.com
        if domain not in valid_domains:
            raise ValueError(f"Invalid domain: {domain}")
        return value
    

    ## use2 :: transformation of data before creating the instance of the model
    @field_validator('name')
    @classmethod
    def transform_name(cls , value): 
        return value.upper()


    ##  mode = 'before' in side the @ field_validator access the value of field before type coersion 
    ##  mode = 'after' in side the @ field_validator access the value of field after type coersion  {default}


    @field_validator('age' , mode='before')
    @classmethod
    def validate_age(cls , value): 
        print(type(value))
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age must be between 0 and 100")


    ## model validator ::  you can combine multiple validators to validate the data

    ## an emergyny_contact should be theri if age is > 60
    @model_validator(mode='after')
    def validate_emergency_contact(cls , model):
        if model.age > 60 and ("emergency_contact" not in model.contact_details or not model.contact_details["emergency_contact"]):
            raise ValueError("Emergency contact under contact_details is required if age is > 60")

        return model






student_info = {
    "name": "anish",
    "email": "anish@hdfc.com",
    "age": 20, ## TypeError: '<' not supported between instances of 'int' and 'str' if age is a string passed
    "weight": 70.5,
    "allergies": ["penicillin", "latex"],
    "contact_details": {
        "phone": "+91 9876543210",
    },
    "marrried": True,
}


s1 : Student = Student(**student_info) 

print(s1)


s2 : Student = Student(
    name="anish",
    email="anish@hdfc.com",
    age=61,
    weight=70.5,
    allergies=["penicillin", "latex"],
    contact_details={
        "phone": "+91 9876543210",
        "emergency_contact": "",
    },
    marrried=True,
)

print(s2)