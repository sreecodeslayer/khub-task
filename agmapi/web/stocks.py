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
from mongoengine.errors import DoesNotExist

from agmapi.utils import logger

schema = StocksSchema()


class StocksResource(Resource):

    def get(self):
        # Accept and parse params
        params = request.args

        logger.debug(params)

        date = params.get('date')
        frm = params.get('from')
        to = params.get('to')
        comm = params.get('commodity')
        mandi_name = params.get('mandi')
        page = int(params.get('page', 1))
        per_page = int(params.get('perPage', 10))
        per_page = 20 if per_page > 20 else per_page

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
                    date=date, commodity=comm, mandi__icontains=mandi_name
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
                )
            elif mandi_name:
                stocks = Stocks.objects(
                    date=date, mandi=mandi_name
                )
            else:
                stocks = Stocks.objects(
                    date=date
                )
        # Inside a range of date , not implemented yet
        elif frm:
            frm = datetime.strptime(frm, '%d/%m/%Y')

            to = datetime.strptime(
                to, '%d/%m/%Y') if to else datetime.utcnow()
            if comm and mandi_name:
                comm = Commidities.objects.get(name=comm)
                stocks = Stocks.objects(
                    date__gte=frm,
                    date__lte=to,
                    mandi__icontains=mandi_name,
                    commodity=comm
                )
            elif comm:
                try:
                    comm = Commidities.objects.get(name=comm)
                except DoesNotExist:
                    return make_response(
                        jsonify(msg="No commodity in that name"), 404
                    )

                stocks = Stocks.objects(
                    date__gte=frm,
                    date__lte=to,
                    commodity=comm
                )
            elif mandi_name:
                stocks = Stocks.objects(
                    date__gte=frm,
                    date__lte=to,
                    mandi__icontains=mandi_name,
                )
            else:
                stocks = Stocks.objects(
                    date=date
                )

        if not stocks:
            stocks = Stocks.objects()

        if int(stocks.count()/per_page) >= page:
            # Flask mongoengine throws a general 404 on over pagination
            # This gives no flexibility on pagination
            stocks = stocks.paginate(
                page=page, per_page=per_page
            )
            total = stocks.total
            page = stocks.page
            per_page = stocks.per_page
            total_pages = total/per_page
            stocks = stocks.items
        else:

            total = stocks.count()
            page = 1
            per_page = per_page
            total_pages = total/per_page

        stocks = schema.dump(stocks, many=True)
        return jsonify(
            stocks=stocks.data,
            page=page,
            per_page=per_page,
            total=total,
            total_pages=int(total_pages)
        )
