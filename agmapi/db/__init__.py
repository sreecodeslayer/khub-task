from flask_mongoengine import MongoEngine


def init_db(app):
    ''' Call this function to initialize a database connection '''
    global db

    db = MongoEngine(app)
    return db


def get_db():
    return db
