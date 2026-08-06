# Python Typing Notes for FastAPI (Complete Guide)

A practical guide to common (and nested) typing patterns used with FastAPI + Pydantic.  
**Rule:** always read nested types **from the inside out**.

```python
from typing import (
    Any, Optional, Union, Literal, Final, ClassVar,
    List, Dict, Tuple, Set, FrozenSet,
    TypedDict, NotRequired, Required,
    Callable, Iterable, Sequence, Mapping, MutableMapping,
    TypeVar, Generic, Annotated, TypeAlias,
)
from pydantic import BaseModel, Field
```

---

## 0. Why typing matters in FastAPI

| Place | What typing does |
|-------|------------------|
| Function params | Request validation (path/query/body) |
| `response_model` | Response validation + Swagger schema |
| Pydantic models | Field validation + docs |
| Return hints | Editor help + clearer code |

Without a proper type, FastAPI cannot enforce shape.

---

# PART A — Basic Types

## 1. Primitive types

| Type | Meaning | Example value |
|------|---------|---------------|
| `str` | text | `"anish"` |
| `int` | integer | `22` |
| `float` | decimal | `22.5` |
| `bool` | true/false | `True` |
| `bytes` | binary | `b"abc"` |
| `None` | null | `None` |

```python
def greet(name: str, age: int, score: float, active: bool) -> str:
    return f"{name}-{age}-{score}-{active}"
```

JSON mapping:

```json
{
  "name": "anish",
  "age": 22,
  "score": 88.5,
  "active": true
}
```

---

## 2. `Any`

Means: **any value is allowed** (turns off checking).

```python
from typing import Any

def dump(data: Any) -> Any:
    return data
```

Valid inputs: `1`, `"hi"`, `[1,2]`, `{"a": 1}`, `None`

Use sparingly. Prefer exact types.

---

## 3. `Optional[T]` and `Union`

### `Optional[T]` = `T | None`

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "anish"
    return None
```

### `Union[A, B]` = `A | B`

```python
from typing import Union

UserId = Union[int, str]   # or: int | str

def get_user(user_id: int | str) -> dict:
    return {"id": user_id}
```

### Complicated example

```python
Payload = dict[str, str | int | float | bool | None]

def normalize(value: str | int | list[str] | None) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ",".join(value)
    return str(value)
```

---

## 4. `Literal`

Only specific exact values allowed.

```python
from typing import Literal

Status = Literal["success", "error", "pending"]

def set_status(status: Status) -> Status:
    return status

set_status("success")   # ok
# set_status("ok")      # type error
```

FastAPI/Pydantic use:

```python
class Task(BaseModel):
    priority: Literal["low", "medium", "high"]
    status: Literal["todo", "doing", "done"]
```

---

## 5. `Final` and `ClassVar`

```python
from typing import Final, ClassVar

MAX_USERS: Final[int] = 100          # should not be reassigned

class Config:
    api_version: ClassVar[str] = "v1"  # class-level, not instance field
    name: str
```

---

# PART B — Collection Types

## 6. `List[T]` / `list[T]`

```text
List[int]  →  [1, 2, 3]
List[str]  →  ["a", "b"]
List[Employee] → [Employee, Employee]
```

```python
ages: list[int] = [20, 21, 22]
names: list[str] = ["a", "b"]
matrix: list[list[int]] = [[1, 2], [3, 4]]
```

### Complicated nested list

```python
# weekly timetable: day -> periods -> subject names
Timetable = list[list[str]]

timetable: Timetable = [
    ["Math", "Physics"],      # Monday
    ["English", "Chemistry"], # Tuesday
]
```

---

## 7. `Tuple`

### Fixed length

```python
point: tuple[int, int] = (10, 20)
person: tuple[str, int, bool] = ("anish", 22, True)
```

### Variable length (homogenous)

```python
scores: tuple[int, ...] = (10, 20, 30, 40)
```

### Complicated

```python
# (lat, lon, label)
Location = tuple[float, float, str]

