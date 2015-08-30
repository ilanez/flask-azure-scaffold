# Imports
from src.infra import controller
from flask import render_template

from flask.ext.api import exceptions
from flask_api.renderers import BrowsableAPIRenderer
from .spec_definition import initialize_swagger as spec


# Defines routes.
def define_route(flask_app, controllers, configuration):

    @flask_app.route('/get_data', methods=['POST'])
    @controller(controllers.TestController)
    def get_data_post():
        """
        Retrieves test data
        ---
              tags:
                - Data
              parameters:
                - in: body
                  name: body
                  schema:
                    id: get_data_post_request
                    properties:
                        id:
                            type: string
                            required: true
              responses:
                200:
                  description: Request was successful, test data returned.
                  schema:
                    properties:
                      test_data:
                        type: string

        """
        pass

    @flask_app.route('/get_data', methods=['GET'])
    @controller(controllers.TestController)
    def get_data_get():
        """
        Retrieves test data
        ---
              tags:
                - Data
              responses:
                200:
                  description: Request was successful, test data returned.
                  schema:
                    properties:
                      test_data:
                        type: string
        """
        pass

    # #####Error handlers######

    # @flask_app.errorhandler(500)
    # def custom_error_handler_example:
    #     return render_template('500.html'), 500


    # Initialize specification endpoint.
    spec(flask_app, configuration)







