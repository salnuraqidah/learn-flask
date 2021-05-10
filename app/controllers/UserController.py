from app import app
from flask import redirect, url_for, request, jsonify
import os
from werkzeug.utils import secure_filename

class User:

    ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png', 'svg'}

    def index(self):
        return "ini index"
        # return redirect(url_for("static", filename="index.html"))


    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".",1)[1].lower() in self.ALLOWED_EXTENSIONS

    def upload(self):
        UPLOAD_FOLDER = "./app/static/upload/"
        app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
        if "image" not in request.files:
            return {"message" : "no selected file"}, 400
        image = request.files['image']
        if self.allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return {"message" : "success"}, 201
        else:
            return {"message" : {"type" : list(self.ALLOWED_EXTENSIONS)}}, 415
    
    def update(self, id):
        return {
            "message" : f"update by id {id}"
        }, 200
    
    def delete(self, id):
        return {
            "message" : f"delete by id {id}"
        }, 200
    
    def get_by_id(self, id):
        return {
            "message" : f"get by id {id}"
        }, 200