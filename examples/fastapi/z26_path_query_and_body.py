from typing import Optional

from zdppy_api  import Api, Path
from pydantic import BaseModel

app = Api()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        q: Optional[str] = None,
        item: Optional[Item] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z26_path_query_and_body:app", reload=True, host="0.0.0.0", port=8888)
