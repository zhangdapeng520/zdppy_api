from typing import Optional
from zdppy_api.fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z14_query_validation:app", reload=True, host="0.0.0.0", port=8888)
