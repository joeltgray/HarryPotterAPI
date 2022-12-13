# WizardingWords
## A rest API for Harry Potter quotes
Currently at over 100 quotes and growing.
### Generate a random quote:
Example: $ curl 'https://wizardingwords.portkey.uk/app/api/app/quote'

### Generate a specific quote using UUID:
Syntax: $ curl 'https://wizardingwords.portkey.uk/app/api/app/quote/UUID'
Example: $ curl 'https://wizardingwords.portkey.uk/app/api/app/quote/a3e8d1f3-b2c3-40d3-a3e0-8ef9b9d3edb1'

Note: We do not allow a GET all quotes, please see the app/api/data/quotes.json file for all quotes.

## Disclaimer: 
Most quotes have been retrieved by AI, I have done my best to verify the accuracy of the quotes but this cannot be guaranteed.

## Submissions:
Submit any quotes to be added by emailing joel@graycode.ie, or submit a PR adding your quote to the quotes.json file with all the required attributes.