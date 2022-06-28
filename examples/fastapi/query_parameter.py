from zdppy_api import Api

app = Api()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("query_parameter:app", reload=True, host="0.0.0.0", port=8888)
    print("测试地址：http://localhost:8888/items/?skip=1&limit=3")
