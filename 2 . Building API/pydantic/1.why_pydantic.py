# def insert_patient_data(name , age):  ## written senior devlopers code
#     print(name)
#     print(age)
#     print("Patient data inserted successfully")



# # now when the junior devlopers comes and writes the code they used it like this
# insert_patient_data("John", "Twenty")
# # now if the senior devlopers expected age will be intger which will be passed by the junior devlopers it may cause error 




## we can use type hinting (only documntation) to solve this problem

# def insert_patient_data(name : str , age : int):
#     print(name)
#     print(age)
#     print("Patient data inserted successfully")

# insert_patient_data("John", 20) # no error will be raised


# ## can be solved by manual validation but it is not efficient and it is not a good practice

# def insert_patient_data(name : str , age : int):
#     if not isinstance(name, str):
#         raise ValueError("Name must be a string")
#     if not isinstance(age, int):
#         raise ValueError("Age must be an integer")
#     print(name)
#     print(age)
#     print("Patient data inserted successfully")

# insert_patient_data("John", "Twenty") # error will be raised
# insert_patient_data("John", 20) # no error will be raised




### but this is not scalable  and code dupliction will be there for type enforcing in production code


## and 2nd problem is that if the data is not valid it will not be raised as an error and it will be silently ignored
## fopr example age should be above 18 and below 100 but if the user passes 101 then it will not be raised as an error and it will be silently ignored

## this also can be solved by manual validation but it is not efficient and it is not a good practice


## so we need a way to enforce the type of the data and also to raise an error if the data is not valid using pydantic library





