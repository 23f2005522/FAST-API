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



## Unpacking in Python  :  allows you to extract individual elements from a collection (like a list, tuple, or dictionary) and assign them to separate variables in a single line of code

# 1. Basic Iterable UnpackingYou can assign elements of a tuple or list directly to comma-separated variables. The number of variables must match the number of items exactly, or Python raises a ValueError

# # Unpacking a tuple
# coordinates = (4, 5)
# x, y = coordinates
# print(x)  # Output: 4

# # Unpacking a list
# fruits = ["apple", "banana"]
# first, second = fruits


# 2. Extended Unpacking (The * Operator)If you do not know the exact length of the collection or only care about specific elements, use the single asterisk (*) operator. It captures the remaining unassigned elements into a new list


# numbers = [1, 2, 3, 4, 5]

# # Grab the first element, collect the rest
# first, *rest = numbers
# print(first)  # Output: 1
# print(rest)   # Output: [2, 3, 4, 5]

# # Grab the first and last elements, collect the middle
# first, *middle, last = numbers
# print(middle) # Output: [2, 3, 4]



# 3. Ignoring Values (_)By convention, if you want to unpack a collection but discard certain items, assign them to an underscore (_).python


# # Ignore the middle values
# start, *_, end = [10, 20, 30, 40, 50]
# print(start, end)  # Output: 10 50




# 4. Dictionary Unpacking  : When you unpack a dictionary directly, Python defaults to unpacking its keys. You can explicitly unpack .values() or .items() if needed

# user = {"name": "Alice", "age": 30}

# # Default unpacking targets keys
# key1, key2 = user 
# print(key1)  # Output: name

# # Unpacking values
# name, age = user.values()
# print(name)  # Output: Alice


# 5. Merging CollectionsThe single asterisk (*) and double asterisk (**) operators are also used to unpack and merge multiple collections inside literals.


# # Merging lists
# list_a = [1, 2]
# list_b = [3, 4]
# combined_list = [*list_a, *list_b]  # [1, 2, 3, 4]

# # Merging dictionaries
# dict_a = {"x": 1}
# dict_b = {"y": 2}
# combined_dict = {**dict_a, **dict_b}  # {'x': 1, 'y': 2}


# 6. Unpacking in Function ArgumentsYou can pass an iterable into a function as individual positional arguments using *, or pass a dictionary as keyword arguments using **


# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# # Unpacking a list into positional arguments
# data = ["Bob", 25]
# greet(*data)

# # Unpacking a dict into keyword arguments
# data_dict = {"name": "Charlie", "age": 40}
# greet(**data_dict)