from typing import List, Optional, Set

from zdppy_api  import Api
from pydantic import BaseModel, HttpUrl

app = Api()


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


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z36_list_of_submodels:app", reload=True, host="0.0.0.0", port=8888)
