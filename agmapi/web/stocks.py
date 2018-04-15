from flask_restful import Resource
from flask import (
    request,
    jsonify,
    make_response
)

from agmapi.db.models import (
    Stocks,
    Commidities
)
from agmapi.db.schemas import StocksSchema
from datetime import datetime

schema = StocksSchema()


class StocksResource(Resource):

    def get(self):
        # Accept and parse params
        params = request.args
        date = params.get('date')
        frm = params.get('from')
        to = params.get('to')
        comm = params.get('commodity')
        mandi_name = params.get('mandi')
        page = int(params.get('page', 1))
        per_page = int(params.get('perPage', 10))
        per_page = 20 if per_page > 20 else per_page

        if not mandi_name:
            return make_response(
                jsonify(msg='`mandi` field is required'), 400
            )
        if not comm:
            return make_response(
                jsonify(msg='`commodity` field is required,'
                        ' and is an ObjectID'), 400
            )

        try:
            # On a specific date
            if date:
                date = datetime.strptime(date, '%d/%m/%Y')
                if comm and mandi_name:
                    try:
                        comm = Commidities.objects.get(name=comm)
                    except DoesNotExist:
                        return make_response(
                            jsonify(msg="No commodity in that name"), 404
                        )
                    stocks = Stocks.objects(
                        date=date, commodity=comm, mandi=mandi_name
                    ).paginate(
                        page=page, per_page=per_page
                    )
                elif comm:
                    try:
                        comm = Commidities.objects.get(name=comm)
                    except DoesNotExist:
                        return make_response(
                            jsonify(msg="No commodity in that name"), 404
                        )
                    stocks = Stocks.objects(
                        date=date,
                        commodity=comm
                    ).paginate(
                        page=page, per_page=per_page
                    )
                elif mandi_name:
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
            # Inside a range of date
            elif frm:
                frm = datetime.strptime(frm, '%d/%m/%Y')

                to = to if datetime.strptime(
                    to, '%d/%m/%Y') else datetime.utcnow()

                stocks = Stocks.objects(date=date, mandi=mandi_name
                                        ).paginate(
                    page=page, per_page=per_page
                )

            stocks = Stocks.objects().paginate(
                page=page, per_page=per_page
            )

            total = stocks.total
            print(total)
            page = stocks.page
            per_page = stocks.per_page
            total_pages = total/per_page
            stocks = schema.dump(stocks.items, many=True)
            return jsonify(
                stocks=stocks.data,
                page=page,
                per_page=per_page,
                total=total,
                total_pages=int(total_pages)
            )
        except Exception as e:
            raise e
