__author__ = 'Beni Ben Zikry'
from functools import wraps

def controller(controller_instance):
    """
    Decorator to set controller for a certain FLASK action method.
    :param controller_instance: The controller type
    :return: the decorator function.
    """
    def function_decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            instance = controller_instance()
            return instance[func.__name__](*args, **kwargs)
        wrap.__name__ = func.__name__
        return wrap
    return function_decorator




