import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/wizardingwords/venv/lib/python3.10/site-packages/')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/wizardingwords/app/api')

# Activate your virtual env
activate_env="/var/www/wizardingwords/venv/bin/activate.fish"
execfile(activate_env, dict(__file__=activate_env))

from app import create_app

application = create_app()