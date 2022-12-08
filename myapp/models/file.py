from myapp import db
from sqlalchemy.sql import func
#from myapp.models.parse_seanse import Parse_seanse

class File(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    path = db.Column(db.String(300),nullable=False)
    name = db.Column(db.String(64), nullable=False)
    extenstion = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') ,nullable=True)
    parse_seanse_id = db.Column(db.Integer, db.ForeignKey('parse_seanse.id') ,nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    



