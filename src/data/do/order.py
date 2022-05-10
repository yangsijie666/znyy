# DO：对应数据表，与数据表字段一一映射（可以只取关注的字段）
from typing import Type

from peewee import *


class OrderDO(Model):
    id = BigIntegerField(primary_key=True)
    userId = CharField()
    orderExtId = CharField()
    mergedProductType = CharField()
    productType = CharField()
    createTime = TimestampField()

    @classmethod
    def set_database(cls, db: Database) -> Type[Model]:
        cls._meta.database = db
        return cls

    class Meta:
        table_name = 'lxy_order'
