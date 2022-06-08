from typing import Optional

from zdppy_api.fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z06_optional_parameter:app", reload=True, host="0.0.0.0", port=8888)
