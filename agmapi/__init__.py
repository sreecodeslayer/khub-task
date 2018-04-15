from flask import Flask, render_template
from flask_restful import Api

from .db import init_db
from .utils import init_logger, get_logger


app = Flask('agmapi')
app.config['DEBUG'] = True
app.config['MONGODB_SETTINGS'] = {
    'db': 'AGMAPI',
    'host': 'mongodb://localhost:27017/AGMAPI'
}


init_db(app)
init_logger(app)
logger = get_logger()

logger.info('Server ready!')


@app.route('/')
def index():
    return render_template('index.html')


from .web import (
    StocksResource,
    CommodityResource,
    StatesResource,
    MandisResource
)
api = Api(app)

api.add_resource(StocksResource, '/api/stocks')
api.add_resource(CommodityResource, '/api/commodities')
api.add_resource(StatesResource, '/api/states')
api.add_resource(MandisResource, '/api/mandis')
