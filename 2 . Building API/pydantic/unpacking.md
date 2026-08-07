# Python Unpacking Cheat Sheet

## 1. Basic Unpacking

Split an iterable into variables.

```python
point = (10, 20)
x, y = point
```

```python
fruits = ["Apple", "Banana", "Mango"]
a, b, c = fruits
```

---

## 2. Extended Unpacking (`*`)

Capture the remaining values.

```python
nums = [1, 2, 3, 4, 5]

first, *rest = nums
# first = 1
# rest = [2,3,4,5]
```

```python
first, *middle, last = nums
# first = 1
# middle = [2,3,4]
# last = 5
```

Ignore unwanted values:

```python
name, _, age = ["Alice", "Developer", 25]
```

---

## 3. Dictionary Unpacking

By default, unpacking gives **keys**.

```python
user = {"name": "John", "age": 22}

k1, k2 = user
```

Values:

```python
name, age = user.values()
```

Keys and values:

```python
for key, value in user.items():
    print(key, value)
```

---

## 4. Merge Collections

### Lists

```python
a = [1, 2]
b = [3, 4]

c = [*a, *b]
```

### Dictionaries

```python
d1 = {"x": 1}
d2 = {"y": 2}

d3 = {**d1, **d2}
```

---

## 5. Function Argument Unpacking

### Using `*`

```python
def add(a, b):
    return a + b

nums = [5, 10]

add(*nums)
```

Equivalent to:

```python
add(5, 10)
```

---

### Using `**`

```python
def user(name, age):
    print(name, age)

data = {
    "name": "John",
    "age": 22
}

user(**data)
```

Equivalent to:

```python
user(name="John", age=22)
```

---

## Quick Summary

| Syntax | Meaning |
|--------|---------|
| `a, b = iterable` | Basic unpacking |
| `*rest` | Capture remaining items |
| `*list1` | Unpack list/tuple |
| `**dict1` | Unpack dictionary |
| `func(*args)` | Pass positional arguments |
| `func(**kwargs)` | Pass keyword arguments |
| `[*a, *b]` | Merge lists |
| `{**d1, **d2}` | Merge dictionaries |