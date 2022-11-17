#!/usr/bin/env python
# -*- coding: utf-8 -*-
from myapp import app
from flask import Flask ,render_template , flash, request, redirect, url_for

import myapp.controllers.loader_controller as loader_controller

@app.route('/')
def r_index_get():
    return render_template('main_blade.html' , title ="Main page" , body="Body")

@app.route('/upload' , methods=['GET'])
def r_upload_get():
    return render_template('upload.html')

@app.route('/upload' , methods=['POST'])
def r_upload_post():
    return loader_controller.upload_post(app,request)
