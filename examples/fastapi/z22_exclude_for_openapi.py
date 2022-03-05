from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
        hidden_query: Optional[str] = Query(None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z22_exclude_for_openapi:app", reload=True, host="0.0.0.0", port=8888)
