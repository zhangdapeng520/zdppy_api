from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    """
    使用三个点...表示这个参数为必填参数，同时不影响这个参数的校验
    :param q:
    :return:
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z17_required_value:app", reload=True, host="0.0.0.0", port=8888)
