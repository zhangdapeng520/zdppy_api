from zdppy_api  import Depends, Api, Header, HTTPException

app = Api()


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z76_dependencies:app", reload=True, host="0.0.0.0", port=8888)
