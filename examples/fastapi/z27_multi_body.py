from typing import Optional

from zdppy_api  import Api
from pydantic import BaseModel

app = Api()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z27_multi_body:app", reload=True, host="0.0.0.0", port=8888)
