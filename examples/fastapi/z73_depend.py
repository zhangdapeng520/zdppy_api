from typing import Optional

from zdppy_api import Depends, Api

app = Api()


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z73_depend:app", reload=True, host="0.0.0.0", port=8888)
