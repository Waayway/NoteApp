from typing import Optional
from fastapi import FastAPI
import uvicorn

from db import *


app = FastAPI()

openJsonFile()

@app.get("/")
async def read_root():
    return ""


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True, access_log=False)