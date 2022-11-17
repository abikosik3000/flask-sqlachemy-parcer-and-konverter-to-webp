#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template
from myapp import app

@app.route('/')
def index():
    return render_template('main_blade.html' , title ="Main page" , body="Bodyy")