from typing import Optional

from zdppy_api.fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z08_path_and_query_parameter:app", reload=True, host="0.0.0.0", port=8888)
