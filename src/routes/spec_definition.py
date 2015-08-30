__author__ = 'Beni Ben Zikry'
from flask_swagger import swagger
from json import dumps as jsonify
from flask_api.decorators import (set_renderers)
from flask_api.renderers import JSONRenderer, HTMLRenderer
from flask import request, render_template

"""
Expose Swagger specification to the outside world.
Must be initialized last to

A) Enumerate over all available endpoints.
B) Set static folder for swagger UI.
"""


def initialize_swagger(app, configuration):

    # The specification route.
    @app.route('/spec')
    @set_renderers(JSONRenderer)
    def swagger_spec():

        # Get swagger application.
        swag = swagger(app)
        swag['info']['title'] = configuration.APP_NAME
        swag['info']['version'] = configuration.VERSION
        return swag

    @app.route('/<path:path>')
    def get_static_files(path):
        return app.send_static_file(path)

    @app.route('/')
    @set_renderers(HTMLRenderer)
    def index():
        model = dict(url="/spec")
        return render_template('index.html', model = model)



