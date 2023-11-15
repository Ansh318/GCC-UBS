from flask import Flask, make_response, request, jsonify

from solutions.coin_change import coin_change_solution
from solutions.data_encryption import data_encryption_solution
from solutions.file_reorganization import file_reorganization_solution
from solutions.portfolio_operations import portfolio_operations_solution
from solutions.risk_mitigation import risk_mitigation_solution
from solutions.time_intervals import time_intervals_solution

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
    result = file_reorganization_solution()

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/portfolio-operations")
def portfolio_operations():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work
    result = portfolio_operations_solution()

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/time-intervals")
def time_intervals():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work
    result = time_intervals_solution()

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/data-encryption")
def data_encryption():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work
    result = data_encryption_solution()

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/coin-change")
def coin_change():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work
    result = coin_change_solution()

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.post("/risk-mitigation")
def risk_mitigation():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work
    result = risk_mitigation_solution()

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)
