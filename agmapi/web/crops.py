from flask_restful import Resource
from flask import (
    request,
    jsonify,
    make_response
)

from agmapi.db.models import Stocks
from datetime import datetime


class StocksResource(Resource):

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
                    stocks = Stocks.objects(
                        date=date, name=crop_name
                    ).paginate(
                        page=page, per_page=per_page
                    )
                elif mandi_name:
                    stocks = Stocks.objects(
                        date=date, name=crop_name, mandi=mandi_name
                    ).paginate(
                        page=page, per_page=per_page
                    )
                elif crop_name and mandi_name:
                    stocks = Stocks.objects(
                        date=date, mandi=mandi_name
                    ).paginate(
                        page=page, per_page=per_page
                    )
                else:
                    stocks = Stocks.objects(
                        date=date
                    ).paginate(
                        page=page, per_page=per_page
                    )

            elif frm:
                frm = datetime.strptime(frm, '%d/%m/%Y')

                to = to if datetime.strptime(
                    to, '%d/%m/%Y') else datetime.utcnow()

                stocks = Stocks.objects(date=date, mandi=mandi_name
                                        ).paginate(
                    page=page, per_page=per_page
                )

            stocks = Stocks.objects(name=crop_name, mandi=mandi_name
                                    ).paginate(
                page=page, per_page=per_page
            )
        except Exception as e:
            raise e

        pass
