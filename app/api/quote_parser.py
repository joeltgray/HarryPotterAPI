from flask import Flask, jsonify, Response
from typing import Dict
import json
import random
from error_handling import GeneralException
import logging
import traceback

data = None

def get_single_quote() -> Dict:
    global data
    quote_path = '/home/joel/WizardingWords/app/api/data/quotes.json'
    
    try:
        # open the json file
        with open(quote_path, "r", encoding='utf-8') as quote_list:
            # load the json data into a python dictionary
            data = json.load(quote_list)
    # except FileNotFoundError as e:
    #         # Handle the FileNotFoundError exception
    #         print('The file does not exist.')
    #         logging.info("Some sort of not found error error: ", e)
    #         logging.info("'error': 'The file does not exist.', 'path': {}".format(quote_path))
    #         # Return a 400 error with the printed message as the json response
    #         return Response(
    #             json.dumps({'error': 'The file does not exist.', 'path': quote_path, 'data': data}),
    #             status=400,
    #             mimetype='application/json'
    #         )
    except Exception as e:
        # Handle the ValueError exception
        print('The file does not contain valid JSON data.')
        logging.info("Some sort of value error: ", e)
        logging.info("'error': 'The file does not contain valid JSON data.', 'path': {}".format(quote_path))
        logging.error(traceback.format_exc())
        # Return a 400 error with the printed message as the json response
        return Response(
            json.dumps({'error': 'The file does not contain valid JSON data.', 'path': quote_path, 'data': data}),
            status=400,
            mimetype='application/json'
        )

    random_quote = random.choice(data)
    return random_quote
