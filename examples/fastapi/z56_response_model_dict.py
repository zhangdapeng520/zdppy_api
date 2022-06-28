from typing import Dict

from zdppy_api  import Api

app = Api()


@app.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z56_response_model_dict:app", reload=True, host="0.0.0.0", port=8888)
   