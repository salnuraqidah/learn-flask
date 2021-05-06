from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hai Semua!!!')

@app.route('/greet/<username>')
def greet(username):
    return f'Hello, {username}!'

@app.route('/greet/<username>', methods=['PUT', 'POST'])
def greets(username):
    return f'Hello, {username}, ini method PUT atau POST!'

@app.route('/about')
def about():
    return "ABOUT PAGE"

@app.route('/contact/')
def contact():
    return "CONTACT PAGE"