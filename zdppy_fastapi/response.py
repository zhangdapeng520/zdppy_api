from typing import Dict, List

from pydantic import BaseModel


class ResponseSuccess(BaseModel):
    """
    成功的响应，包括创建成功，修改成功，删除成功等
    """
    status: bool = True  # 状态
    msg: str = "成功"  # 信息
    code: int = 10000  # 状态码：不采用常见HTTP状态码的原因，是为了避免容易被猜测


class ResponseSuccessData(ResponseSuccess):
    """
    成功的响应，同时携带数据返回，该数据是字典类型
    """
    data: Dict = None


class ResponseSuccessListData(ResponseSuccess):
    """
    成功的响应，同时携带数据返回，该数据是列表嵌套字典类型
    """
    data: List[Dict] = None


class ResponseParamError(BaseModel):
    """
    参数错误
    """
    status: bool = False  # 状态
    msg: str = "参数错误"  # 信息
    code: int = 10001  # 状态码


class ResponseServerError(BaseModel):
    """
    服务器内部错误
    """
    status: bool = False  # 状态
    msg: str = "服务器内部错误"  # 信息
    code: int = 10002  # 状态码


class ResponseNotFound(BaseModel):
    """
    资源不存在
    """
    status: bool = False  # 状态
    msg: str = "资源不存在"  # 信息
    code: int = 10003  # 状态码


class ResponseGrpcCanNotUse(BaseModel):
    """
    gRPC服务不可用
    """
    status: bool = False  # 状态
    msg: str = "gRPC服务不可用"  # 信息
    code: int = 10004  # 状态码


class ResponseExistsError(BaseModel):
    """
    数据已存在
    """
    status: bool = False  # 状态
    msg: str = "数据已存在"  # 信息
    code: int = 10005  # 状态码


class ResponseUnAuth(BaseModel):
    """
    没有访问权限
    """
    status: bool = False  # 状态
    msg: str = "没有访问权限"  # 信息
    code: int = 10006  # 状态码


class ResponseTokenExpired(BaseModel):
    """
    token已过期
    """
    status: bool = False  # 状态
    msg: str = "token已过期"  # 信息
    code: int = 10007  # 状态码


class ResponseTimeout(BaseModel):
    """
    服务连接超时
    """
    status: bool = False  # 状态
    msg: str = "服务连接超时"  # 信息
    code: int = 10008  # 状态码


class ResponseCorsError(BaseModel):
    """
    跨域请求失败
    """
    status: bool = False  # 状态
    msg: str = "跨域请求失败"  # 信息
    code: int = 10009  # 状态码


class ResponseRequestLimitError(BaseModel):
    """
    请求被限制
    """
    status: bool = False  # 状态
    msg: str = "请求频率过快"  # 信息
    code: int = 10010  # 状态码
