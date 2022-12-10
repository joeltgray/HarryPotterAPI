from flask_restful import Resource, request
from quote_parser import get_single_quote, get_quote_by_uuid

class Quote(Resource):

    def __init__(self):
        self.resource = "quote"

    def get(self):
        response = get_single_quote()
        return response

class QuoteByUUID(Resource):

    def __init__(self):
        self.resource = "quote_by_uuid"

    def get(self, uuid):
        response = get_quote_by_uuid(uuid)
        return response