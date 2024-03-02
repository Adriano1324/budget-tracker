"""
This is main module resposnible for creating our app
"""
import logging

from fastapi import FastAPI

from app.core.config import settings

logging.getLogger("passlib").setLevel(logging.ERROR)

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
def hello():
    return {"projectName": settings.PROJECT_NAME}
