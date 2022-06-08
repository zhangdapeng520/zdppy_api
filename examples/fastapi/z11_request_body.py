from typing import Optional

from zdppy_api.fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z11_request_body:app", reload=True, host="0.0.0.0", port=8888)
