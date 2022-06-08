from typing import List, Optional

from zdppy_api.fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z48_response_model:app", reload=True, host="0.0.0.0", port=8888)
