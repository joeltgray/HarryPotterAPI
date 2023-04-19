from flask import Response
import json

def response_missing_uuid(uuid) -> Response:
    # Return a 400 error with the printed message as the json response
    msg = 'A quote with the UUID {} does not exist, pls try again pal.'.format(uuid)
    return Response(
        json.dumps({'KeyError': msg, 'Solution': 'If you wish to specify a quote you can reference a UUID from the list of all quotes in the github repo', 'GitHub Repo': 'https://github.com/joeltgray/WizardingWords'}),
        status=404,
        mimetype='application/json'
    )

def response_missing_file() -> Response:
    # Return a 400 error with the printed message as the json response
    return Response(
        json.dumps({'error': 'The file does not exist.', 'data': data}),
        status=400,
        mimetype='application/json'
    )

def response_invalid_format() -> Response:
    # Return a 400 error with the printed message as the json response
    return Response(
        json.dumps({'error': 'The file does not contain valid JSON data.', 'data': data}),
        status=400,
        mimetype='application/json'
    )