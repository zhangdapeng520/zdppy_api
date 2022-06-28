#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 19:43
# @Author  : 张大鹏
# @Github  : https://github.com/zhangdapeng520
# @File    : apirouter.py
# @Software: PyCharm
# @Description: 演示API Router的使用
from zdppy_api import response, Api, APIRouter

app = Api()
router = APIRouter()


@router.get("/")
def user():
    return response.string("user router")


@app.get("/")
def hello():
    return response.string("hello world")


app.include_router(
    router,
    prefix="/user",
    tags=["用户管理"]
)

if __name__ == '__main__':
    import uvicorn

    # http://localhost:8889/docs
    uvicorn.run("apirouter:app", reload=True, host="0.0.0.0", port=8889)
