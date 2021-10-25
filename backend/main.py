from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION,
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )

    create_tables()

    return app

# set 0.0.0.0 IP address to be accessible from outside


# app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION, host=settings.HOST, port=settings.PORT, reload=True)

app = start_application()

@app.get("/")
def hello_api():
    return {"detail": "Hello World!"}