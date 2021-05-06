from app import app
from flask import request

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

@app.route("/user", methods=["POST"])
def user():
    # return request.json #return dict
    # return request.form # return dict
    # return "User"

    name = request.json["name"]
    data = dict()
    data["name"] = name
    data["message"] = "Success!"
    return data, 201, {"authors" : "sal"}