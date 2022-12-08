from flask import Flask, jsonify, Response
from typing import Dict
import json
import random
from error_handling import GeneralException

data = None

def get_single_quote() -> Dict:
    
    try:
        # open the json file
        with open('data/quotes.json') as quote_list:
            # load the json data into a python dictionary
            data = json.load(quote_list)
    except FileNotFoundError:
            # Handle the FileNotFoundError exception
            print('The file does not exist.')
            # Return a 400 error with the printed message as the json response
            return Response(
                json.dumps({'error': 'The file does not exist.'}),
                status=400,
                mimetype='application/json'
            )
    except ValueError:
        # Handle the ValueError exception
        print('The file does not contain valid JSON data.')
        # Return a 400 error with the printed message as the json response
        return Response(
            json.dumps({'error': 'The file does not contain valid JSON data.'}),
            status=400,
            mimetype='application/json'
        )

    random_quote = random.choice(data)
    return random_quote