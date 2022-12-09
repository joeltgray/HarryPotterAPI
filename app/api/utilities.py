import json
from decimal import Decimal
from datetime import date

def format_json(logger, json_data):
    if is_jsonable(json_data) == True:
        return json_data
    else:
        logger.warning("Json contains unserializable data, returning string-ified version")
        serialised_json = json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': '), cls=JsonSerialiser)
        return json.loads(serialised_json)

def is_jsonable(data):
    try:
        json.dumps(data)
        return True
    except (TypeError, OverflowError):
        return False

class JsonSerialiser(json.JSONEncoder):
    def default(self, obj):
        #If passed in object is instance of Decimal convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)

        #If passed in object is instance of Date convert it to a isodate
        if isinstance(obj, date):
            return str(obj)

        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

