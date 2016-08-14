from flask_restplus import Resource, fields
from api import drafthouse_api
from drafthouse.cinemas import get_cinema
ns = drafthouse_api.namespace('cinemas', description='Cinema operations')


@ns.route('/<string:cinema_id>')
@ns.param('cinema_id', 'The 4 digit cinema id')
class GetCinema(Resource):

    def get(self, cinema_id):
        """
        Get information on a single cinema
        :return:
        """
        return get_cinema(cinema_id)
