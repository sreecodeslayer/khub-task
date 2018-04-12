from flask import Flask, render_template
from flask_restful import Api

from .web import CropsResource

app = Flask('agmapi')

app.route('/')


def index():
    return render_template('index.html')


api = Api(app)

api.add_resource(CropsResource, '/api/crops')
