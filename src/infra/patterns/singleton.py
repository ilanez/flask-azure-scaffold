__author__ = 'Beni Ben-Zikry'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


def singleton_value_decorator(object_initialization_delegate):
    instances = {}

    def internal_decorator(cls):

        if cls not in instances:
            instances[cls] = object_initialization_delegate()

        # Always return the same object
        cls.__new__ = staticmethod(lambda cls: instances[cls])

        # Disable __init__
        try:
            del cls.__init__
        except AttributeError:
            pass
        return cls
    return internal_decorator

