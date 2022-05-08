from src.data.data import *
from src.biz.model.order import Order


class OrderBiz:
    order_repo: OrderRepo

    def __init__(self, order_repo: OrderRepo):
        # 访问数据库的东东
        self.order_repo = order_repo

    def describe_order(self, order_id: int) -> Order:
        # 通过数据库Repo获取数据库对象
        order = self.order_repo.select_order_by_id(order_id=order_id)

        if order is None:
            return None
        return order
