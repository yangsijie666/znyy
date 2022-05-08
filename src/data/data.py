from typing import Optional

from src.config import settings
from src.data.do.order import *
from src.biz.model.order import Order
import src.data.translator.order as order_translator


class OrderRepo:
    driver: str
    source: str

    # 初始化，例如数据库地址等
    def __init__(self):
        self.driver = settings.DRIVER
        self.source = settings.SOURCE
        self._connect()

    def _connect(self):
        # 连接数据库
        pass

    def select_order_by_id(self, order_id: int) -> Order:
        do_obj = self._select_order_by_id(order_id=order_id)

        # do_obj = OrderDO(
        #     id=1, order_id=123, user_id="123", order_ext_id="123",
        #     merged_product_type="sss",
        #     product_type="xxxx", create_time=1459175064.0
        # )

        # 通过转换器将 do 转换为领域对象 Order
        return order_translator.trans_to_entity(do_obj=do_obj)

    # 从 db 中获取订单详情
    def _select_order_by_id(self, order_id: int) -> OrderDO:
        # ...
        pass

