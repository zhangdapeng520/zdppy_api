from typing import Union

from zdppy_api  import Api
from pydantic import BaseModel

app = Api()


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z54_union:app", reload=True, host="0.0.0.0", port=8888)
