from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World!</h1><hr>'


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name
