from agmapi.db import get_db

# Models
db = get_db()


class Commidities(db.Document):
    types = db.ListField()
    name = db.StringField(unique=True)

    meta = {
        'indexes': ['name', 'types']
    }


class States(db.Document):
    name = db.StringField(unique=True)


class Mandis(db.Document):
    name = db.StringField()
    state = db.ReferenceField(States)

    meta = {
        'indexes': ['name', 'state']
    }


class Stocks(db.Document):
    commodity = db.ReferenceField(Commidities)
    state = db.ReferenceField(States)
    mandi = db.ReferenceField(Mandis)
    date = db.DateTimeField()
    modal_price = db.StringField()
    min_price = db.StringField()
    max_price = db.StringField()
    arrivals = db.StringField()

    meta = {
        'indexes': ['state', 'date', 'modal_price', 'min_price', 'max_price']
    }
