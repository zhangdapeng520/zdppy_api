from zdppy_api.fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z58_form_data:app", reload=True, host="0.0.0.0", port=8888)
