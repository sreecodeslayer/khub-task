from flask_mongoengine import MongoEngine


def init_db(app):
    ''' Call this function to initialize a database connection '''
    global db

    db = MongoEngine(app)
    return db


def get_db():
    return db

# Models

class Crops(db.Document):
    name = db.StringField(required=True)
    mandi = db.StringField()
    date = db.DateTimeField()
    modal_price = db.IntField()
    min_price = db.IntField()
    max_price = db.IntField()
    arrivals = db.FloatField()
    