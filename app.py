import json

from flask import Flask, make_response, request, jsonify

from solutions.file_reorganization import file_reorganization_solution

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    headers = {"Content-Type": "application/json"}
    if request.method == 'GET':
        my_dict = {'key': 'dictionary value'}
        return make_response(jsonify(my_dict), 200, headers)
    if request.method == 'POST':
        my_dict = {'key': request.args.get('language')}
        return make_response(jsonify(my_dict), 200, headers)


@app.post("/file-reorganization")
def file_reorganization():
    # Set Up
    headers = {"Content-Type": "application/json"}
    """
    POST -> { "inputs" : ["coding", "its harder to read code than to write it"] }
    request.args.get('inputs') yields value 
    """
    inputs = json.loads(request.args.get('inputs'))  # do some cleanup / conversion to as expected from JSON

    # Do Work
    # results = file_reorganization_solution(inputs)
    my_dict = {"inputs": inputs}
    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/portfolio-operations")
def portfolio_operations():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = file_reorganization_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.post("/time-intervals")
def time_intervals():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = file_reorganization_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.post("/data-encryption")
def data_encryption():
    # Setup
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = file_reorganization_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.post("/coin-change")
def coin_change():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = file_reorganization_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.post("/risk-mitigation")
def risk_mitigation():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = file_reorganization_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)
