import os

from myapp import app


basedir = os.path.abspath(os.path.dirname(__file__))
app.config["BASEDIR"] = basedir

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = os.path.join(basedir, 'uploads') #os.path.dirname(__file__)+
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

# sqlalhemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

# WTF forms
CSRF_ENABLED = False
SECRET_KEY = 'gdshsdfgh1rfwas'
app.config['CSRF_ENABLED'] = CSRF_ENABLED 
app.config['SECRET_KEY'] = SECRET_KEY 