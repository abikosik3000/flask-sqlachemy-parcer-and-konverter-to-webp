#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__ , static_url_path='', static_folder='uploads/')


app.secret_key = os.urandom(24)

import myapp.config
db.init_app(app)
import myapp.routes



#
#if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0')#,