# Run as - Python3 app.py to enable the debug mode

from flask import Flask, json

# debug errors & analyse the performance of application
import logging

# 5 Standard levels indicating the severity of log events.
## DEBUG - logger.debug()
## INFO - logger.info()
## WARNING - logger.warning()
## ERROR - logger.error()
## CRITICAL - logger.critical()

app = Flask(__name__)


@app.route('/status')
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    # log line - logger to log messages
    app.logger.info('Status request successfull')
    return response


@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    # log line
    app.logger.info('Metrics request successfull')
    return response


@app.route("/")
def hello():
    # log line
    app.logger.info('Main request successfull')

    return "Hello World!"


if __name__ == "__main__":

    # stream logs to app.log file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0', debug=True)
