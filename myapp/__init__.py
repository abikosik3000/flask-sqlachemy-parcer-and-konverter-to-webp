#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask , render_template
import os
app = Flask(__name__)

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = os.path.dirname(__file__)+"/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

import myapp.routes


#
#if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0')#,