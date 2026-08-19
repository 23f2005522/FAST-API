##  here we define the pydantic models for our application --  for data validation and serialization
## promotes data consistency and integrity by enforcing rules and constraints on the data being processed (input from clients).

from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="The name of the user" , example="John Doe")
    email: EmailStr = Field(..., description="The email of the user")
    phone : str | None = Field(... , min_length=10, max_length=15, description="The phone number of the user" , example="+1-123-456-7890" ) ## default value is None, but we can make it optional in the UserCreate model
    


class UserCreate(UserBase):
    phone : Optional[str] = Field(None, min_length=10, max_length=15, description="The phone number of the user", example="+1-123-456-7890") ## overriding the phone field to make it optional for user creation


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50, description="The name of the user")
    phone: Optional[str] = Field(None, min_length=10, max_length=15, description="The phone number of the user", example="+1-123-456-7890")  ## only phone field is updatable for user update


class UserOut(UserBase):
    id: int = Field(..., description="The ID of the user", example=1)

    model_config = ConfigDict(from_attributes=True)
