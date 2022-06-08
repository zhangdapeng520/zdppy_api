from zdppy_api.fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z62_error_404:app", reload=True, host="0.0.0.0", port=8888)
