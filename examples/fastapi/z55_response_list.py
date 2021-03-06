from typing import List

from zdppy_api  import Api
from pydantic import BaseModel

app = Api()


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/items/", response_model=List[Item])
async def read_items():
    return items


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z55_response_list:app", reload=True, host="0.0.0.0", port=8888)
