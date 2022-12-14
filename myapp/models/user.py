from myapp import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash,  check_password_hash
from flask_login import UserMixin
from myapp import login_manager

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), nullable=False, unique = True)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return '<User %r>' % (self.email)

    def check_password(self,  _password):
	    return check_password_hash(self.password, _password)

    def set_password(self, _password):
	    self.password = generate_password_hash(_password)
    

    
    