# row of mixed SQL-like result
Row = tuple[int, str, float | None]
rows: list[Row] = [(1, "anish", 88.5), (2, "riya", None)]
```

---

## 8. `Set` / `FrozenSet`

```python
tags: set[str] = {"fastapi", "python"}
ids: frozenset[int] = frozenset({1, 2, 3})
```

JSON note: sets are not native JSON. Convert to list before returning from API.

```python
return {"tags": list(tags)}
```

---

## 9. `Dict[K, V]` / `dict[K, V]`  ★ most confusing

```text
Dict[str, int]
→ { "any_string_key": integer_value }
```

### Simple

```python
ages: dict[str, int] = {"anish": 22, "riya": 21}
```

### Values are lists

```python
Dict[str, list[int]]
→ { "math": [90, 80], "science": [70] }
```

### Values are dicts

```python
Dict[str, dict[str, int]]
→ {
    "anish": {"math": 90, "eng": 80},
    "riya":  {"math": 70, "eng": 88}
  }
```

### Values are models

```python
Dict[str, Employee]
→ {
    "e1": {"id": 1, "name": "A", "department": "IT", "age": 20},
    "e2": {"id": 2, "name": "B", "department": "HR", "age": 25}
  }
```

### Critical mistake

```python
# ❌ This does NOT mean status + data
response_model = Dict[str, Employee]

# Because it means EVERY value is Employee.
# So "status": "success" is invalid.
```

---

## 10. Nested Dict / List combinations (complicated)

### A) `Dict[str, List[Employee]]`

```text
{ "key": [Employee, Employee] }
```

```json
{
  "IT": [
    {"id": 1, "name": "A", "department": "IT", "age": 20}
  ],
  "HR": []
}
```

### B) `Dict[str, Dict[str, List[Employee]]]`

```text
{
  outer_key: {
    inner_key: [Employee, ...]
  }
}
```

```json
{
  "CS": {
    "active": [
      {"id": 1, "name": "Anish", "department": "CS", "age": 20}
    ],
    "inactive": []
  },
  "HR": {
    "active": [],
    "inactive": [
      {"id": 2, "name": "Riya", "department": "HR", "age": 25}
    ]
  }
}
```

### C) `List[Dict[str, Union[str, int]]]`

```json
[
  {"name": "anish", "age": 22},
  {"name": "riya", "age": 21}
]
```

### D) `Dict[str, List[Dict[str, Any]]]`

```json
{
  "page1": [{"id": 1, "ok": true}],
  "page2": [{"id": 2, "ok": false, "reason": "bad input"}]
}
```

### E) Very nested (API analytics style)

```python
# date -> endpoint -> status_code -> count
Analytics = dict[str, dict[str, dict[int, int]]]

analytics: Analytics = {
    "2026-08-05": {
        "/employees": {200: 120, 404: 3, 500: 1},
        "/login": {200: 80, 401: 12},
    }
}
```

### F) Graph-like nesting

```python
# user_id -> friend_id -> interaction stats
SocialGraph = dict[int, dict[int, dict[str, int]]]

graph: SocialGraph = {
    1: {
        2: {"messages": 10, "likes": 3},
        3: {"messages": 0, "likes": 1},
    }
}
```

---

# PART C — Structured Dict Alternatives

## 11. `TypedDict` (best for fixed keys in a dict)

Use when keys are known: `status`, `data`, `error`, etc.

```python
from typing import TypedDict, NotRequired

class Employee(BaseModel):
    id: int
    name: str
    department: str
    age: int

class EmployeeResponse(TypedDict):
    status: str
    data: Employee

class EmployeeListResponse(TypedDict):
    status: str
    data: list[Employee]

class ErrorResponse(TypedDict):
    status: Literal["error"]
    detail: str
    code: NotRequired[int]   # optional key
```

Valid:

```python
resp: EmployeeResponse = {
    "status": "success",
    "data": Employee(id=1, name="Anish", department="CS", age=20),
}
```

### Complicated TypedDict

```python
class Meta(TypedDict):
    page: int
    page_size: int
    total: int

class PaginatedEmployees(TypedDict):
    status: Literal["success"]
    meta: Meta
    data: list[Employee]
    warnings: NotRequired[list[str]]
```

```json
{
  "status": "success",
  "meta": {"page": 1, "page_size": 10, "total": 35},
  "data": [
    {"id": 1, "name": "Anish", "department": "CS", "age": 20}
  ],
  "warnings": ["cache miss"]
}
```

---

## 12. Pydantic `BaseModel` (best for FastAPI)

```python
class Employee(BaseModel):
    id: int
    name: str
    department: str
    age: int

class EmployeeResponse(BaseModel):
    status: str
    data: Employee

