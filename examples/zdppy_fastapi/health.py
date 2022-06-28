from zdppy_api import Api, ResponseResult

app = Api(init_routers=["health"])  # 自动添加健康检查接口


# 主动添加健康检查接口
@app.get("/health1")
async def health():
    return ResponseResult()


if __name__ == '__main__':
    import uvicorn

    # http://localhost:8888/health
    # http://localhost:8888/health1
    uvicorn.run("health:app", reload=True, host="0.0.0.0", port=8888)
