from zdppy_api.fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z04_file_path:app", reload=True, host="0.0.0.0", port=8888)
