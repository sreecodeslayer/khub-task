from flask_restful import Resource
from flask import (
    request,
    jsonify,
    make_response
)


class CropsResource(Resource):

    def get(self):
        # Accept and parse params
        params = request.args

        date = params.get('date')
        frm = params.get('from')
        to = params.get('to')
        crop_name = params.get('crop')
        mandi_name = params.get('mandi')
        page = params.get('page')
        per_page = params.get('perPage')

        pass
