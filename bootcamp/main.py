from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/{name}")
# async def get_name(name: str) -> dict:
#     return {"message": f"Hello {name}"}

@app.get("/greet/{name}")
async def greet(name: str,age: int) -> dict:
    return {"message": f"Hello {name} you're {age} years old"}

@app.get("/greet")
async def greet(name: Optional[str] = "User",age: int=0) -> dict:
    return {"message": f"Hello {name} you're {age} years old!", "age": age}


class BookCreateModel(BaseModel):
    title : str
    author : str

@app.post("/create_book")
async def create_book(book: BookCreateModel) -> dict:
    return {"title": book.title, "author": book.author}

@app.get("/get_headers", status_code=200)
async def get_headers(
    accept : str = Header(None),
    content_type : str = Header(None),
    user_agent : str = Header(None),
    host : str = Header(None)
):
    req_headers = {}

    req_headers["Accept"] = accept
    req_headers["Content-Type"] = content_type
    req_headers["User-Agent"] = user_agent
    req_headers["Host"] = host

    return req_headers

