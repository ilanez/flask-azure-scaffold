__author__ = 'Beni Ben-Zikry'

from peewee import *
from string_helper import StringHelper as STRING_HELPER
from playhouse.csv_loader import load_csv

def transform_models(func):
    """
    A decorator used to transform models passed into the DAL to their corresponding proxy object.
    :param func:
    :return:
    """
    def decorator(self, *args, **kwargs):

        # meta magic
        """Create so called MetaClass required by peewee"""
        Meta = type('Meta', (), {'database': self._db})

        def transform_model_internal(model):

            # get class specification
            cls = model

            # Create generated model class
            generated_class = type(cls.__name__, (cls, ), {'Meta': Meta})
            # Generated_class.original_name = cls.__name__
            return generated_class

        # Transform all models to models with the correct MetaClass
        transformed_models = [transform_model_internal(arg) for arg in args[0]]

        # call original function with transformed models
        return func(self, transformed_models, **kwargs)

    return decorator


class DataAccessLayer(object):

    def __init__(self, conn_string=":memory:"):
        self._db = self._create_connection(conn_string)
        self._models = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._db:
            try:
                self._db.close()

            except Exception as e:

                """Obviously,
                better logging should be used here"""
                print 'exception encountered', e.message
                pass

    #TODO: Add support for different types of DBs - sql server/ODBC exists.
    @classmethod
    def _create_connection(cls, conn_string):
        try:
            # instantiate ORM
            db = SqliteDatabase(conn_string)

            return db
        except Exception as e:
            print 'exception encountered during database initialization:', STRING_HELPER.NEW_LINE, \
            e.message
            raise

    @transform_models
    def add_models(self, models):
        """
        :param models: The peewee models to use for initialization.
        Used before initialize_tables
        """

        model_dict = {model.__name__: model for model in models}
        self._models.update(model_dict)


    def initialize_tables(self):
        """
        Initializes tables for each model added.
        """
        if len(self._models) > 0:
            self._db.create_tables(self._models.values())

    def get_model_by_name(self, model_name):
        """
        :param model_name: The model name
        :return: A model for the perticular DB(issue with peewee - Meta class must be created dynamically
        """
        returned_model = self._models[model_name]
        if returned_model:
            return returned_model
        return None

    def drop_all_tables(self):
        """
        Drops all tables in the DB - should only be used for initial bootstrapping.
        """
        if len(self._models) > 0:
            try:
                self._db.drop_tables(self._models.values())
            except OperationalError:
                pass

    @staticmethod
    def upload_csv(model, path):
        """Uploads a csv file into the DB"""
        load_csv(model, path)




