from flask_restful import Resource
from flask import jsonify

from agmapi.db.models import Mandis
from agmapi.db.schemas import MandisSchema

from agmapi.utils import logger

schema = MandisSchema()


class MandisResource(Resource):

    def get(self):
        # Return a full list of mandis
        logger.debug("Sending mandis list without any filter")
        mandis = Mandis.objects()
        mandis = schema.dump(mandis, many=True)
        return jsonify(mandis=mandis.data)
