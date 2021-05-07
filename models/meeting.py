from typing import Optional
from datetime import datetime

from app import db


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meeting_creator = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    max_bikers = db.Column(db.Integer, nullable=True, default=None) #  None if no limit
    area = db.Column(db.String(256), nullable=False)
    trail = db.Column(db.String(256), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    min_skill = db.Column(db.Integer, nullable=True, default=0)
