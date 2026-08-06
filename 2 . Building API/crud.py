from fastapi import FastAPI , HTTPException
from models import Employee
from typing import List, Dict ## typing is a module that provides a way to type hint in python


employees : List[Employee] = [] 


app = FastAPI()


## Path Parameters : are the dynamic part of URL used to identify a resource. 
## URL : http://localhost:8000/employees/1  or http://localhost:8000/employees/2  etc.
## syntax : http://localhost:8000/employees/{path_parameter}
## and passed as an argument to the function as a parameter.
## Example : @app.get("/employees/{id}" , response_model=Employee)
## def get_employee(id: int):
##    return employees[id-1]


## Query Parameters : are the optional part of URL used to filter or sort data.
## URL : http://localhost:8000/employees?page=1&limit=10 
## syntax : http://localhost:8000/employees?query_parameter=value
## and passed as an argument to the function as a parameter.
## Example : @app.get("/employees" , response_model=List[Employee])
## def get_employees(page: int = 1, limit: int = 10): 
##    return employees[(page-1)*limit:page*limit]




# 1. read all employees

@app.get("/employees" , response_model=List[Employee])
def get_employees():
    return employees


# 2. read specific employee

@app.get("/employees/{id}" , response_model=Employee)
def get_employee(id: int):

    for employee in employees:
        if employee.id == id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


# 3. create new employee

@app.post("/employees" , response_model=Employee)
def create_employee(new_employee: Employee):


    # validation if it already exists
    for employee in employees:
        if employee.id == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee already exists")

    employees.append(new_employee)

    return new_employee

# 4. update employee

@app.put("/employees/{id}" , response_model=Employee)
def update_employee(id: int, updated_employee: Employee): ## updated employee is to be sent in the body of the request as per the request body schema


    for employee in employees:
        if employee.id == id:
            employee.name = updated_employee.name if updated_employee.name else employee.name   
            employee.department = updated_employee.department if updated_employee.department else employee.department
            employee.age = updated_employee.age if updated_employee.age else employee.age
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")



# 5. delete employee

@app.delete("/employees/{id}" , response_model=Employee)
def delete_employee(id: int): ## ID is the path parameter changed to integer type ? Yes it is
    for employee in employees:
        if employee.id == id:
            employees.remove(employee)
            return {"status": "success", "message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")


