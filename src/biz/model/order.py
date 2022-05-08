class Order:
    order_id: int
    user_id: str
    order_ext_id: str
    merged_product_type: str
    product_type: str
    create_time: float

    def __init__(self, order_id: int, user_id: str, order_ext_id: str, merged_product_type: str, product_type: str,
                 create_time: float):
        self.order_id = order_id
        self.user_id = user_id
        self.order_ext_id = order_ext_id
        self.merged_product_type = merged_product_type
        self.product_type = product_type
        self.create_time = create_time
