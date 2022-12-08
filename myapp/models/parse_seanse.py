from myapp import db
from sqlalchemy.sql import func

class Parse_seanse(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') ,nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    