class EmployeeListResponse(BaseModel):
    status: str
    data: list[Employee]
```

### Complicated nested models

```python
class Address(BaseModel):
    city: str
    pincode: str

class Profile(BaseModel):
    bio: str | None = None
    address: Address

class User(BaseModel):
    id: int
    name: str
    tags: list[str] = []
    profile: Profile
    scores: dict[str, float]          # subject -> marks
    roles: list[Literal["admin", "user", "guest"]]

class UserBundle(BaseModel):
    status: Literal["success"]
    users: list[User]
    index: dict[int, User]            # id -> user
```

Example payload:

```json
{
  "status": "success",
  "users": [
    {
      "id": 1,
      "name": "Anish",
      "tags": ["fastapi", "ml"],
      "profile": {
        "bio": "learner",
        "address": {"city": "Pune", "pincode": "411001"}
      },
      "scores": {"math": 90.0, "english": 88.5},
      "roles": ["user"]
    }
  ],
  "index": {
    "1": {
      "id": 1,
      "name": "Anish",
      "tags": ["fastapi", "ml"],
      "profile": {
        "bio": "learner",
        "address": {"city": "Pune", "pincode": "411001"}
      },
      "scores": {"math": 90.0, "english": 88.5},
      "roles": ["user"]
    }
  }
}
```

---

# PART D — Advanced Typing

## 13. `Annotated` (metadata for FastAPI/Pydantic)

```python
from typing import Annotated
from fastapi import Query, Path, Body

@app.get("/items/{item_id}")
def read_item(
    item_id: Annotated[int, Path(ge=1)],
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
    return {"item_id": item_id, "q": q}
```

```python
from pydantic import Field

class Product(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=40)]
    price: Annotated[float, Field(gt=0)]
    qty: Annotated[int, Field(ge=1, le=1000)]
```

---

## 14. `Callable`

```python
from typing import Callable

# function that takes (int, int) and returns int
Adder = Callable[[int, int], int]

def run(op: Adder) -> int:
    return op(2, 3)

run(lambda a, b: a + b)
```

Complicated:

```python
Validator = Callable[[dict[str, Any]], tuple[bool, str | None]]

def validate_user(data: dict[str, Any]) -> tuple[bool, str | None]:
    if "name" not in data:
        return False, "name missing"
    return True, None
```

---

## 15. `Iterable`, `Sequence`, `Mapping`

```python
from typing import Iterable, Sequence, Mapping

def total(nums: Iterable[int]) -> int:
    return sum(nums)

def first(items: Sequence[str]) -> str:
    return items[0]

def get_age(ages: Mapping[str, int], name: str) -> int:
    return ages[name]
```

Differences:

| Type | Meaning |
|------|---------|
| `Iterable[T]` | can loop |
| `Sequence[T]` | ordered, indexable (`list`, `tuple`) |
| `Mapping[K,V]` | read-only dict-like |
| `MutableMapping[K,V]` | writable dict-like |

---

## 16. Generics (`TypeVar`, `Generic`)

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    status: Literal["success", "error"]
    data: T | None = None
    detail: str | None = None

# usages
UserResponse = ApiResponse[Employee]
UsersResponse = ApiResponse[list[Employee]]
StatsResponse = ApiResponse[dict[str, int]]
```

Examples:

```python
ApiResponse[Employee](
    status="success",
    data=Employee(id=1, name="A", department="IT", age=20),
)

ApiResponse[list[Employee]](
    status="success",
    data=[Employee(id=1, name="A", department="IT", age=20)],
)

ApiResponse[dict[str, int]](
    status="success",
    data={"total": 10, "active": 7},
)
```

---

## 17. Type aliases

```python
from typing import TypeAlias

JSONDict: TypeAlias = dict[str, Any]
EmployeeId: TypeAlias = int
Headers: TypeAlias = dict[str, str]
Matrix: TypeAlias = list[list[float]]
Tree: TypeAlias = dict[str, "Tree | int"]   # recursive-ish idea
```

Modern syntax:

```python
type JSONDict = dict[str, Any]
type Matrix = list[list[float]]
```

---

# PART E — FastAPI Practical Patterns

## 18. Request body / query / path typing

