from typing import Optional

from zdppy_api.fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z13_request_body_and_path_parameter:app", reload=True, host="0.0.0.0", port=8888)
