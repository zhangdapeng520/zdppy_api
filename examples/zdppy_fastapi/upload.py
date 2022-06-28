from zdppy_api import Api

app = Api(init_routers=["health", "upload", "uploads"])  # 初始化的时候自动加上

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("upload:app", reload=True, host="0.0.0.0", port=8888)