```python
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    department: str
    age: int

@app.get("/employees/{employee_id}")
def get_one(employee_id: Annotated[int, Path(ge=1)]):
    return {"id": employee_id}

@app.get("/search")
def search(
    q: Annotated[str, Query(min_length=1)],
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    departments: Annotated[list[str] | None, Query()] = None,
):
    return {"q": q, "limit": limit, "departments": departments}

@app.post("/employees")
def create(employee: Employee):   # body model
    return employee
```

---

## 19. Response model patterns

### Single object

```python
@app.get("/employee", response_model=Employee)
def one():
    return Employee(id=1, name="A", department="IT", age=20)
```

### List

```python
@app.get("/employees", response_model=list[Employee])
def many():
    return [...]
```

### Wrapper dict with fixed keys (recommended)

```python
class EmployeeResponse(BaseModel):
    status: str
    data: Employee

@app.post("/employees", response_model=EmployeeResponse)
def create(emp: Employee):
    return {"status": "success", "data": emp}
```

### Dynamic map

```python
@app.get("/by-dept", response_model=dict[str, list[Employee]])
def by_dept():
    return {
        "IT": [Employee(id=1, name="A", department="IT", age=20)],
        "HR": [],
    }
```

### Nested dynamic map

```python
@app.get("/grouped", response_model=dict[str, dict[str, list[Employee]]])
def grouped():
    return {
        "IT": {
            "active": [Employee(id=1, name="A", department="IT", age=20)],
            "inactive": [],
        }
    }
```

---

## 20. Decision table (print this in your brain)

| JSON shape | Type to use |
|------------|-------------|
| `"anish"` | `str` |
| `22` | `int` |
| `true` | `bool` |
| `null` or value | `T \| None` / `Optional[T]` |
| only `"success"`/`"error"` | `Literal["success", "error"]` |
| `[1,2,3]` | `list[int]` |
| `["a","b"]` | `list[str]` |
| `[{employee}, ...]` | `list[Employee]` |
| `{"a": 1, "b": 2}` | `dict[str, int]` |
| `{"IT": [Employee...]}` | `dict[str, list[Employee]]` |
| `{"IT": {"active": [Employee...]}}` | `dict[str, dict[str, list[Employee]]]` |
| `{"status":"success","data":Employee}` | `TypedDict` / `BaseModel` (**not** `dict[str, Employee]`) |
| mixed unknown JSON | `dict[str, Any]` (last resort) |

---

# PART F — Complicated End-to-End Examples

## Example 1: E-commerce order API

```python
class Money(BaseModel):
    amount: float
    currency: Literal["INR", "USD"]

class OrderItem(BaseModel):
    sku: str
    qty: Annotated[int, Field(ge=1)]
    price: Money

class Customer(BaseModel):
    id: int
    name: str
    tags: list[str] = []

class Order(BaseModel):
    id: int
    customer: Customer
    items: list[OrderItem]
    metadata: dict[str, str | int | bool]
    status: Literal["created", "paid", "shipped", "cancelled"]

class OrderResponse(BaseModel):
    status: Literal["success"]
    data: Order
    links: dict[str, str]
```

```json
{
  "status": "success",
  "data": {
    "id": 101,
    "customer": {"id": 1, "name": "Anish", "tags": ["vip"]},
    "items": [
      {
        "sku": "BOOK-1",
        "qty": 2,
        "price": {"amount": 499.0, "currency": "INR"}
      }
    ],
    "metadata": {"source": "web", "retry": 0, "gift": false},
    "status": "paid"
  },
  "links": {
    "self": "/orders/101",
    "invoice": "/orders/101/invoice"
  }
}
```

Types involved:

- `Literal[...]`
- nested `BaseModel`
- `list[OrderItem]`
- `dict[str, str | int | bool]`
- wrapper response model

---

## Example 2: ML prediction batch API

```python
FeatureValue = int | float | str | bool
Features = dict[str, FeatureValue]

class PredictRequest(BaseModel):
    model_name: str
    records: list[Features]
    options: dict[str, Any] | None = None

class Prediction(BaseModel):
    input: Features
    label: str
    confidence: float
    extras: dict[str, list[float]] | None = None

class PredictResponse(BaseModel):
    status: Literal["success"]
    model_name: str
    predictions: list[Prediction]
    metrics: dict[str, dict[str, float]]
```

