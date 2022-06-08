from zdppy_api.fastapi import FastAPI
from zdppy_api.fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z83_cors:app", reload=True, host="0.0.0.0", port=8888)
