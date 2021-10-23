from fastapi import FastAPI
from config import settings

# set 0.0.0.0 IP address to be accessible from outside


app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION, host=settings.HOST, port=settings.PORT, reload=True)


@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}