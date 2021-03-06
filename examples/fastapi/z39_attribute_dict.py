from typing import Dict

from zdppy_api  import Api

app = Api()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z39_attribute_dict:app", reload=True, host="0.0.0.0", port=8888)
