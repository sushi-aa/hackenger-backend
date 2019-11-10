from flask import flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def homepage():
	if not session.get('logged_in'):
		return render_template(' ')
	else:
		return "hello" <a hfref="/logout">Logout</a>""

@app.route('/login', methods=['POST'])
def admin_login():
	if request.form['password'] == ' ' and request.form['username'] == ' ':
		session['logged_in'] = True
	else:
		flash("incorrect password!")

	return home()

def logout():
	session['logged_in'] = False
	return home()



