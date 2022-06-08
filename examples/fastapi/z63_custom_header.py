from zdppy_api.fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z63_custom_header:app", reload=True, host="0.0.0.0", port=8888)
