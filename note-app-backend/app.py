from typing import Optional
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
import uvicorn

from db import *

cookie = "64jxYlcsbcjfjvev9JSUa7BJbn+GMsUgp7dOzf1IKhs"

app = FastAPI()

openJsonFile()

def checkCookie(request: Request):
    print(request.cookies)
    return request.cookies.__contains__(cookie)

# Root URL
@app.get("/")
async def read_root(request: Request):
    if checkCookie(request):
        pass
    else:
        return
    return "Cookie Works"


@app.get("/cookie/{key}/{value}")
async def create_cookie(key: str,value: str):
    response = JSONResponse(content={})
    response.set_cookie(key=key, value=value)
    return response

# GET urls
@app.get("/objective")
async def get_objectives(request: Request):
    if checkCookie(request):
        print(getData("objectives"))
        return getData("objectives")
    else:
        return
@app.get('/objective/{num}')
async def get_objective(num: int, request: Request):
    if checkCookie(request):
        print(getData("objectives"))
        return getData("objectives")
    else:
        return
# POST urls



if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, reload=True, access_log=False)