from ..infra import Object
from .test_controller import TestController

# Instantiate controller dictionary.
Controllers = Object()

# Basic definition for controller addition.
def addController(controller):
    setattr(Controllers, controller.__name__, controller)


# Used to specify which controllers are currently available.
addController(TestController)

