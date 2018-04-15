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
    Stocks,
    Mandis,
    States
)


class StatesSchema(Schema):
    id = ObjectID(dump_only=True)
    name = fields.String()


class MandisSchema(Schema):
    id = ObjectID(dump_only=True)
    name = fields.String()
    state = fields.Nested(StatesSchema, dump_only=True)


class CommiditiesSchema(Schema):
    id = ObjectID(dump_only=True)
    name = fields.String()
    types = fields.List(fields.String)


class StocksSchema(Schema):
    id = ObjectID(dump_only=True)
    commodity = fields.Nested(CommiditiesSchema, dump_only=True)
    state = fields.Nested(StatesSchema, dump_only=True)
    mandi = fields.Nested(MandisSchema, dump_only=True)
    date = fields.DateTime(dump_only=True)
    modal_price = fields.String(dump_only=True)
    min_price = fields.String(dump_only=True)
    max_price = fields.String(dump_only=True)
    arrivals = fields.String(dump_only=True)
