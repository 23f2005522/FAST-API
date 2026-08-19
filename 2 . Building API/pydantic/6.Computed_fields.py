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


# The @property decorator in Python is a built-in tool that allows you to turn a class method into a "read-only" attribute . 
# It lets you access, modify, or delete a class attribute like a normal variable, while secretly executing custom code behind the scenes to handle validation, dynamic calculations, or logging.

# The Core Components: 
#     @property: Defines the Getter method to retrieve the attribute value.@<attribute_name>.setter: Defines the Setter method to validate and assign a new value.@<attribute_name>.deleter: Defines the Deleter method to clear or delete the attribute
    
#     @<attribute_name>.setter: Defines the Setter method to validate and assign a new value
    
#     @<attribute_name>.setter: Defines the Setter method to validate and assign a new value



# Code Example: Temperature Controller 

# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius  # Internal "private" attribute

#     # 1. Getter: Access value without parenthesis
#     @property
#     def celsius(self):
#         print("Fetching temperature...")
#         return self._celsius

#     # 2. Setter: Add data validation logic
#     @celsius.setter
#     def celsius(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature below absolute zero is impossible!")
#         print("Setting temperature...")
#         self._celsius = value

#     # 3. Deleter: Clean up resources on deletion
#     @celsius.deleter
#     def celsius(self):
#         print("Deleting temperature records...")
#         del self._celsius


# # Create an instance
# temp = Temperature(25)

# # Triggers the Getter (@property)
# print(temp.celsius)  
# # Output:
# # Fetching temperature...
# # 25

# # Triggers the Setter (@celsius.setter)
# temp.celsius = 30  
# # Output: Setting temperature...

# # Triggers data validation error
# temp.celsius = -300  
# # Output: ValueError: Temperature below absolute zero is impossible!

# # Triggers the Deleter (@celsius.deleter)
# del temp.celsius  
# # Output: Deleting temperature records...
