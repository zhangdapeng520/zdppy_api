from zdppy_api import Api
from zdppy_api import *

app = Api()


@app.get("/success", response_model=ResponseSuccess, summary="成功")
async def success():
    return ResponseSuccess()


@app.get("/success_data", response_model=ResponseSuccessData, summary="成功且携带数据")
async def success_data():
    return ResponseSuccessData(data={"username": "张大鹏", "age": 22})


@app.get("/success_list_data", response_model=ResponseSuccessListData, summary="成功且携带列表数据")
async def success_list_data():
    return ResponseSuccessListData(data=[{"username": "张大鹏", "age": 22} for _ in range(10)])


@app.get("/param_error", response_model=ResponseParamError, summary="参数错误")
async def param_error():
    return ResponseParamError()


@app.get("/server_error", response_model=ResponseServerError, summary="服务器内部错误")
async def server_error():
    return ResponseServerError()


@app.get("/not_found", response_model=ResponseNotFound, summary="资源不存在")
async def not_found():
    return ResponseNotFound()


@app.get("/grpc_can_not_use", response_model=ResponseGrpcCanNotUse, summary="grpc服务不可用")
async def grpc_can_not_use():
    return ResponseGrpcCanNotUse()


@app.get("/exists_error", response_model=ResponseExistsError, summary="数据已存在")
async def exists_error():
    return ResponseExistsError()


@app.get("/un_auth", response_model=ResponseUnAuth, summary="没有访问权限")
async def un_auth():
    return ResponseUnAuth()


@app.get("/token_expired", response_model=ResponseTokenExpired, summary="数据已过期")
async def token_expired():
    return ResponseTokenExpired()


@app.get("/timeout", response_model=ResponseTimeout, summary="服务连接超时")
async def timeout():
    return ResponseTimeout()


@app.get("/cors_error", response_model=ResponseCorsError, summary="跨域请求错误")
async def cors_error():
    return ResponseCorsError()


@app.get("/request_limit_error", response_model=ResponseRequestLimitError, summary="请求被限制")
async def request_limit_error():
    return ResponseRequestLimitError()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("z01_common_result:app", reload=True, host="0.0.0.0", port=8888)
