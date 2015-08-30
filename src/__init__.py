#!/usr/bin/python
import os

from flask.ext.api import FlaskAPI, status, exceptions
from src.configuration import Configuration
from src.validation.validation_handler import initialize_validators as hook_validators

# Initialize Flask API.
app = FlaskAPI(__name__.split('.')[0], static_url_path='/')

# Get routes.
from src.routes import route

# Acquire controllers.
from src.controllers import (Controllers)

# Get configuration.
config = Configuration()

# Set routes for flask application.
route(app, Controllers, config)

# Set debugging if necessary.
if config.ENVIRONMENT == config.ConfigurationConstants.DEVELOPMENT:
    app.debug = True

# Set JSON schemas
app.config['JSONSCHEMA_DIR'] = os.path.join(app.root_path, 'DTO/schemas')

# Set request level validators.
hook_validators(app)

# Run flask application.
if __name__ == '__main__':
    app.run()



