from src.config import settings
from src.data.do.order import *
from src.biz.model.order import Order
import src.data.translator.order as order_translator


class OrderRepo:
    db_name: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db: Database

    # 初始化，例如数据库地址等
    def __init__(self):
        self.db_name = settings.DB_NAME
        self.db_host = settings.DB_HOST
        self.db_port = settings.DB_PORT
        self.db_user = settings.DB_USER
        self.db_password = settings.DB_PASSWORD
        self._connect()

    def _connect(self):
        # 连接数据库
        self.db = MySQLDatabase(self.db_name, host=self.db_host, port=self.db_port, user=self.db_user,
                                password=self.db_password)
        self.db.connect()

    def select_order_by_id(self, order_id: int) -> Order:
        do_obj = self._select_order_by_id(order_id=order_id)

        # 通过转换器将 do 转换为领域对象 Order
        return order_translator.trans_to_entity(do_obj=do_obj)

    # 从 db 中获取订单详情
    def _select_order_by_id(self, order_id: int) -> OrderDO:
        return OrderDO.set_database(self.db).get_or_none(OrderDO.id == order_id)
