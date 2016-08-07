from flask import Flask
from flask_restplus import Api

drafthouse_app = Flask(__name__)
drafthouse_api = Api(drafthouse_app, version='1.0', title='Alamo Drafthouse Api',
                     description="An API wrapper around the alamo drafthouse information. "
                                 "\n\n\n Currently a work in progress. Will add more api's as I find time.")
