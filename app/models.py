from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    user_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float)
    comment = db.Column(db.String(255))
    cretaed_at = db.Column(db.DateTime, default=datetime.now(datetime.UTC), nullable=False)
            
