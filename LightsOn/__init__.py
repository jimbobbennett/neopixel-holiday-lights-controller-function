import sys
import os
sys.path.append(os.path.abspath(""))

import logging
import azure.functions as func
from ..Shared import api

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Turning lights on...')

    colour = req.params.get('colour')

    api.call_iot_central("On", {"request":colour})

    return func.HttpResponse(
        "Lights on.",
        status_code=200
    )
