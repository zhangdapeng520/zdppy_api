from zdppy_api  import Depends, Api
from zdppy_api.security import OAuth2PasswordBearer

app = Api()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z78_token:app", reload=True, host="0.0.0.0", port=8888)
