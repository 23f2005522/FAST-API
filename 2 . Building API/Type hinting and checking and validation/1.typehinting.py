# type hinting or type annotation is a way to tell the type of the variable or function parameters or return value in the code 
# which jsut increases the readability and maintainability of the code.
# the type is not enforced at runtime, it is only used by the IDE to provide autocomplete and type checking.




# Without type hints
def add(a, b):
    return a + b

# With type hints
def add_2(a: int, b: int) -> int:
    return a + b


## more examples
def create_user(first_name: str, age: int, last_name: str) :
    email = f"{first_name}.{last_name}@example.com" # did not give type hint whaich is obvious by seeing the code
    return {
        "first_name": first_name,
        "age": age,
        "last_name": last_name,
        "email": email
    }
    



user1 : dict = create_user("John", 25, "Doe")

# try to write user1. then enter tab key then the see the suggestions will come .keys() and so on for the dictionary 
print(user1)

a : list[int] = [1, 2, 3, 4, 5] 
# try to write a.  then enter tab key then the see the suggestions will come .append() and so on for the lists 




## but but but 
## if we do like 

# user2: dict = create_user("anish", "25", "kumar") ## this still work and not throw error which is not expected 
# print(user2) 

# for example why this can be a problem ?
# because the type hinting is only used by the IDE to provide autocomplete and type checking. and dont enforce it at runtime.
# consider the following example :

def process_numbers(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num  # Assumes num is int
    return total

# Your code says it expects list[int]...
# process_numbers([1, 2, 3])  # ✓ Works fine

# But Python lets you pass this:
# process_numbers([1, "two", 3])  # ❌ Has a string! Will crash at runtime with TypeError

# Or this completely wrong thing:
# process_numbers("123")  # ❌ No error from Python during call, crashes when iterating

## what we learn from this ?
# type hinting is not a security feature, it is only used to provide autocomplete and type checking.



## so what is the solution ?
## Type checking :  we can use type checking to enforce the type of the variable at runtime.

