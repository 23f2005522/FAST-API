from pydantic import BaseModel

class Patient(BaseModel):
    name : str 
    age : int 



def insert_patient_data(patient : Patient):
    print(patient)
    print("Patient data inserted successfully")


patient_info = { "name": "ankit", "age": 20} ## if age : "twenty" then it will raise an error

patient = Patient(**patient_info) ## ** is used to unpack the dictionary into the constructor ==> name = "ankit", age = 20 ## this will raise an error if the data is not valid


insert_patient_data(patient)




















