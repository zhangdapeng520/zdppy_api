from zdppy_api.fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z01_hello:app", reload=True, host="0.0.0.0", port=8888)
