from datetime import datetime
from typing import Optional, List, Dict

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None


app = FastAPI()


@app.put("/items/{id}", response_model=Dict[str, Item])
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z71_json_able_encoder:app", reload=True, host="0.0.0.0", port=8888)
