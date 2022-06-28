from typing import Optional

from zdppy_api  import Cookie, Depends, Api

app = Api()


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
        q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z75_sub_depends:app", reload=True, host="0.0.0.0", port=8888)
