from fastapi import FastAPI
from fastapi.responses import JSONResponse
from patients_routes import patients_router as pr



app = FastAPI()


@app.get("/health")
def check_health():
    return JSONResponse(status_code=200 , content={
        "message": "API is running successfully"
    })




# register the routes
app.include_router(pr , prefix="/patients")