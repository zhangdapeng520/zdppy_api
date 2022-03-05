from enum import Enum

from fastapi import FastAPI

app = FastAPI()


class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]


@app.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z67_enum_tags:app", reload=True, host="0.0.0.0", port=8888)
