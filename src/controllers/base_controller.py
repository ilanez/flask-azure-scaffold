"""
Import for sub-controllers.
"""
from flask_api.exceptions import APIException
#from flask.ext.api import status as HttpStatus
from flask import request, url_for
from flask import current_app
from flask import Response


class BaseController(object):
    def __getitem__(self, item):
        return getattr(self, item)

    def __init__(self):
        self.app = current_app
