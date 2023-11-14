import flask
from flask import request, jsonify, redirect, url_for, Response

app = flask.Flask(__name__)
app.config['DEBUG'] = True

from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    print(app.name)
    if 'username' in session:

        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/guide', methods=["POST"])
def add_guide():
    title = request.json['title']
    content = request.json['content']
    return f'{title} is cool'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))