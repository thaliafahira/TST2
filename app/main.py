from fastapi import FastAPI, Depends
from typing import Optional, List
from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from router import secure, public
from auth import get_user

app = FastAPI(
    title="digital wedding invitation",
    description="Wedding invitation",
    version="1.0",
    contact={
        "name": "Thalia",
        "email": "thaliafahira@gmail.com"
    }
)

app.include_router(
    public.router,
    prefix="/api/v1/public"
)

app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)

@app.get("/")
def read_root():
    return {
        "message": "Hello World",
        "project": "Wedding API",
        "version": "1.0",
        "developer": "thaliafahira",
        "description": "Wedding invitation",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }