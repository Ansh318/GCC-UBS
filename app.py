from flask import Flask, make_response, request, jsonify
import backend
import json

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


@app.route("/file-reorganization", methods=['GET', 'POST'])
def file_reorganization():
    # Set Up
    headers = {"Content-Type": "application/json"}
    # Access the data sent in the POST request
    #data = request.json  Assuming the data is sent as JSON
    with open('sample_data.json', 'r') as json_file:
        data = json.load(json_file)
    my_dict = backend.max_palindrome_length(data)
    # Return Value
    return make_response(jsonify(my_dict), 200, headers)

@app.route("/portfolio-operations", methods=['GET', 'POST'])
def portfolio_operations():
    headers = {"Content-Type": "application/json"}
    #Access the data sent in the POST request
    #data = request.json  Assuming the data is sent as JSON
    with open('sample_data_2.json', 'r') as json_file:
        data = json.load(json_file)
    my_dict = backend.calculate_max_profit(data)
    # Return Value
    return make_response(jsonify(my_dict), 200, headers)

@app.route("/time-intervals",methods=['GET', 'POST'])
def time_intervals():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.route("/data-encryption", methods=['GET', 'POST'])
def data_encryption():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.route("/coin-change", methods=['GET', 'POST'])
def coin_change():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)


@app.route("/risk-mitigation", methods=['GET', 'POST'])
def risk_mitigation():
    headers = {"Content-Type": "application/json"}
    my_dict = {}

    # Do Work

    # Return Value
    return make_response(jsonify(my_dict), 200, headers)
