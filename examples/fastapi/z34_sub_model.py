from typing import Optional, Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    image: Optional[Image] = None  # 子模型


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z34_sub_model:app", reload=True, host="0.0.0.0", port=8888)
