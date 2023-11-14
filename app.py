from flask import Flask, make_response, request, jsonify

# Create Flask's `app` object
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    headers = {"Content-Type": "application/json"}
    if request.method == 'GET':
        my_dict = {'key': 'dictionary value'}
        return make_response(jsonify(my_dict), 200, headers)
    if request.method == 'POST':
        my_dict = {'key': request.args.get('language')}
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(my_dict), 200, headers)


@app.post("/file-reorganization")
def file_reorganization():
    # Set Up
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/portfolio-operations")
def portfolio_operations():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/time-intervals")
def time_intervals():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/data-encryption")
def data_encryption():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/coin-change")
def coin_change():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/risk-mitigation")
def risk_mitigation():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)
