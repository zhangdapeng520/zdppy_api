from typing import Optional

from zdppy_api.fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return {"ads_id": ads_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z46_cookie:app", reload=True, host="0.0.0.0", port=8888)
