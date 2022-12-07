#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myapp import app
from flask import Flask ,render_template , flash, request, redirect, url_for

import myapp.controllers.loader_controller as loader_controller
import myapp.controllers.optimize_controller as optimize_controller

@app.route('/')
def r_index_get():
    return render_template('main_blade.html' , title ="Main page" , body="Body")

@app.route('/upload' , methods=['GET'])
def get_upload():
    return render_template('upload.html')

@app.route('/upload' , methods=['POST'])
def post_upload():
    return loader_controller.post_upload(app,request)

@app.route('/optimize' , methods=['GET'])
def get_optimize():
    return render_template('upload_from_site.html')

@app.route('/optimize' , methods=['POST'])
def post_optimize():
    return optimize_controller.post_upload_from_site(app,request)
