from src.data.do.order import OrderDO
from src.biz.model.order import Order


def trans_to_entity(do_obj: OrderDO) -> Order:
    if do_obj is None:
        return None
    return Order(order_id=do_obj.order_id, user_id=do_obj.user_id, order_ext_id=do_obj.order_ext_id,
                 merged_product_type=do_obj.merged_product_type, product_type=do_obj.product_type,
                 create_time=do_obj.create_time)
