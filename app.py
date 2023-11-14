from flask import Flask, make_response, request, jsonify


# Create Flask's `app` object
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    if request.method == 'GET':
        my_dict = {'key': 'dictionary value'}
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(my_dict), 200, headers)
    if request.method == 'POST':
        my_dict = {'key': request.data}
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(my_dict), 200, headers)