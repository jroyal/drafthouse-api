from flask import Flask, Blueprint
from flask_restplus import Api


def my_register(self, app, options, first_registration=False):
    """Called by :meth:`Flask.register_blueprint` to register a blueprint
    on the application.  This can be overridden to customize the register
    behavior.  Keyword arguments from
    :func:`~flask.Flask.register_blueprint` are directly forwarded to this
    method in the `options` dictionary.
    """
    if self.name == "restplus_doc":
        self.static_url_path = "/drafthouse/swaggerui"
    self._got_registered_once = True
    state = self.make_setup_state(app, options, first_registration)
    if self.has_static_folder:
        state.add_url_rule(self.static_url_path + '/<path:filename>',
                           view_func=self.send_static_file,
                           endpoint='static')

    for deferred in self.deferred_functions:
        deferred(state)

Blueprint.register = my_register

drafthouse_app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/drafthouse')
drafthouse_api = Api(blueprint, version='1.0', title='Alamo Drafthouse Api',
                     description="An API wrapper around the alamo drafthouse information. "
                                 "\n\n\n Currently a work in progress. Will add more api's as I find time.")

drafthouse_app.register_blueprint(blueprint)
