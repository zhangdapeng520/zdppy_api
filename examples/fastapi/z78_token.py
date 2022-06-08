from zdppy_api.fastapi import Depends, FastAPI
from zdppy_api.fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z78_token:app", reload=True, host="0.0.0.0", port=8888)