```json
{
  "status": "success",
  "model_name": "churn-v2",
  "predictions": [
    {
      "input": {"age": 22, "plan": "pro", "active": true},
      "label": "stay",
      "confidence": 0.91,
      "extras": {"probs": [0.09, 0.91]}
    }
  ],
  "metrics": {
    "latency_ms": {"p50": 12.0, "p95": 30.0},
    "batch": {"size": 1.0}
  }
}
```

---

## Example 3: Deep nested org chart

```python
class EmployeeNode(BaseModel):
    id: int
    name: str
    reports: list["EmployeeNode"] = []

class DepartmentTree(BaseModel):
    name: str
    head: EmployeeNode
    teams: dict[str, list[EmployeeNode]]

class OrgResponse(BaseModel):
    status: str
    org: dict[str, DepartmentTree]
```

```json
{
  "status": "success",
  "org": {
    "Engineering": {
      "name": "Engineering",
      "head": {
        "id": 1,
        "name": "Anish",
        "reports": [
          {"id": 2, "name": "Riya", "reports": []}
        ]
      },
      "teams": {
        "backend": [
          {"id": 2, "name": "Riya", "reports": []}
        ],
        "ml": []
      }
    }
  }
}
```

Type chain:

```text
OrgResponse
 └─ dict[str, DepartmentTree]
     ├─ EmployeeNode
     │   └─ list[EmployeeNode]   (recursive)
     └─ dict[str, list[EmployeeNode]]
```

---

## Example 4: Where `Dict[str, Dict[str, List[Employee]]]` is correct

```python
# campus -> club -> members
CampusClubs = dict[str, dict[str, list[Employee]]]

data: CampusClubs = {
    "Pune": {
        "AI Club": [
            Employee(id=1, name="Anish", department="CS", age=20)
        ],
        "Robotics": [],
    },
    "Delhi": {
        "AI Club": [],
    },
}

@app.get("/campus-clubs", response_model=CampusClubs)
def campus_clubs():
    return data
```

This works because **every level is dynamic keys + same value type**.

---

## Example 5: Wrong vs right for your CRUD

Your return:

```python
return {"status": "success", "data": new_employee}
```

| response_model | Result |
|----------------|--------|
| `Dict[str, Employee]` | ❌ fails (`status` is str) |
| `Dict[str, Dict[str, List[Employee]]]` | ❌ fails (wrong nesting) |
| `Dict[str, Any]` | ⚠️ works, weak docs/validation |
| `TypedDict` / `BaseModel` with `status`+`data` | ✅ correct |

---

# PART G — Mini Drills

Write the type for each JSON:

**1.** `"pending"` where only 3 values allowed  
→ `Literal["pending", "success", "error"]`

**2.** `[1, 2, 3]`  
→ `list[int]`

**3.** `{"math": 90, "eng": 80}`  
→ `dict[str, int]`

**4.** `{"IT": [Employee, Employee]}`  
→ `dict[str, list[Employee]]`

**5.** `{"IT": {"junior": [Employee], "senior": [Employee]}}`  
→ `dict[str, dict[str, list[Employee]]]`

**6.** `{"status":"success","data":Employee}`  
→ `TypedDict` / `BaseModel` (fixed keys)

**7.** `[{"id":1,"ok":true},{"id":2,"ok":false}]`  
→ `list[dict[str, int | bool]]` or better a model

**8.** `null` or `"anish"`  
→ `str | None`

**9.** `(10.5, 72.8, "Pune")`  
→ `tuple[float, float, str]`

**10.** date → route → status → count  
→ `dict[str, dict[str, dict[int, int]]]`

---

# PART H — One-page cheat sheet

```text
T | None                     → optional value
Literal["a","b"]             → exact allowed values
list[T]                      → JSON array of T
tuple[A,B]                   → fixed pair
dict[str, T]                 → object, all values are T
dict[str, list[T]]           → object of arrays
dict[str, dict[str, list[T]]]→ object of objects of arrays
TypedDict / BaseModel        → object with FIXED keys
Callable[[A], B]             → function type
Annotated[T, ...]            → type + validation metadata
Generic[T]                   → reusable container types
Any                          → escape hatch (avoid)
```

### Golden rule

> Use `dict[str, ...]` for **dynamic keys**.  
> Use `TypedDict` / `BaseModel` for **fixed keys** like `status` and `data`.

---

*Keep this file open while practicing FastAPI CRUD and response models.*
