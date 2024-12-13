from fastapi import APIRouter, HTTPException
from app.models import TodoItem

router = APIRouter()
todos = {}  # In-memory database

@router.post("/todos/", response_model=TodoItem)
def create_todo(todo: TodoItem):
    if todo.id in todos:
        raise HTTPException(status_code=400, detail="Todo already exists.")
    todos[todo.id] = todo
    return todo

@router.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int):
    todo = todos.get(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found.")
    return todo

@router.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, todo: TodoItem):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found.")
    todos[todo_id] = todo
    return todo

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found.")
    del todos[todo_id]
    return {"message": "Todo deleted"}
