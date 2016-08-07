from flask_restplus import Resource, fields
from api import drafthouse_api
from drafthouse.markets import get_all_markets
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