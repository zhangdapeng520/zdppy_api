from zdppy_api  import Api, File, UploadFile

app = Api()


@app.post("/files/")
async def create_file(file: bytes = File(..., description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
        file: UploadFile = File(..., description="A file read as UploadFile")
):
    return {"filename": file.filename}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z59_upload_file:app", reload=True, host="0.0.0.0", port=8888)
