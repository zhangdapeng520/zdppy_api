from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(..., title="The ID of the item to get"),
        q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z24_path_and_query:app", reload=True, host="0.0.0.0", port=8888)
