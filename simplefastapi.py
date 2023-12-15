from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List

app = FastAPI()


class TodoItem(BaseModel):
    id: Optional[int] = None
    title: str  # int
    description: Optional[str] = None
    completed: bool = False


db: Dict[int, TodoItem] = {}


@app.get("/todos", response_model=List[TodoItem])
async def read_todos():
    return list(db.values())


@app.post("/todos", response_model=int)
async def create_todo(todo: TodoItem) -> int:
    todo_id = len(db) + 1  # Auto increment id
    todo.id = todo_id
    db[todo_id] = todo
    return todo_id


@app.get("/todos/", response_model=List[TodoItem])
async def read_todos() -> List[TodoItem]:
    return list(db.values())


@app.get("/todos/{todo_id}", response_model=TodoItem)
async def read_todo(todo_id: int) -> TodoItem:
    todo = db.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: int, todo_update: TodoItem) -> TodoItem:
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="Todo not found")
    db[todo_id] = todo_update
    return db[todo_id]


@app.delete("/todos/{todo_id}", response_model=None)
async def delete_todo(todo_id: int):
    if todo_id not in db:
        raise HTTPException(status_code=404, detail="Todo not found")
    del db[todo_id]
    return None
