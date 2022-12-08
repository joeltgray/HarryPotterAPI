from flask_restful import Resource, request
from quote_parser import get_single_quote

class Quotes(Resource):

    def __init__(self):
        self.resource = "quotes"

    def get(self):
        response = get_single_quote()
        return response