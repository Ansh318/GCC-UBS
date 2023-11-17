import json

from flask import Flask, make_response, request, jsonify

from solutions.coin_change import coin_change_solution
from solutions.data_encryption import data_encryption_solution
from solutions.file_reorganization import file_reorganization_solution
from solutions.fraudulent_transcations import fraudulent_transactions_solution
from solutions.mlmm import mlmm_program_solution
from solutions.portfolio_operations import portfolio_operations_solution
from solutions.profit_maximization import profit_maximization_solution
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
        return make_response(jsonify(my_dict), 200, headers)


@app.route("/profit-maximization", methods=['GET', 'POST'])
def profit_maximization():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON
    results = profit_maximization_solution(inputs)
    return make_response(jsonify(results), 200, headers)


@app.route("/file-reorganization", methods=['GET', 'POST'])
def file_reorganization():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON
    results = file_reorganization_solution(inputs)
    return make_response(jsonify(results), 200, headers)


@app.route("/portfolio-operations", methods=['GET', 'POST'])
def portfolio_operations():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = request.args.get('inputs')  # do some cleanup / conversion to as expected from JSON
    # Do Work
    results = portfolio_operations_solution(inputs)
    # Return Value
    return make_response(jsonify(results), 200, headers)


# noinspection SpellCheckingInspection
@app.route("/mlmm-program", methods=['GET', 'POST'])
def mlmm_program():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = json.loads(request.args.get('inputs'))  # do some cleanup / conversion to as expected from JSON
    results = mlmm_program_solution(inputs)
    return make_response(jsonify(results), 200, headers)


@app.route("/data-encryption", methods=['GET', 'POST'])
def data_encryption():
    # Setup
    headers = {"Content-Type": "application/json"}
    inputs = json.loads(request.args.get('inputs'))  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = data_encryption_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.route("/time-intervals", methods=['GET', 'POST'])
def time_intervals():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = json.loads(request.args.get('inputs'))  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = time_intervals_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.route("/fraudulent-transactions", methods=['GET', 'POST'])
def fraudulent_transactions():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = json.loads(request.args.get('inputs'))  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = fraudulent_transactions_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.route("/coin-change", methods=['GET', 'POST'])
def coin_change():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = json.loads(request.args.get('inputs'))  # do some cleanup / conversion to as expected from JSON
    # Do Work
    results = coin_change_solution(inputs)
    # Return Value
    return make_response(jsonify(results), 200, headers)


@app.route("/risk-mitigation", methods=['GET', 'POST'])
def risk_mitigation():
    # Set Up
    headers = {"Content-Type": "application/json"}
    inputs = json.loads(request.args.get('inputs'))  # do some cleanup / conversion to as expected from JSON

    # Do Work
    results = risk_mitigation_solution(inputs)

    # Return Value
    return make_response(jsonify(results), 200, headers)


