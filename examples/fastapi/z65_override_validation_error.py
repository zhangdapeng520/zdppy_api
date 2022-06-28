from zdppy_api import Api, HTTPException
from zdppy_api.exceptions import RequestValidationError
from zdppy_api.responses import PlainTextResponse
from zdppy_api.starlette.exceptions import HTTPException as StarletteHTTPException

app = Api()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z65_override_validation_error:app", reload=True, host="0.0.0.0", port=8888)
