from fastapi import FastAPI, HTTPException, Path, Query
from models import Employee
from typing import List, Literal  ## typing is a module that provides a way to type hint in python
import json
from pathlib import Path as FilePath


employees: List[Employee] = []

with open(FilePath(__file__).parent / "employess.json", "r") as f:
    data = json.load(f)
    print(data)
    employees = [Employee(**item) for item in data]

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


## Path() from the fastapi is used to provide metadata ,  validation rules adn doc hints to the path parameter in your API endpoints.

# Title : A title for the path parameter.
# Ge : A ge (greater than or equal to) for the path parameter.
# Gt : A gt (greater than) for the path parameter.
# Le : A le (less than or equal to) for the path parameter.
# Lt : A lt (less than) for the path parameter.
# Eq : A eq (equal to) for the path parameter.
# Ne : A ne (not equal to) for the path parameter.
# In : A in (in) for the path parameter.
# NotIn : A notIn (not in) for the path parameter.
# Min_length : A min_length (minimum length) for the path parameter.
# Max_length : A max_length (maximum length) for the path parameter.
# Regex : A regex (regular expression) for the path parameter.


# Query() from the fastapi is used to provide metadata ,validation rules adn doc hints to the query parameter in your API endpoints.
# Title : A title for the query parameter.
# Description : A description for the query parameter.
# Example : An example for the query parameter.
# Default : A default value for the query parameter.
# Ge : A ge (greater than or equal to) for the query parameter.
# Gt : A gt (greater than) for the query parameter.
# Le : A le (less than or equal to) for the query parameter.
# Lt : A lt (less than) for the query parameter.


# 1. read all employees


@app.get("/employee", response_model=List[Employee])
def get_employees():
    return employees


# 2. read specific employee


@app.get("/employee/{id}", response_model=Employee)
def get_employee(id: int):

    for employee in employees:
        if employee.id == id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


# 3. create new employee


@app.post("/employee", response_model=Employee)
def create_employee(new_employee: Employee):

    # validation if it already exists
    for employee in employees:
        if employee.id == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee already exists")

    employees.append(new_employee)

    return new_employee


# 4. update employee


@app.put("/employee/{id}", response_model=Employee)
def update_employee(  # ... means required parameter other wise
    updated_employee: Employee,
    id: int = Path(
        ...,
        description="The ID of the employee to update in array",
        example=1,
    ),
):  ## updated employee is to be sent in the body of the request as per the request body schema

    for employee in employees:
        if employee.id == id:
            employee.name = (
                updated_employee.name if updated_employee.name else employee.name
            )
            employee.department = (
                updated_employee.department
                if updated_employee.department
                else employee.department
            )
            employee.age = (
                updated_employee.age if updated_employee.age else employee.age
            )
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


# 5. delete employee


@app.delete("/employee/{id}")
def delete_employee(
    id: int,
):  ## ID is the path parameter changed to integer type ? Yes it is
    for employee in employees:
        if employee.id == id:
            employees.remove(employee)
            return {"status": "success", "message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")


# 6. search employees by name or department


@app.get("/employees/search", response_model=List[Employee])
def search_employees(
    name: str = Query(
        ...,
        description="The name of the employee to search in array",
        example="John",
    ),
    department: str = Query(
        ...,
        description="The department of the employee to search in array",
        example="IT",
    ),
    order_by: Literal["asc", "desc"] = Query(
        "asc",
        description="Sort the results by a age",
    ),
):
    results = []

    sort_order_bool = True if order_by == "desc" else False

    sorted_employees = sorted(employees, key=lambda x: x.age, reverse=sort_order_bool)

    for employee in sorted_employees:
        if (
            employee.name.lower() == name.lower()
            or employee.department.lower() == department.lower()
        ):
            results.append(employee)
    return results
