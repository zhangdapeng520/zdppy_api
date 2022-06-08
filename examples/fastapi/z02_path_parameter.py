from zdppy_api.fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z02_path_parameter:app", reload=True, host="0.0.0.0", port=8888)
