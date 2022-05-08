from pydantic import BaseModel
from typing import Optional

from src.utils.error import Error
from src.utils.uuid import build_random_id


class Request(BaseModel):
    request_id: Optional[str] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.request_id is None:
            self.request_id = build_random_id()

    # 校验
    def validate_self(self) -> Error:
        return None

    # 填充默认值
    def fill_self(self):
        pass


class Response(BaseModel):
    code: str
    message: Optional[str] = None
    data: Optional[object] = None
    request_id: Optional[str]
