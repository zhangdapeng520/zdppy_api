import time

from zdppy_api import Request, Api

app = Api()


@app.get("/")
async def hello():
    time.sleep(3)
    return "hello world!!!"


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print("中间件计算的时间：", process_time)
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("middleware:app", reload=True, host="0.0.0.0", port=8888)
