'''
Minimal Flask application
--------------------------------
To run the application: flask --app hello run
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'