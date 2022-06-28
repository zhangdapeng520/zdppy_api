from typing import Optional

from zdppy_api  import Api, Query

app = Api()


@app.get("/items/")
async def read_items(
        q: Optional[str] = Query(
            "fixedquery",
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            regex="^fixedquery$",
            deprecated=True,
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z21_deprecating:app", reload=True, host="0.0.0.0", port=8888)
