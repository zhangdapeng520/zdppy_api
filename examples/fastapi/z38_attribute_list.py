from typing import List

from zdppy_api.fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z38_attribute_list:app", reload=True, host="0.0.0.0", port=8888)