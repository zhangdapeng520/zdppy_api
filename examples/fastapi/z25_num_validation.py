from zdppy_api.fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: str,
        size: float = Query(..., gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q, "size": size})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z25_num_validation:app", reload=True, host="0.0.0.0", port=8888)
