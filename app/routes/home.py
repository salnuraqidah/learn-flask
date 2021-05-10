from app import app
from flask import redirect, url_for, request, jsonify
from app.controllers.UserController import User
# import os
# from werkzeug.utils import secure_filename
user = User() 
@app.route('/user', methods=['GET', 'POST'])
def user_route():
    if request.method == 'GET':
        return user.index()
    if request.method == 'POST':
        return user.upload()

@app.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
def user_route_id(id):
    if request.method == "GET":
        return user.get_by_id(id)
    elif request.method == "PUT":
        return user.update(id)
    elif request.method == "DELETE":
        return user.delete(id)



# @app.route('/')
# def hello():
#     return ('Hai Semua!!!')

# @app.route('/greet/<username>')
# def greet(username):
#     return f'Hello, {username}!'

# @app.route('/greet/<username>', methods=['PUT', 'POST'])
# def greets(username):
#     return f'Hello, {username}, ini method PUT atau POST!'

# @app.route('/about')
# def about():
#     return "ABOUT PAGE"

# @app.route('/contact/')
# def contact():
#     return "CONTACT PAGE"

# @app.route("/user", methods=["POST"])
# def user():
#     # return request.json #return dict
#     # return request.form # return dict
#     # return "User"

#     name = request.json["name"]
#     data = dict()
#     data["name"] = name
#     data["message"] = "Success!"
#     return data, 201, {"authors" : "sal"}

# ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png', 'svg'}
# def allowed_file(filename):
#     return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['POST'])
# def upload():
#     UPLOAD_FOLDER = "./app/static/upload/"
#     app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
#     if "image" not in request.files:
#         return {"message" : "no selected file"}, 400
#     image = request.files['image']
#     if allowed_file(image.filename):
#         filename = secure_filename(image.filename)
#         image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return {"message" : "success"}, 201
#     else:
#         return {"message" : {"type" : list(ALLOWED_EXTENSIONS)}}, 415