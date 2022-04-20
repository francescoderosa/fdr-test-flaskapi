from datetime import datetime
from re import M
from this import d
from commons.response import AppResponse

def ping():
    return AppResponse(200, "SUCCESS", 'pong').to_json()

def healthcheck(context={}):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return AppResponse(200, "SUCCESS", now).to_json()
