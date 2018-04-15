from flask_restful import Resource
from flask import jsonify

from agmapi.db.models import States
from agmapi.db.schemas import StatesSchema

schema = StatesSchema()


class StatesResource(Resource):

    def get(self):
        # Return a full list of states
        states = States.objects()
        states = schema.dump(states, many=True)
        return jsonify(states=states.data)
