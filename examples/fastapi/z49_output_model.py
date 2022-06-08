from typing import Optional

from zdppy_api.fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z49_output_model:app", reload=True, host="0.0.0.0", port=8888)
