from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z09_required_parameter:app", reload=True, host="0.0.0.0", port=8888)
