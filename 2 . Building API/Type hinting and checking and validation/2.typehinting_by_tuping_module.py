
## The typing module is a built-in Python module (you don't install it) that provides tools to write more sophisticated type hints.
## typing module is built upon and directly extends Python’s native types to support structural static type checking
#  It's still just documentation for your code — Python doesn't enforce it.

# Why You Need It : Basic types like str, int, list don't capture complex type requirements

# for example :

# Basic types can't express:
# - A list of strings (not just "list")
# - A function that takes either int or str
# - A dictionary with specific key/value types
# - Optional values (might be None)
# - Custom generic types

# That's where typing module comes in!


from typing import Callable, Optional, List, Dict, Tuple, Union


### 1. Optional - Value might be None
def find_user(user_id: int) -> Optional[str]:
    """Returns username or None if not found"""
    if user_id == 1:
        return "Alice"
    return None  # ✓ Valid because return type includes None possibility

# Usage
name = find_user(1)  # Type is str | None


###2. List, Dict, Tuple - Specify container element types
# List of specific type
def get_names() -> List[str]:
    return ["Alice", "Bob", "Charlie"]

# Dictionary with specific key/value types
def user_ages() -> Dict[str, int]:
    return {"Alice": 25, "Bob": 30}

# Tuple with specific order and types
def coordinates() -> Tuple[float, float, float]:
    return (10.5, 20.3, 30.1)




### 3. Union - Multiple possible types


def process(value: Union[int, str]) -> Union[int, str]:
    """Can receive int or str, returns int or str"""
    if isinstance(value, int):
        return value * 2
    return value.upper()

print(process(1))
print(process("hello"))

# Python 3.10+ shorthand
def process_modern(value: int | str) -> int | str:
    """Same thing, newer syntax"""
    if isinstance(value, int):
        return value * 2
    return value.upper()

print(process_modern(1))
print(process_modern("hello"))



##4. Callable - Functions as parameters


def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    """Takes two ints and a function that takes two ints and returns int"""
    return operation(a, b)

# Usage
def multiply(x: int, y: int) -> int:
    return x * y

result = apply_operation(5, 3, multiply)  # Returns 15
print(result)