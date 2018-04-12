from flask import Flask, render_template
from .db import init_db
from flask_restful import Api

from .web import CropsResource

app = Flask('agmapi')
app.config['DEBUG'] = True
app.config['MONGODB_SETTINGS'] = {
    'db': 'AGMAPI',
    'host': 'mongodb://localhost:27017/AGMAPI'
}

db = init_db(app)


@app.route('/')
def index():
    return render_template('index.html')


api = Api(app)

api.add_resource(CropsResource, '/api/crops')
