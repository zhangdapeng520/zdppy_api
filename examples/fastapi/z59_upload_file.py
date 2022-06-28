from zdppy_api import Api, File, UploadFile, ResponseResult

app = Api(init_routers=["health", "upload"])  # 初始化的时候自动加上


@app.post("/upload1")
async def upload(file: UploadFile):
    content = await file.read()
    data = {
        "filename": file.filename,
        "content-type": file.content_type,
        "size": len(content)
    }
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(content)
    await file.close()
    return ResponseResult(data=data)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z59_upload_file:app", reload=True, host="0.0.0.0", port=8888)
