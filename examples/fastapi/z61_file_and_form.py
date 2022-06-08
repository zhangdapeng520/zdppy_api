from zdppy_api.fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
        file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z61_file_and_form:app", reload=True, host="0.0.0.0", port=8888)
