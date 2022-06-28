from typing import Optional

from zdppy_api  import Api, Query

app = Api()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z20_query_alias:app", reload=True, host="0.0.0.0", port=8888)