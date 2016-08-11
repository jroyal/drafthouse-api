from flask_restplus import Resource, fields
from api import drafthouse_api
from drafthouse.markets import get_all_markets
from drafthouse.cinemas import get_cinemas
ns = drafthouse_api.namespace('markets', description='Market operations')

market = drafthouse_api.model('Market', {
    "market_id": fields.String(required=True, description="The market id number"),
    "name": fields.String(required=True, decription="The full market name"),
    "short_name": fields.String(required=True, description="The markets short name used in the URL")
})


@ns.route('/')
class Markets(Resource):

    @ns.marshal_list_with(market)
    def get(self):
        """
        Get all markets
        """
        return get_all_markets()


@ns.route('/<string:market_id>/cinemas')
@ns.param('market_id', 'The 4 digit market id')
class MarketCinemas(Resource):

    def get(self, market_id):
        """
        Get all cinemas in a market
        :return:
        """
        return get_cinemas(market_id)