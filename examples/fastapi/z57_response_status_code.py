from zdppy_api.fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z57_response_status_code:app", reload=True, host="0.0.0.0", port=8888)
