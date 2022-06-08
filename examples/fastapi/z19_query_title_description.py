from typing import Optional

from zdppy_api.fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
        q: Optional[str] = Query(
            None,
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z19_query_title_description:app", reload=True, host="0.0.0.0", port=8888)
