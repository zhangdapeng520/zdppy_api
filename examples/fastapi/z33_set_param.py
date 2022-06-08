from typing import Optional, Set

from zdppy_api.fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z33_set_param:app", reload=True, host="0.0.0.0", port=8888)
