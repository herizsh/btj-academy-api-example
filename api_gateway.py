from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

JSON_PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/todos"


@app.get("/todos/")
async def read_todos():
    async with httpx.AsyncClient() as client:
        response = await client.get(JSON_PLACEHOLDER_URL + "/1")
    return response.json()


@app.get("/todos/{todo_id}")
async def read_todo(todo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{JSON_PLACEHOLDER_URL}/{todo_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Todo not found")
    return response.json()


@app.post("/todos/")
async def create_todo(todo: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(JSON_PLACEHOLDER_URL, json=todo)
    return response.json()


@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: dict):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{JSON_PLACEHOLDER_URL}/{todo_id}", json=todo)
    return response.json()


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{JSON_PLACEHOLDER_URL}/{todo_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
