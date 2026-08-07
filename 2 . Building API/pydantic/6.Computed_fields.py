from pydantic import BaseModel , Field , computed_field , field_validator
from typing import List , Dict , Optional


class User(BaseModel):
    name : str = Field(..., min_length=3 , example="John Doe")
    email : str = Field(..., format="email" , example="Student_name@iitm.ac.in")
    age : int = Field(..., gt=18)
    weight : float = Field(..., gt=50)
    height : float = Field(..., gt=150)
    is_active : bool = Field(default=True , example=True)
    contact_detail : Optional[Dict[str, str]] = None



    @field_validator("email")
    @classmethod
    def validate_email(cls , value):
        valid_domain = "iitm.ac.in"
        if value.split("@")[1] != valid_domain:
            raise ValueError("Invalid email domain")
        return value 


    @computed_field
    @property
    def bmi_value(self) -> float :  ## gets instance object as self and returns the computed value
        ## BMI = weight(kg) / height(m)^2
        ## height is stored in cm (170) → convert to meters first, else 70/170^2 ≈ 0.002 → rounds to 0.0
        height_m = self.height / 100
        bmi = self.weight / (height_m ** 2)
        return round(bmi , 2)



def print_user_data(user : User):
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print(f"Age: {user.age}")
    print(f"Weight: {user.weight}")
    print(f"Height: {user.height}")
    print(f"BMI: {user.bmi_value}")
    print(f"Is Active: {user.is_active}")
    print(f"Contact Detail: {user.contact_detail}")


u1 : User = User(
    name="anish bhat" , 
    email="anish@iitm.ac.in" , 
    age=20 , 
    weight=70 , 
    height=170 , 
    is_active=True , 
    contact_detail={"phone":"+91 9876543210" , "email":"anish@iitm.ac.in"}
)

print_user_data(u1)