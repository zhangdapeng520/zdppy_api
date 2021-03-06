from typing import List

from zdppy_api  import Api, Query

app = Api()


@app.get("/items/")
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z18_query_list:app", reload=True, host="0.0.0.0", port=8888)
