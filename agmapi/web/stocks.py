from flask_restful import Resource
from flask import (
    request,
    jsonify,
    make_response
)

from agmapi.db.models import (
    Stocks,
    Commidities,
    Mandis,
    States
)
from agmapi.db.schemas import StocksSchema
from datetime import datetime
from mongoengine.errors import (
    DoesNotExist,
    ValidationError
)

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
        mandi_id = params.get('mandi', '').strip()
        state_id = params.get('state', '').strip()
        page = int(params.get('page', 1))
        per_page = int(params.get('perPage', 10))
        per_page = 20 if per_page > 20 else per_page

        stocks = Stocks.objects()

        # Filter by state if asked
        if state_id:
            logger.debug("Filtering by states")
            try:
                state = States.objects.get(id=state_id)
                stocks = stocks.filter(state=state)
            except ValidationError:
                return make_response(
                    jsonify(msg="Field state needs to be an ObjectId"), 404
                )
            except DoesNotExist:
                return make_response(
                    jsonify(msg="No state in that name"), 404
                )

        # Filter by mandi and crop combos if asked
        if comm and mandi_id:
            logger.debug("Filtering by commodity and mandi together")
            try:
                comm = Commidities.objects.get(name=comm)
            except DoesNotExist:
                return make_response(
                    jsonify(msg="No commodity in that name"), 404
                )
            try:
                mandi = Mandis.objects.get(id=mandi_id)
            except ValidationError:
                return make_response(
                    jsonify(msg="Field mandi needs to be an ObjectId"), 404
                )
            except DoesNotExist:
                return make_response(
                    jsonify(msg="No mandi in that id"), 404
                )

            stocks = stocks.filter(
                commodity=comm, mandi=mandi
            )
        elif comm:
            logger.debug("Filtering by commodity")
            try:
                comm = Commidities.objects.get(name=comm)
            except DoesNotExist:
                return make_response(
                    jsonify(msg="No commodity in that name"), 404
                )

            stocks = stocks.filter(
                commodity=comm
            )
        elif mandi_id:
            logger.debug("Filtering by mandi")
            try:
                mandi = Mandis.objects.get(id=mandi_id)
            except ValidationError:
                return make_response(
                    jsonify(msg="Field mandi needs to be an ObjectId"), 404
                )
            except DoesNotExist:
                return make_response(
                    jsonify(msg="No mandi in that id"), 404
                )
            stocks = stocks.filter(
                mandi=mandi
            )

        # Filter by date or range now if asked
        # Date have precedence over range
        if date:
            logger.debug("Filtering by specific date")
            date = datetime.strptime(date, '%Y-%m-%d')
            stocks = stocks.filter(date=date)
        elif frm:
            logger.debug("Filtering by date range")
            frm = datetime.strptime(frm, '%Y-%m-%d')

            to = datetime.strptime(
                to, '%d/%m/%Y') if to else datetime.utcnow()
            stocks = stocks.filter(
                date__gte=frm,
                date__lte=to
            )

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
