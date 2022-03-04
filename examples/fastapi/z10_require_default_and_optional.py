from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z10_require_default_and_optional:app", reload=True, host="0.0.0.0", port=8888)
