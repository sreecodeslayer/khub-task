from flask_restful import Resource
from flask import (
    request,
    jsonify,
    make_response
)

from agmapi.db.models import Commidities
from agmapi.db.schemas import CommiditiesSchema
from datetime import datetime

schema = CommiditiesSchema()


class CommodityResource(Resource):

    def get(self):
        # Accept and parse params
        params = request.args

        name = params.get('name')
        typ = params.get('type')

        if name:
            comm = Commidities.objects.get(name=name)
            comm = schema.dump(comm)
            return jsonify(commidity=comm)
        elif typ:
            comms = Commidities.objects(typ=typ)
            comms = schema.dump(comms, many=True)
            return jsonify(commidities=comms.data)
        else:
            comms = Commidities.objects()
            comms = schema.dump(comms, many=True)
            return jsonify(commidities=comms)
