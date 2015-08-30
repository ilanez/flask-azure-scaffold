"""
Validation handlers for incoming JSON data based on schemas in DTO/schemas
"""
import os

try:
    import simplejson as json
except ImportError:
    import json

from flask import current_app, request
from jsonschema import ValidationError, validate

def init_app(app):
    default_dir = os.path.join(app.root_path, 'jsonschema')
    schema_dir = app.config.get('JSONSCHEMA_DIR', default_dir)
    schemas = {}
    for fn in os.listdir(schema_dir):
        key = fn.split('.')[0]
        fn = os.path.join(schema_dir, fn)
        if os.path.isdir(fn) or not fn.endswith('.json'):
            continue
        with open(fn) as f:
            actions = json.load(f)
            for key in actions:
                if key in schemas:
                    raise ValueError('key %s is used twice in configuration. source file name: %s' %(key, fn))
                schemas[key] = actions[key]

    return schemas

def initialize_validators(app):

    # Initialize json schemas.
    schemas = init_app(app)

    # Subscribe to before_request for validation hook.
    @app.before_request
    def json_validate():
        current_path = request.path
        current_path = current_path[1:len(current_path)]
        request_method = request.method.lower()
        path_schema = None

        if request_method == 'get':
            if current_path in schemas:
                path_schema = schemas[current_path]
                if request_method in path_schema:
                    schema = path_schema[request_method]
                    all_arguments = request.args
                    validate(all_arguments, schema)

        else:
            if request.json is not None:
                # Other methods must all have application/json defined.
                try:
                    schema = schemas[current_path][request.method.lower()]
                except KeyError:
                    raise ValidationError('Couldn\'t acquire method key for schema %s , key requested was %s' %(current_path,
                                                                                                         request.method))
                validate(request.json, schema)



