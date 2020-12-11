import sys
import os
sys.path.append(os.path.abspath(""))

import logging
import azure.functions as func
from ..Shared import api

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Turning lights off...')
    
    api.call_iot_central("Off", {})

    return func.HttpResponse(
        "Lights off.",
        status_code=200
    )
