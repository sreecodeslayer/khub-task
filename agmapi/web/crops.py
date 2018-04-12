from flask_restful import Resource
from flask import (
    request,
    jsonify,
    make_response
)

from agmapi.db.models import Crops
from datetime import datetime


class CropsResource(Resource):

    def get(self):
        # Accept and parse params
        params = request.args

        date = params.get('date')
        frm = params.get('from')
        to = params.get('to')
        crop_name = params.get('crop')
        mandi_name = params.get('mandi')
        page = int(params.get('page', 1))
        per_page = int(params.get('perPage', 10))
        per_page = 20 if per_page > 20 else per_page

        try:
            if date:
                date = datetime.strptime(date, '%d/%m/%Y')
                if crop_name:
                    crops = Crops.objects(date=date, name=crop_name).paginate(
                        page=page, per_page=per_page)
                elif mandi_name:
                    crops = Crops.objects(date=date, name=crop_name, mandi=mandi_name).paginate(
                        page=page, per_page=per_page)
                elif crop_name and mandi_name:
                    crops = Crops.objects(date=date, mandi=mandi_name).paginate(
                        page=page, per_page=per_page)
                else:
                    crops = Crops.objects(date=date).paginate(
                        page=page, per_page=per_page)

            elif frm:
                frm = datetime.strptime(frm, '%d/%m/%Y')

                to = to if datetime.strptime(
                    to, '%d/%m/%Y') else datetime.utcnow()

                crops = Crops.objects(date=date, mandi=mandi_name).paginate(
                    page=page, per_page=per_page)

            crops = Crops.objects(name=crop_name, mandi=mandi_name).paginate(
                page=page, per_page=per_page)
        except Exception as e:
            raise e

        pass
