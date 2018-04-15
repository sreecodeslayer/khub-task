from agmapi.db import get_db

# Models
db = get_db()


class Commidities(db.Document):
    type = db.StringField()
    name = db.StringField(unique=True)

    meta = {
        'indexes': ['name', 'type']
    }


class Stocks(db.Document):
    commodity = db.ReferenceField(Commidities)
    state = db.StringField()
    mandi = db.StringField()
    date = db.DateTimeField()
    modal_price = db.StringField()
    min_price = db.StringField()
    max_price = db.StringField()
    arrivals = db.StringField()

    meta = {
        'indexes': ['state', 'date', 'modal_price', 'min_price', 'max_price']
    }
