from myapp import app
import os

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = os.path.dirname(__file__)+"/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

#sqlalhemy
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
#app.config["SQLALCHEMY_MIGRATE_REPO"] = SQLALCHEMY_MIGRATE_REPO 

#WTF forms
CSRF_ENABLED = False
SECRET_KEY = 'gdshsdfgh1rfwas'
app.config['CSRF_ENABLED'] = CSRF_ENABLED 
app.config['SECRET_KEY'] = SECRET_KEY 