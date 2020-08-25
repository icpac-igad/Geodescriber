"""The Geodescriber ANALYSIS API MODULE"""
import CTRegisterMicroserviceFlask
import ee
import logging
import os
from flask import Flask
from oauth2client.service_account import ServiceAccountCredentials
from geodescriber.config import SETTINGS
from geodescriber.routes.api import error
from geodescriber.routes.api.v1 import geodescriber_endpoints_v1
from geodescriber.utils.files import load_config_json
from dotenv import load_dotenv
from geodescriber.utils.files import BASE_DIR, PROJECT_DIR

dotenv_path = os.path.join(BASE_DIR, '.env')

load_dotenv(dotenv_path=dotenv_path)

logging.basicConfig(
    level=SETTINGS.get('logging', {}).get('level'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)

# Initilizing GEE
gee = SETTINGS.get('gee')
ee_user = gee.get('service_account')
private_key_file = gee.get('privatekey_file')
if private_key_file:
    logging.info(f'Initilizing EE with privatekey.json credential file: {ee_user} | {private_key_file}')
    credentials = ee.ServiceAccountCredentials(ee_user, private_key_file)
    ee.Initialize(credentials)
    ee.data.setDeadline(60000)
else:
    raise ValueError("privatekey.json file not found. Unable to authenticate EE.")

# Flask App
app = Flask(__name__)

# Routing
app.register_blueprint(geodescriber_endpoints_v1, url_prefix="/api/v1/geodescriber")

# CT
info = load_config_json('register')
swagger = load_config_json('swagger')
CTRegisterMicroserviceFlask.register(
    app=app,
    name='geodescriber',
    info=info,
    swagger=swagger,
    mode=CTRegisterMicroserviceFlask.AUTOREGISTER_MODE if os.getenv('CT_REGISTER_MODE') and os.getenv(
        'CT_REGISTER_MODE') == 'auto' else CTRegisterMicroserviceFlask.NORMAL_MODE,
    ct_url=os.getenv('CT_URL'),
    url=os.getenv('LOCAL_URL')
)


@app.errorhandler(403)
def forbidden(e):
    return error(status=403, detail='Forbidden')


@app.errorhandler(404)
def page_not_found(e):
    return error(status=404, detail='Not Found')


@app.errorhandler(405)
def method_not_allowed(e):
    return error(status=405, detail='Method Not Allowed')


@app.errorhandler(410)
def gone(e):
    return error(status=410, detail='Gone')


@app.errorhandler(500)
def internal_server_error(e):
    return error(status=500, detail='Internal Server Error')
