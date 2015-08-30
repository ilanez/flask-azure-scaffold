import yaml
import os.path
from os import (getenv)
from sys import (exit)
import io
from src.infra.patterns.singleton import singleton_value_decorator as singleton


class ConfigurationConstants(object):
    ENVIRONMENT_VARIABLE_NAME = "ENVIRONMENT"
    CONFIGURATION_FILE_NAME = "conf.yaml"
    PRODUCTION = "PRODUCTION"
    TEST = "TEST"
    DEVELOPMENT = "DEVELOPMENT"

class _SpecificFieldConstants(object):
        GOOGLE_PRIVATE_KEY = 'google_private_key'


class _ConfigInternal(object):
	pass


def initialize_config():
    internal_config = _ConfigInternal()
    environment = getenv(ConfigurationConstants.ENVIRONMENT_VARIABLE_NAME)

    # Check environment.
    if not environment:
         raise EnvironmentError("Environment variable %s wasn't provided."
                                       % ConfigurationConstants.ENVIRONMENT_VARIABLE_NAME)

    # Get configuration.
    yaml_config = _parse_yaml(environment)

    # Add items to internal configuration implementation.
    for (k,v) in yaml_config.items():
        setattr(internal_config, k, v)

        # Set configuration constants into internal config.
        setattr(internal_config, ConfigurationConstants.__name__, ConfigurationConstants)
    return internal_config



def _parse_yaml(environment):

    current_dir = os.path.dirname(__file__)
    config_file = os.path.join(current_dir, environment, ConfigurationConstants.CONFIGURATION_FILE_NAME)

    try:
        with io.open(config_file, encoding='UTF-8') as file_stream:
            parsed = yaml.load(file_stream)
            parsed[ConfigurationConstants.ENVIRONMENT_VARIABLE_NAME] = environment
            return parsed
    except IOError:
        print("Couldn\'t load config file at %s" % config_file)
        exit(1)


@singleton(initialize_config)
class Configuration(object):
    pass







