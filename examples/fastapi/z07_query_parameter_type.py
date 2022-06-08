from zdppy_api.fastapi import FastAPI

app = FastAPI()


@app.get("/users/{id}", summary="获取用户信息")
async def read_user(id: int, name: str | None = None, status: bool = False):
    """
    获取用户
    - id: 用户ID
    - name: 用户姓名
    - status: 账户状态

    返回: 用户信息
    """
    user = {
        "id": id,
        "status": status,
    }
    if name:
        user.update({"name": name})  # 字典更新
    if not status:
        user.update(
            {"description": "账户已激活"}
        )
    return user


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z07_query_parameter_type:app", reload=True, host="0.0.0.0", port=8888)
