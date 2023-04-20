from flask import Flask
from flask_restful import Resource, Api, reqparse
from error_handling import GeneralException
from request_processor import Quote, QuoteByUUID
from ww_api import WWAPI, WWAPIErrors
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

def create_app() -> Flask:

    # Error Handling
    errors = WWAPIErrors()
    errors.add_error(GeneralException, 400)

    # Flask App and API
    app = Flask("HarryPotterAPI")

    # Rate Limiting
    limiter = Limiter(app=app, key_func=get_remote_address, default_limits=["50 per minute"])
    
    api = WWAPI(error_list=errors, app=app)

    # APIS
    api.add_resource(Quote, '/quote')
    api.add_resource(QuoteByUUID, '/quote/<uuid>')
    application = app
    return application
