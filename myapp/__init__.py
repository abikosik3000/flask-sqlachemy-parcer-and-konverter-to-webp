#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask , render_template
app = Flask(__name__)

import myapp.routes

@app.route('/test')
def index2():
    return render_template('test.html')

#if __name__ == '__main__':
    #app.run(debug=True,host='0.0.0.0')#,