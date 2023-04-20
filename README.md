# Harry Potter API

## A rest API for Harry Potter quotes
Currently at over 100 quotes and growing.
### Generate a random quote:
Example: $ curl 'https://api.portkey.uk/quote'

### Generate a specific quote using UUID:
Syntax: $ curl 'https://api.portkey.uk/quote/UUID'
Example: $ curl 'https://api.portkey.uk/quote/a3e8d1f3-b2c3-40d3-a3e0-8ef9b9d3edb1'

## Rate Limit
We do not allow a GET all quotes due to our rate limit, please see the data/quotes.json file for all quotes.
This api ('https://api.portkey.uk/quote') is rate limited to 50 requests per minute, if you implement this project yourself you can change this setting in the python code.

## Disclaimer: 
Most quotes have been retrieved by AI, I have done my best to verify the accuracy of the quotes but this cannot be guaranteed.

## Submissions:
Submit any quotes to be added by emailing joel@joelgray.work, or submit a PR adding your quote to the quotes.json file with all the required attributes.