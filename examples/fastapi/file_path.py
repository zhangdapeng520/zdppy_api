from zdppy_api import Api

app = Api()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("file_path:app", reload=True, host="0.0.0.0", port=8888)
    print("测试地址：http://localhost:8888/files/a/b/c/d/eee.txt")
