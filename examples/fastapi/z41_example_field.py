from typing import Optional

from zdppy_api  import Api
from pydantic import BaseModel, Field

app = Api()


class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z41_example_field:app", reload=True, host="0.0.0.0", port=8888)
