from typing import Optional

from zdppy_api.fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z47_header_parameter:app", reload=True, host="0.0.0.0", port=8888)
