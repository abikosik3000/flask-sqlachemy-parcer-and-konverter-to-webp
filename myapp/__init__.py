#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

app = Flask(__name__ , static_url_path='', static_folder='uploads/')


app.secret_key = os.urandom(24)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

import myapp.config
db.init_app(app)
import myapp.routes



#
#if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0')#,