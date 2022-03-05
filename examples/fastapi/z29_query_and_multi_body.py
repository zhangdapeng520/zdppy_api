from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(..., gt=0),
        q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z29_query_and_multi_body:app", reload=True, host="0.0.0.0", port=8888)
