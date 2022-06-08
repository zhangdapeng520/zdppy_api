from typing import Optional

from zdppy_api.fastapi import Depends, FastAPI
from zdppy_api.fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="zhangdapeng@example.com", full_name="zhangdapeng"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


if __name__ == '__main__':
    from zdppy_api import uvicorn

    uvicorn.run("z79_current_user:app", reload=True, host="0.0.0.0", port=8888)
