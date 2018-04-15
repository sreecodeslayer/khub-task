from flask_restful import Resource
from flask import jsonify

from agmapi.db.models import Mandis
from agmapi.db.schemas import MandisSchema

schema = MandisSchema()


class MandisResource(Resource):

    def get(self):
        # Return a full list of mandis
        mandis = Mandis.objects()
        mandis = schema.dump(mandis, many=True)
        return jsonify(mandis=mandis.data)
