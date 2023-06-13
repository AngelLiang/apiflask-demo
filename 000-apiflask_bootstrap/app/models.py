from peewee import *

from .db import BaseModel


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BuyRecord(BaseModel):
    buy_at = DateTimeField()
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_barcode = CharField(constraints=[SQL("DEFAULT ''")])
    goods_id = IntegerField()
    goods_name = CharField()
    handled_at = DateTimeField(null=True)
    policy_id = IntegerField(null=True)
    policy_item_detail_id = IntegerField(null=True)
    policy_item_id = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'buy_record'


class Client(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = IntegerField()
    online_at = DateTimeField(null=True)
    sn = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'client'
        indexes = (
            (('id', 'status'), True),
        )
        primary_key = CompositeKey('id', 'status')


class Enterprise(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'enterprise'


class Goods(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_barcode = CharField(null=True)
    goods_name = CharField()
    purchase_price = DecimalField(null=True)
    sale_price = DecimalField(null=True)
    unit = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods'


class GoodsCategory(BaseModel):
    category_code = CharField()
    category_name = CharField()
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    parent_category = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods_category'


class GoodsTag(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    tag_name = CharField()
    tag_weight = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods_tag'


class GoodsTagGoods(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    goods_code = CharField(null=True)
    goods_id = IntegerField()
    tag_id = IntegerField()
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods_tag_goods'
        indexes = (
            (('goods_id', 'tag_id'), True),
        )
        primary_key = CompositeKey('goods_id', 'tag_id')


class Policy(BaseModel):
    client_id = IntegerField(null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deleted_at = DateTimeField(null=True)
    name = CharField(null=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'policy'


class PolicyItem(BaseModel):
    close_time = TimeField(null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_rest = IntegerField(constraints=[SQL("DEFAULT 0")])
    open_time = TimeField(null=True)
    policy_id = IntegerField()
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    week = CharField(constraints=[SQL("DEFAULT '1'")])

    class Meta:
        table_name = 'policy_item'


class PolicyItemDetail(BaseModel):
    begin_time = TimeField()
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deleted_at = DateTimeField(null=True)
    end_time = TimeField()
    policy_item_id = IntegerField()
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    week = IntegerField(constraints=[SQL("DEFAULT 1")])

    class Meta:
        table_name = 'policy_item_detail'


class PolicyItemDetailGoods(BaseModel):
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deleted_at = DateTimeField(null=True)
    goods_barcode = CharField(null=True)
    goods_id = IntegerField(null=True)
    goods_name = CharField()
    policy_item_detail_id = IntegerField()
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'policy_item_detail_goods'
