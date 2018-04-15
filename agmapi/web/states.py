from flask_restful import Resource
from flask import jsonify

from agmapi.db.models import States
from agmapi.db.schemas import StatesSchema

from agmapi.utils import logger

schema = StatesSchema()


class StatesResource(Resource):

    def get(self):
        # Return a full list of states
        logger.debug("Sending states list without any filter")
        states = States.objects()
        states = schema.dump(states, many=True)
        return jsonify(states=states.data)
