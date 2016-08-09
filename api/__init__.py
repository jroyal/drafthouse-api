from flask import Flask, Blueprint
from flask_restplus import Api

drafthouse_app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/drafthouse')
drafthouse_api = Api(blueprint, version='1.0', title='Alamo Drafthouse Api',
                     description="An API wrapper around the alamo drafthouse information. "
                                 "\n\n\n Currently a work in progress. Will add more api's as I find time.")

drafthouse_app.register_blueprint(blueprint)
