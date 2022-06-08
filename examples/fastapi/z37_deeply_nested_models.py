from typing import List, Optional, Set

from zdppy_api.fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z37_deeply_nested_models:app", reload=True, host="0.0.0.0", port=8888)
