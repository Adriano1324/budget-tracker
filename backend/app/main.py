"""
This is main module resposnible for creating our app
"""

import logging

from fastapi import FastAPI

from app.api.v1.api import api_router_v1
from app.core.config import settings

logging.getLogger("passlib").setLevel(logging.ERROR)

app = FastAPI(docs_url=None, redoc_url=None)

app_v1 = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")
app_v1.include_router(api_router_v1)
app.mount(settings.API_V1_STR, app_v1)
