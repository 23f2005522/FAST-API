from typing import Optional
from pydantic import BaseModel, Field , computed_field


class Patient(BaseModel):
    id : str = Field(..., description="The ID of the patient" , example="P001")
    name : str = Field(... ,description="The name of the patient" , max_length=50)
    age : int = Field(... ,description="The age of the patient" , gt=0 , lt=100 , example=22)
    weight : float = Field(... ,description="The weight of the patient" , gt=0 , lt=200 , example=72.5)
    height : float = Field(... ,description="The height of the patient" , gt=0 , lt=2.5 , example=1.75)
    city : str = Field(... , description="The city of the patient" , max_length=50 , example="Kolkata")


    @computed_field
    @property
    def bmi(self) -> float : 
        return self.weight / (self.height ** 2)

    @computed_field
    @property
    def verdict(self) -> str : 
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi >= 18.5 and self.bmi < 25:
            return "Normal"
        elif self.bmi >= 25 and self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        
        


class PatientUpdate(BaseModel):
    name : Optional[str] = Field(None, description="The name of the patient" , max_length=50)
    age : Optional[int] = Field(None, description="The age of the patient" , gt=0 , lt=100 , example=22)
    weight : Optional[float] = Field(None, description="The weight of the patient" , gt=0 , lt=200 , example=72.5)
    height : Optional[float] = Field(None, description="The height of the patient" , gt=0 , lt=2.5 , example=1.75)
    city : Optional[str] = Field(None, description="The city of the patient" , max_length=50 , example="Kolkata")
