from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

api = FastAPI()

class Todo(BaseModel):
    title: str
    description: str
    done: bool = False  # Default value

all_todos = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "done": False
    },
    {
        "id": 2,
        "title": "Supply groceries",
        "description": "Milk, eggs, bread",
        "done": False
    },
    {
        "id": 3,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "done": False
    },
    {
        "id": 4,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "done": False
    }
]

@api.get("/")
def root():
    return {"message": "Hello World"}

@api.get("/todos/{todo_id}") #path parameters
def get_todo(todo_id: int): 
    for todo in all_todos:
        if todo["id"] == todo_id:
            return todo

# localhost:8000/todos?first_n=2
@api.get("/todos") # with query parameters
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos

@api.post("/todos")
def create_todo(todo: Todo):
    new_todo_id = max(todo["id"] for todo in all_todos) + 1
    new_todo = {
        "id": new_todo_id,
        "title": todo.title,
        "description": todo.description,
        "done": todo.done
    }
    all_todos.append(new_todo)
    return new_todo


@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for existing_todo in all_todos:
        if existing_todo["id"] == todo_id:
            existing_todo["title"] = todo.title  
            existing_todo["description"] = todo.description  
            existing_todo["done"] = todo.done  
            return existing_todo
    return {"error": "Not Found"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo["id"] == todo_id:
            deleted_todo = all_todos.pop(index)
            return {"message": "Todo deleted successfully", "todo": deleted_todo}
    # Return a proper 404 error
    raise HTTPException(status_code=404, detail="Todo not found")