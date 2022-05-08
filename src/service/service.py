from src.service import dto
from src.utils.log import defaultLogger
import src.biz.biz as order_biz
import src.data.data as order_data
import src.service.convert as order_convertor

# 实例化 Biz 和 Repo
order_repo = order_data.OrderRepo()
order_biz = order_biz.OrderBiz(order_repo=order_repo)


def with_log(func):
    def wrapper(*args, **kwargs):
        defaultLogger.info("func.in: %s. Request is %s, %s" % (func.__name__, str(args), str(kwargs)))
        res = func(*args, **kwargs)
        defaultLogger.info("func.out: %s. Response is %s" % (func.__name__, str(res)))
        return res

    return wrapper


def validate_and_fill(func):
    def wrapper(*args, **kwargs):
        # 第一个参数必为请求体 Request
        req = args[0]
        validate_err = req.validate_self()
        if validate_err is not None:
            return dto.Response(code=validate_err.code, message=validate_err.message, request_id=req.request_id)
        req.fill_self()
        return func(*args, **kwargs)
    return wrapper


@validate_and_fill
@with_log
def describe_order(req: dto.OrderDescribeRequest) -> dto.Response:
    # 执行biz层的具体的逻辑
    order_entity = order_biz.describe_order(req.data.order_id)

    # 将 order_entity 转换为 dto
    resp = order_convertor.convert_order_to_order_describe_response(order_entity)
    resp.request_id = req.request_id
    return resp


# @validate_and_fill
# @with_log
# def 执行具体逻辑的函数():
#     pass
