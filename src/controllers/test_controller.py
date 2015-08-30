__author__ = 'Beni Ben Zikry'
from .base_controller import *
from ..infra.errors import (APIError, BadRequest, InternalServerError)
from flask_api.exceptions import (NotFound)


class TestController(BaseController):
    """
    A basic test controller
    """
    @staticmethod
    def get_data_get():

        """
        Returns sample data.
        :return: test data.
        """

        return {'test_data': "GET operation"}

    @staticmethod
    def get_data_post():
        """
        mock data for a post operation.
        :return: test data for a post operation.
        """
        return {'test data': 'POST OPERATION'}






