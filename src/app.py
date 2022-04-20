from controllers import api_status
from commons.response import AppResponse

from flask import Flask
app = Flask(__name__)

@app.route('/ping', methods=['GET', 'HEAD'])
def ping():
    r = api_status.ping()
    return r

@app.route('/healthcheck', methods=['GET', 'HEAD'])
def healthcheck():
    r = api_status.healthcheck()
    return r

@app.route("/", methods=['GET', 'HEAD'])
def hello():
    ret = {
        "message": "Hello World!"
    }
    return AppResponse(200, "SUCCESS", ret).to_json()

if __name__ == "__main__":
    app.run(host='0.0.0.0')