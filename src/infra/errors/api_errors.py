__author__ = 'Beni Ben Zikry'
from flask_api.exceptions import (APIException, status)


class APIError(APIException):
    """
    Basic implementation for an API error.
    """
    def __init__(self, status_code, detail = None):
        if not isinstance(status_code, int):
            raise TypeError('status code must be of type int')
        self.status_code = status_code
        super(APIError, self).__init__(detail)


class BadRequest(APIException):
    def __init__(self, detail=None):
        self.status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(detail)


class InternalServerError(APIException):
    def __init__(self, detail=None):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.message = "Internal server error has occurred"
        super().__init__(detail)





