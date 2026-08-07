from pydantic import BaseModel, Field ,  computed_field
from typing import  Dict , Optional


## benifits of nested models ::
## 1. Better data organization of related data (eg: address of a user or cars details of a user)
## 2. Reuseability : use Vital details in multiple models (eg: address of a user in multiple models)
## 3. Readability : easier for dev and API comsumers to understand the data 
## 4. Validation  : nested models are validated automatically-no extra code required



class Address(BaseModel): 
    street : str = Field(..., example="123 Main St")
    city : str = Field(..., example="New York")
    state : str = Field(..., example="NY")
    zip_code : str = Field(..., example="10001")


class User(BaseModel):
    name : str = Field(..., example="John Doe")
    email : str = Field(..., format="email" , example="Student_name@iitm.ac.in")
    age : int = Field(..., gt=18)
    weight : float = Field(..., gt=50)
    height : float = Field(..., gt=150)
    is_active : bool = Field(default=True , example=True)
    contact_detail : Optional[Dict[str, str]] = None
    address : Address = Field(..., example=Address(street="123 Main St", city="New York", state="NY", zip_code="10001"))


    @computed_field
    @property
    def full_address(self)->str : 
        return f"{self.address.street}, {self.address.city}, {self.address.state}, {self.address.zip_code}"


    @computed_field
    @property
    def bmi_value(self)->float : 
        return self.weight / (self.height ** 2)


def print_user_data(user : User):
    print(f"Name: {user.name}")
    print(f"Email: {user.email}")
    print(f"Age: {user.age}")
    print(f"Weight: {user.weight}")
    print(f"Height: {user.height}")
    print(f"BMI: {user.bmi_value}")
    print(f"Is Active: {user.is_active}")
    print(f"Contact Detail: {user.contact_detail}")
    print(f"Address: {user.full_address}")


def print_address_data(address : Address):
    print(f"Street: {address.street}")
    print(f"City: {address.city}")
    print(f"State: {address.state}")
    print(f"Zip Code: {address.zip_code}")

u1_a1 : Address = Address(street="123 Main St", city="New York", state="NY", zip_code="10001")

u1 : User = User(
    name="anish bhat" , 
    email="anish@iitm.ac.in" , 
    age=20 , 
    weight=70 , 
    height=170 , 
    is_active=True , 
    contact_detail={"phone":"+91 9876543210" , "email":"anish@iitm.ac.in"},
    address=u1_a1
)

print_user_data(u1)
print_address_data(u1_a1)