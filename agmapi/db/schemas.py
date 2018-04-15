from marshmallow import (
    Schema,
    fields,
    validate,
    pre_load,
    post_dump,
    post_load
)
from bson import ObjectId


class ObjectID(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            ''
        return str(value)


Schema.TYPE_MAPPING[ObjectId] = ObjectID


from .models import (
    Commidities,
    Stocks
)


class CommiditiesSchema(Schema):
    id = ObjectID(dump_only=True)
    name = fields.String()
    typ = fields.String()


class StocksSchema(Schema):
    id = ObjectID(dump_only=True)
    commodity = fields.Nested(CommiditiesSchema, dump_only=True)
    state = fields.String(dump_only=True)
    mandi = fields.String(dump_only=True)
    date = fields.DateTime(dump_only=True)
    modal_price = fields.String(dump_only=True)
    min_price = fields.String(dump_only=True)
    max_price = fields.String(dump_only=True)
    arrivals = fields.String(dump_only=True)
