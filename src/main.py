from fastapi import FastAPI
from config import settings
import uvicorn
import service

app = FastAPI()


# 智能语音交互订单查询
@app.post("/znyy/order/describe", response_model=service.OrderDescribeResponse)
async def znyy_describe_order(req: service.OrderDescribeRequest) -> service.Response:
    return service.describe_order(req)


# @app.post("/xxxxxxx", response_model=响应的结构体)
# async def 定义的函数名(req: 请求的结构体) -> 响应的结构体:
#     return service.执行具体逻辑的函数(req)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
