from myapp import db
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), nullable=False, unique = True)
    password = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return '<User %r>' % (self.email)
