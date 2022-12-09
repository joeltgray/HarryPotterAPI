from flask import Flask
from flask_restful import Resource, Api, reqparse
from error_handling import GeneralException
from request_processor import Quotes
from ww_api import WWAPI, WWAPIErrors

def create_app() -> Flask:

    errors = WWAPIErrors()
    errors.add_error(GeneralException, 400)

    app = Flask("WizardingWords")
    api = WWAPI(error_list=errors, app=app)

    # APIS
    api.add_resource(Quotes, '/quote')
    application = app
    return application
