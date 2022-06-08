from typing import Optional

from zdppy_api.fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    """
    多个路径参数和查询参数的示例
    - user_id：用户ID
    - item_id：项目ID
    - q: 查询参数
    - short: 其他参数

    返回: 项目信息
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z08_path_and_query_parameter:app", reload=True, host="0.0.0.0", port=8888)
