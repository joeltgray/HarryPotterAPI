from flask import Flask, jsonify
from typing import Dict
import json
import random
from utilities import format_json
import logging
import traceback
from failure_responses import *

data = None

def get_single_quote() -> Dict:
    quote_list = get_quote_list()
    random_quote = format_json(random.choice(quote_list))
    return random_quote


def get_quote_by_uuid(uuid) -> Dict:
    quote_list = get_quote_list()

    for quote in quote_list:
        if quote['id'] == str(uuid):
            return quote
    
    return response_missing_uuid(uuid)


def get_quote_list() -> Dict:
    global data
    quote_path = '/var/www/wizardingwords/app/data/quotes.json'
    
    try:
        # open the json file
        with open('data/quote.json', "r", encoding='utf-8') as quote_list:
            # load the json data into a python dictionary
            data = json.load(quote_list)
            
    except FileNotFoundError as e:
            # Handle the FileNotFoundError exception
            print('The file does not exist.')
            logging.info("'error': 'The file does not exist.', 'path': {}".format(quote_path))
            logging.error(traceback.format_exc())

            return response_missing_file()

    except Exception as e:
        # Handle the ValueError exception
        print('The file does not contain valid JSON data.')
        logging.info("'error': 'The file does not contain valid JSON data.', 'path': {}".format(quote_path))
        logging.error(traceback.format_exc())
        
        return response_invalid_format()

    return data