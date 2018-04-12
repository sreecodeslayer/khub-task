from agmapi.db import get_db

# Models
db = get_db()


class Crops(db.Document):
    name = db.StringField(required=True)
    mandi = db.StringField()
    date = db.DateTimeField()
    modal_price = db.IntField()
    min_price = db.IntField()
    max_price = db.IntField()
    arrivals = db.FloatField()
