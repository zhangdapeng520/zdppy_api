from zdppy_api import Api

app = Api()

# 添加跨域中间件
app.add_middleware_cors()


@app.get("/")
async def main():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("cors:app", reload=True, host="0.0.0.0", port=8888)
