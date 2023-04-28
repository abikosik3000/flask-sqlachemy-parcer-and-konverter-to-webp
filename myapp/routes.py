from flask import render_template, request, send_from_directory
from flask_login import login_required

from myapp import app
import myapp.controllers.optimize_controller as optimize_controller
import myapp.controllers.login_controller as login_controller
import myapp.controllers.cabinet_controller as cabinet_controller


@app.route("/cabinet", methods=["GET"])
@login_required
def get_cabinet():
    return cabinet_controller.get_cabinet(app, request)


@app.route("/")
def get_main():
    return render_template("main.html")


@app.route("/optimize", methods=["GET"])
def get_optimize():
    return optimize_controller.get_upload_from_site(app, request)


@app.route("/optimize", methods=["POST"])
def post_optimize():
    return optimize_controller.post_upload_from_site(app, request)


"""
LOGIN PATH
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    return login_controller.login(app, request)


@app.route("/register", methods=["GET", "POST"])
def register():
    return login_controller.register(app, request)


@app.route("/logout")
@login_required
def logout():
    return login_controller.logout(app, request)


"""
OTHER PATH
"""


@app.route("/shutdown", methods=["GET"])
def shutdown():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()
    return "Server shutting down..."


@app.route("/uploads/<path:name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


"""
@app.route('/upload' , methods=['GET'])
def get_upload():
    return render_template('upload.html')

@app.route('/upload' , methods=['POST'])
def post_upload():
    return loader_controller.post_upload(app,request)
"""
