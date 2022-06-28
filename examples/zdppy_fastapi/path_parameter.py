from zdppy_api import Api

app = Api()


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == '__main__':
    import uvicorn

    # http://localhost:8888/users/zhangdapeng
    uvicorn.run("path_parameter:app", reload=True, host="0.0.0.0", port=8888)
