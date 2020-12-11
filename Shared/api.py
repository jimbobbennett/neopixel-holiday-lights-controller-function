import logging
import os
import requests

url_root = os.environ['IOT_CENTRAL_APP_URL_ROOT']
api_key = os.environ['API_KEY']
interface_identity = os.environ['INTERFACE_IDENTITY_NAME']

command_root = "https://" + url_root + ".azureiotcentral.com/api/preview/devices/neopixel/components/" +  interface_identity + "/commands/"

def call_iot_central(command, body):
    r = requests.post(command_root + command, json = body, params = {"access_token": api_key})

    logging.info(r)
    logging.info(r.content)