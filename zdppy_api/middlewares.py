import time
from zdppy_api import Api, Request

app = Api()


@app.get("/")
async def hello():
    return "hello world!"


# 添加中间件
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    统计请求的时间
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print("本次请求共用时间：", process_time)
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("middleware:app", reload=True, host="0.0.0.0", port=8888)
