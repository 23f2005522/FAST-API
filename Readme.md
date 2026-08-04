# FastAPI for Machine Learning — Learning Roadmap

A structured curriculum to learn FastAPI from fundamentals through ML serving, databases, auth, testing, performance, and deployment.

**Primary resources**

- [CampusX — FastAPI for Machine Learning (YouTube)](https://www.youtube.com/playlist?list=PLKnIA16_RmvY5eP91BQJua-eRJgjOumYW)
- Course syllabus modules (Introduction → Capstone)

---

## Learning Path Overview


| #   | Module                       | Focus                                |
| --- | ---------------------------- | ------------------------------------ |
| 0   | API Foundations              | What APIs are, HTTP basics           |
| 1   | Introduction to FastAPI      | Setup, first app, architecture       |
| 2   | Building APIs                | CRUD, validation, async              |
| 3   | Database Integration         | SQLAlchemy, project structure        |
| 4   | Machine Learning Integration | Serialize & serve models             |
| 5   | Advanced FastAPI             | Middleware, DI, JWT, API keys        |
| 6   | Testing & Debugging          | Unit/integration/E2E, logging        |
| 7   | Performance & Monitoring     | Redis, profiling, Prometheus/Grafana |
| 8   | Capstone Project             | End-to-end ML API + deploy           |


---



## 0. API Foundations *(CampusX)*


| #   | Topic                                           | Duration |
| --- | ----------------------------------------------- | -------- |
| 0.1 | What is an API? — Introduction to APIs          | 46:37    |
| 0.2 | FastAPI Philosophy — Setup, Installation & Demo | 42:07    |
| 0.3 | HTTP Methods in FastAPI                         | 27:01    |
| 0.4 | Path & Query Params in FastAPI                  | 41:12    |
| 0.5 | Pydantic Crash Course — Data Validation         | 1:25:31  |
| 0.6 | POST Request & Request Body                     | 35:42    |
| 0.7 | PUT & DELETE in FastAPI                         | 31:11    |


**Goals:** Understand REST, HTTP verbs, path/query params, and Pydantic validation before writing production APIs.

---



## 1. Introduction to FastAPI


| #   | Topic                                         | Duration |
| --- | --------------------------------------------- | -------- |
| 1.7 | API Authentication & Authorization *(bridge)* | 9:00     |
| 2.0 | Introduction to FastAPI                       | 1:00     |
| 2.1 | About FastAPI                                 | 4:00     |
| 2.2 | Key Features of FastAPI                       | 12:00    |
| 2.3 | Architecture of FastAPI                       | 15:00    |
| 2.4 | Installing FastAPI                            | 4:00     |
| 2.5 | First App using FastAPI                       | 11:00    |
| 2.6 | Comparative Analysis                          | 6:00     |


**Goals:** Install FastAPI + Uvicorn, run a Hello World app, and know why FastAPI fits ML services (async, OpenAPI, Pydantic).

**Checklist**

- [ ] Create a virtual environment and install `fastapi`, `uvicorn`
- [ ] Run a minimal `GET /` endpoint
- [ ] Open `/docs` (Swagger) and `/redoc`

---



## 2. Building APIs using FastAPI


| #   | Topic                           | Duration |
| --- | ------------------------------- | -------- |
| 3   | Building APIs using FastAPI     | 2:00     |
| 3.1 | Creating APIs                   | 21:00    |
| 3.2 | CRUD Operations                 | 39:00    |
| 3.3 | Handling Validations and Errors | 26:00    |
| 3.4 | Asynchronous Programming        | 28:00    |


**Goals:** Build full CRUD endpoints with validation, proper status codes, and async handlers.

**Checklist**

- [ ] Implement GET / POST / PUT / DELETE for a resource
- [ ] Add Pydantic request/response models
- [ ] Raise `HTTPException` for not-found / bad input
- [ ] Convert a blocking handler to `async def` where useful

---



## 3. Database Integration


| #     | Topic                            | Duration |
| ----- | -------------------------------- | -------- |
| 4     | Database Integration             | 1:00     |
| 4.1   | Database Basics                  | 9:00     |
| 4.2   | SQLAlchemy Basics                | 13:00    |
| 4.3   | CRUD App Project Structure       | 6:00     |
| 4.3.1 | `database.py` — engine & session | 11:00    |
| 4.3.2 | `models.py` — SQLAlchemy models  | 8:00     |
| 4.3.3 | `schemas.py` — Pydantic schemas  | 14:00    |
| 4.3.4 | `crud.py` — CRUD helpers         | 24:00    |
| 4.3.5 | `main.py` — routes & app wiring  | 39:00    |


**Suggested layout**

```text
app/
  database.py
  models.py
  schemas.py
  crud.py
  main.py
```

**Checklist**

- [ ] Configure SQLAlchemy engine + session dependency
- [ ] Define ORM models and matching Pydantic schemas
- [ ] Wire CRUD through FastAPI route handlers

---



## 4. Machine Learning Integration


| #    | Topic                                   | Duration |
| ---- | --------------------------------------- | -------- |
| 5    | Machine Learning Integration            | 1:00     |
| 5.1  | Model Serialization                     | 15:00    |
| 5.2  | Serialization with Pickle and Joblib    | 17:00    |
| 5.3  | Serialization with Keras                | 19:00    |
| 5.4  | Pickle vs Joblib                        | 6:00     |
| 5.5  | Input and Output Schemas (theory)       | 9:00     |
| 5.6  | Input and Output Schemas (`schemas.py`) | 13:00    |
| 5.7  | Serving ML Models (theory)              | 6:00     |
| 5.8  | Serving ML Models (`train.py`)          | 10:00    |
| 5.9  | Serving ML Models (`predict.py`)        | 12:00    |
| 5.10 | Serving ML Models (`main.py`)           | 12:00    |
| 5.11 | Handling Batch Predictions              | 19:00    |


**CampusX companion videos**


| Topic                          | Duration |
| ------------------------------ | -------- |
| Serving ML Models with FastAPI | 46:37    |
| Improving the FastAPI API      | 40:35    |


**Suggested layout**

```text
ml/
  train.py
  predict.py
  models/          # saved .pkl / .joblib / Keras artifacts
app/
  schemas.py
  main.py
```

**Checklist**

- [ ] Train and serialize a model (Joblib/Pickle/Keras)
- [ ] Define input/output Pydantic schemas
- [ ] Expose `/predict` (single) and `/predict/batch`
- [ ] Load the model once at startup (not per request)

---



## 5. Advanced FastAPI Concepts


| #     | Topic                     | Duration |
| ----- | ------------------------- | -------- |
| 6     | Advanced FastAPI Concepts | 1:00     |
| 6.1   | Middlewares               | 9:00     |
| 6.2   | Built-in Middlewares      | 16:00    |
| 6.3   | Custom Middlewares        | 19:00    |
| 6.4   | Dependency Injection      | 8:00     |
| 6.4.1 | Database Connections      | 7:00     |
| 6.4.2 | Configuration Management  | 10:00    |
| 6.4.3 | User Authentication       | 25:00    |
| 6.5   | JWT Authentication        | 6:00     |
| 6.5.1 | `auth.py`                 | 15:00    |
| 6.5.2 | `models.py`               | 5:00     |
| 6.5.3 | `utils.py`                | 9:00     |
| 6.5.4 | `main.py`                 | 16:00    |
| 6.5.5 | Workflow                  | 9:00     |
| 6.6   | Managing API Keys         | 5:00     |
| 6.6.1 | API Keys with Headers     | 10:00    |
| 6.6.2 | API Keys with `.env` file | 11:00    |
| 6.7   | Best Practices            | 6:00     |


**Checklist**

- [ ] Add CORS / custom middleware (e.g. timing, request ID)
- [ ] Use `Depends()` for DB session and config
- [ ] Implement JWT login + protected routes
- [ ] Protect an endpoint with an API key from `.env`

---



## 6. Testing and Debugging


| #     | Topic                      | Duration |
| ----- | -------------------------- | -------- |
| 7     | Testing and Debugging      | 1:00     |
| 7.1   | Importance of Testing APIs | 6:00     |
| 7.2   | Types of Tests             | 1:00     |
| 7.2.1 | Unit Tests (theory)        | 2:00     |
| 7.2.2 | Unit Tests (code)          | 19:00    |
| 7.2.3 | Integration Testing        | 24:00    |
| 7.2.4 | End-to-End Testing         | 24:00    |
| 7.3   | Mock ML Models             | 9:00     |
| 7.3.1 | Mock ML Demo               | 43:00    |
| 7.4   | Common API Errors          | 14:00    |
| 7.5   | Debugging Techniques       | 1:00     |
| 7.5.1 | Logging                    | 18:00    |
| 7.5.2 | Exception Handling         | 9:00     |
| 7.5.3 | CURL & Configurations      | 6:00     |
| 7.5.4 | Summary                    | 4:00     |


**Checklist**

- [ ] Write unit tests with `TestClient` / `httpx.AsyncClient`
- [ ] Add an integration test against a test DB
- [ ] Mock the ML model in prediction tests
- [ ] Configure structured logging and exception handlers

---



## 7. Performance Optimization and Monitoring



### Caching


| #     | Topic                          | Duration |
| ----- | ------------------------------ | -------- |
| 8.1   | Caching & its Importance       | 8:00     |
| 8.1.1 | Caching Use Cases              | 4:00     |
| 8.1.2 | Types of Caching               | 11:00    |
| 8.1.3 | Key Considerations for Caching | 5:00     |
| 8.1.4 | Common Tools for Caching       | 2:00     |
| 8.2   | Caching with Redis             | 7:00     |
| 8.2.1 | Redis Data Structures          | 4:00     |
| 8.2.2 | Redis Use Cases                | 3:00     |
| 8.2.3 | Redis Setup                    | 16:00    |
| 8.3   | Redis with FastAPI             | 1:00     |
| 8.3.1 | Caching ML Predictions         | 25:00    |
| 8.3.2 | Caching DB Queries             | 29:00    |
| 8.3.3 | Caching External API Call      | 23:00    |




### Profiling & Benchmarking


| #     | Topic                          | Duration |
| ----- | ------------------------------ | -------- |
| 8.4   | Profiling FastAPI Apps         | 9:00     |
| 8.4.1 | Profiling with `time`          | 15:00    |
| 8.4.2 | Profiling with `cProfile`      | 24:00    |
| 8.4.3 | Profiling with `line-profiler` | 21:00    |
| 8.5   | Benchmarking APIs              | 2:00     |
| 8.5.1 | Advantages of Benchmarking     | 6:00     |
| 8.5.2 | Metrics for Benchmarking       | 9:00     |
| 8.5.3 | Tools for Benchmarking         | 5:00     |
| 8.5.4 | Locust Demo                    | 23:00    |
| 8.5.5 | Benchmarking Best Practices    | 4:00     |




### Monitoring


| #     | Topic                                   | Duration |
| ----- | --------------------------------------- | -------- |
| 8.6   | Monitoring APIs                         | 8:00     |
| 8.6.1 | Prometheus                              | 10:00    |
| 8.6.2 | Prometheus with FastAPI                 | 17:00    |
| 8.6.3 | FastAPI + Prometheus + Docker           | 35:00    |
| 8.6.4 | Grafana                                 | 14:00    |
| 8.6.5 | FastAPI + Grafana + Prometheus + Docker | 28:00    |


**Checklist**

- [ ] Cache prediction results in Redis
- [ ] Profile a slow endpoint and fix the hotspot
- [ ] Run a Locust load test
- [ ] Expose Prometheus metrics and a Grafana dashboard

---



## 8. Docker & Deployment *(CampusX)*


| #   | Topic                                      | Duration |
| --- | ------------------------------------------ | -------- |
| D.1 | Docker for Machine Learning — Crash Course | 1:26:45  |
| D.2 | FastAPI + Docker — Dockerize an API        | 19:22    |
| D.3 | Deploy a FastAPI API on AWS                | 18:58    |


**Checklist**

- [ ] Write a `Dockerfile` for the FastAPI app
- [ ] Run the API in a container locally
- [ ] Deploy to AWS (or Render — see Capstone)

---



## 9. Capstone Project


| #     | Topic                                      | Duration |
| ----- | ------------------------------------------ | -------- |
| 9.1   | Project File Structure                     | 18:00    |
| 9.2   | Project Setup with GitHub                  | 15:00    |
| 9.3   | Configurations and Security                | 25:00    |
| 9.4   | Auth & Dependencies                        | 24:00    |
| 9.5.1 | ML Integration with Caching — Part 1       | 37:00    |
| 9.5.2 | ML Integration with Caching — Part 2       | 16:00    |
| 9.5.3 | ML Integration with Caching — Part 3       | 19:00    |
| 9.6   | Middlewares and API                        | 16:00    |
| 9.7   | Monitoring & Containerization              | 9:00     |
| 9.8   | Running the Project Locally                | 17:00    |
| 9.9   | Project Deployment over Render using Redis | 16:00    |
| 9.10  | Important Note for Deployment              | 4:00     |


**Capstone deliverables**

- [ ] Clean project structure + GitHub repo
- [ ] Secure config (env vars, secrets)
- [ ] Auth (JWT / dependencies)
- [ ] ML predict endpoints with Redis caching
- [ ] Middleware + monitoring stack
- [ ] Dockerized app running locally
- [ ] Deployed on Render with Redis

---



## Suggested Weekly Plan


| Week | Modules | Outcome                                     |
| ---- | ------- | ------------------------------------------- |
| 1    | 0–1     | First FastAPI app + HTTP/Pydantic basics    |
| 2    | 2–3     | CRUD API backed by SQLAlchemy               |
| 3    | 4       | Serve a trained ML model via `/predict`     |
| 4    | 5       | JWT, API keys, middleware, DI               |
| 5    | 6       | Test suite + logging/debugging              |
| 6    | 7       | Redis caching + profiling + Locust          |
| 7    | 7–8     | Prometheus/Grafana + Docker                 |
| 8    | 9       | Capstone built, cached, monitored, deployed |


---



## Quick Start (local)

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install fastapi uvicorn[standard] pydantic sqlalchemy
uvicorn main:app --reload
```

Open interactive docs at `http://127.0.0.1:8000/docs`.

---



## Core Stack


| Layer         | Tools                                |
| ------------- | ------------------------------------ |
| API           | FastAPI, Uvicorn, Pydantic           |
| Data          | SQLAlchemy, PostgreSQL/SQLite        |
| ML            | scikit-learn / Keras, Joblib, Pickle |
| Cache         | Redis                                |
| Auth          | JWT, API keys, `.env`                |
| Test          | pytest, TestClient, mocks            |
| Observability | Prometheus, Grafana, Locust          |
| Deploy        | Docker, AWS, Render                  |


---



## Progress Tracker

Copy and check off as you go:

- [ ] Module 0 — API Foundations
- [ ] Module 1 — Introduction to FastAPI
- [ ] Module 2 — Building APIs
- [ ] Module 3 — Database Integration
- [ ] Module 4 — ML Integration
- [ ] Module 5 — Advanced Concepts
- [ ] Module 6 — Testing & Debugging
- [ ] Module 7 — Performance & Monitoring
- [ ] Module 8 — Docker & Deployment
- [ ] Module 9 — Capstone Project

---

*Curriculum compiled from CampusX “FastAPI for Machine Learning” and the corresponding course syllabus modules.*