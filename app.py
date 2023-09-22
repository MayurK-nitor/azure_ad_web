from azure_ad_web import IdentityWebPython
from azure_ad_web.adapters import FlaskContextAdapter
from azure_ad_web.configuration import AADConfig
from cryptography.fernet import Fernet
from flask import (Flask, g, make_response, redirect, render_template, request,
                   session, url_for)

key = b'85m-3ExDEz2wCCNERphWTMVJH29tLn-TEa4DpyDRCWM='
cipher_suite = Fernet(key)

import json
import os

import app_config
from flask_session import Session

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True

app = Flask(__name__)
app.config.from_object(app_config) # load Flask configuration file (e.g., session configs)
app.secret_key = SECRET_KEY
Session(app) # init the serverside session for the app: this is requireddue to large cookie size


## NOTE -azure-ad Azure settings
adapter = FlaskContextAdapter(app)    # we are using flask
aad_configuration = AADConfig.parse_json('aad.config.json')
AADConfig.sanity_check_configs(aad_configuration)
azure_identity_web = IdentityWebPython(aad_configuration, adapter) # instantiate utils

source_url = None
@app.route('/')
@app.route('/sign_in')
def login_user():
    current_url = request.args.get('current_url')
    session['current_url'] = current_url
    return redirect(f'auth/sign_in?current_url={current_url}')

@app.route('/index/')
# @azure_identity_web.login_required
def index():
    if 'current_url' in session:
        current_url = session['current_url']
        identity_context_data = session['identity_context_data']
        identity_context_data = json.dumps(identity_context_data)

        # Encrypt the parameter
        encrypted_data = cipher_suite.encrypt(identity_context_data.encode()).decode()

        # Append the encrypted parameter to the URL
        url_with_param = f"{current_url}?identity_context_data={encrypted_data}"

        return redirect(url_with_param)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=DEBUG,)
