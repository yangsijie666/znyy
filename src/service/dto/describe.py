from pydantic import BaseModel
from src.service.dto.common import *
from src.utils.error import *


# 后期增加新的请求体和响应体
# 1. 创建对应的 XXRequestData 结构体，填充需要的业务属性
# 2. 创建对应的 XXRequest 对象，并继承 Request
# 3. 将 XXRequestData 作为 XXRequest 的一个属性
# 响应体 同理（继承 Response）


# 智能语音交互订单查询请求
class OrderDescribeRequestData(BaseModel):
    order_id: Optional[int] = None


class OrderDescribeRequest(Request):
    data: Optional[OrderDescribeRequestData] = None

    def validate_self(self) -> Error:
        if self.data is None or self.data.order_id is None:
            return params_missing("order_id")

    def fill_self(self):
        # xxxx
        pass


# 智能语音交互订单查询响应
class OrderDescribeResponseData(BaseModel):
    id: int
    user_id: str
    order_ext_id: str
    merged_product_type: str
    product_type: str
    create_time: str


class OrderDescribeResponse(Response):
    data: Optional[OrderDescribeResponseData] = None
