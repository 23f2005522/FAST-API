# serialization :: converting Pydantic models to JSON or other data formats (Python dict or list of dicts etc)

from pydantic import BaseModel, Field ,  computed_field
from typing import  Dict , Optional


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




u1 : User = User(
    name="anish bhat" , 
    email="anish@iitm.ac.in" , 
    age=20 , 
    weight=70 , 
    height=170 , 
    is_active=True , 
    contact_detail={"phone":"+91 9876543210" , "email":"anish@iitm.ac.in"},
    address=Address(street="123 Main St", city="New York", state="NY", zip_code="10001")
)


u1_dict : dict = u1.model_dump()
print(u1_dict , type(u1_dict))
print(u1_dict["name"]) ## accessing the data from the dictionary


u1_json : str = u1.model_dump_json(exclude={'address':["zip_code"]})
print(u1_json , type(u1_json)) ## python resives in string format which is properly json serialized format 

## include=["name" , "email" , "age" , "weight" , "height" , "is_active" , "contact_detail" , "address"] :: to include only the specified fields in the serialized output
## exclude=["address"] :: to exclude the specified fields in the serialized output
## exclude


