#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myapp import app , db
from flask import Flask ,render_template , flash, request, redirect, url_for , send_from_directory

import myapp.controllers.loader_controller as loader_controller
import myapp.controllers.optimize_controller as optimize_controller
from myapp.forms.login import LoginForm

from myapp.models.user import User


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for login')
        return redirect(url_for('get_main'))
    return render_template('login_form.html', form = form)

@app.route('/')
def get_main():
    return render_template('main.html' )

@app.route('/upload' , methods=['GET'])
def get_upload():
    return render_template('upload.html')

@app.route('/upload' , methods=['POST'])
def post_upload():
    return loader_controller.post_upload(app,request)

@app.route('/uploads/<path:name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/optimize' , methods=['GET'])
def get_optimize():
    return optimize_controller.get_upload_from_site(app,request)
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return 'Server shutting down...'

@app.route('/optimize' , methods=['POST'])
def post_optimize():
    return optimize_controller.post_upload_from_site(app,request)
