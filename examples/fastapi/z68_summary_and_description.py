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


@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z68_summary_and_description:app", reload=True, host="0.0.0.0", port=8888)
