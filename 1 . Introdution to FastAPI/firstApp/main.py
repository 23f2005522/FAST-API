from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/" , status_code=status.HTTP_200_OK)
def home():
    """
    Return a welcome message.

    - **Returns**:
        - **message**: A welcome message.
        - **status**: A status message.
    """
    return {
        "message": "Hello World",
        "status": "success",
    } 


@app.get("/index")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


## Notes  :

#- status_code is used to set the status code of the response.
#- request is used to get the request object.
#- templates is used to render the template.
#- Jinja2Templates is used to render the template.
#- FastAPI is used to create the API.
#- Request is used to get the request object.
#- status is used to set the status code of the response.
#- templates is used to render the template.
#- Jinja2Templates is used to render the template.
#- FastAPI is used to create the API.
#- Request is used to get the request object.