from azure_ad_web import IdentityWebPython
from azure_ad_web.adapters import FlaskContextAdapter
from azure_ad_web.configuration import AADConfig
from flask import (Flask, g, redirect, render_template, request, session,
                   url_for)

import app_config
from flask_session import Session
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')

app = Flask(__name__)
app.config.from_object(app_config) # load Flask configuration file (e.g., session configs)
app.secret_key = SECRET_KEY
Session(app) # init the serverside session for the app: this is requireddue to large cookie size


## NOTE -azure-ad Azure settings
adapter = FlaskContextAdapter(app)    # we are using flask
aad_configuration = AADConfig.parse_json('aad.config.json')
AADConfig.sanity_check_configs(aad_configuration)
azure_identity_web = IdentityWebPython(aad_configuration, adapter) # instantiate utils

@app.route('/')
@app.route('/sign_in_status')
def login_user():
    return render_template('azure_ad_api/login.html')

@app.route('/index/')
# @azure_identity_web.login_required
def index():
    return render_template('azure_ad_api/index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=DEBUG,)
