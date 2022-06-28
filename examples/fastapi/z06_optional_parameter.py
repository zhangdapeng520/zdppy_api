from zdppy_api  import Api

app = Api()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    """
    q: str | None = None
    q是可选参数，字符串类型或者None，默认是None
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z06_optional_parameter:app", reload=True, host="0.0.0.0", port=8888)
