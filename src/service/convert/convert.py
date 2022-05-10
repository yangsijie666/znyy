import time
from src.utils.error import not_found

from src.biz.model.order import Order
from src.service.dto.describe import Response, OrderDescribeResponse, OrderDescribeResponseData


def convert_order_to_order_describe_response(order: Order) -> Response:
    if order is None:
        err = not_found("Order is not found.")
        return Response(code=err.code, message=err.message)
    return OrderDescribeResponse(code="Success",
                                 data=OrderDescribeResponseData(id=order.order_id, user_id=order.user_id,
                                                                order_ext_id=order.order_ext_id,
                                                                merged_product_type=order.merged_product_type,
                                                                product_type=order.product_type,
                                                                create_time=order.create_time.strftime(
                                                                    "%Y-%m-%d %H:%M:%S.%f")))
