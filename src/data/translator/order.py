from src.data.do.order import OrderDO
from src.biz.model.order import Order


def trans_to_entity(do_obj: OrderDO) -> Order:
    if do_obj is None:
        return None
    return Order(order_id=do_obj.id, user_id=do_obj.userId, order_ext_id=do_obj.orderExtId,
                 merged_product_type=do_obj.mergedProductType, product_type=do_obj.productType,
                 create_time=do_obj.createTime)
