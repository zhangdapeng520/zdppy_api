from typing import Optional

from zdppy_api  import Body, Api
from pydantic import BaseModel

app = Api()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z30_embed_single_parameter:app", reload=True, host="0.0.0.0", port=8888)
