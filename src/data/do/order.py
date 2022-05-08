# DO：对应数据表，与数据表字段一一映射
class OrderDO:
    id: int
    order_id: int
    user_id: str
    order_ext_id: str
    merged_product_type: str
    product_type: str
    create_time: float

    def __init__(self, id: int, order_id: int, user_id: str, order_ext_id: str, merged_product_type: str,
                 product_type: str,
                 create_time: float):
        self.id = id
        self.order_id = order_id
        self.user_id = user_id
        self.order_ext_id = order_ext_id
        self.merged_product_type = merged_product_type
        self.product_type = product_type
        self.create_time = create_time
