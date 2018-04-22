from common import db

from datetime import datetime

class FacebookCredential(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	username = db.Column(db.String(4096))
	password = db.Column(db.String(4096))

	logged_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
