from flask import render_template, url_for, request
from fly_app import app
from fly_app.controllers import create_airport, get_all_airports, get_all_users, register_user, login_user, verify_user


@app.route('/')
def main_page():
    all_airports = get_all_airports(request)
    all_users = get_all_users(request)
    return render_template('index.html', airports=all_airports, users=all_users)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/add_airport', methods=["POST"])
def add_airport():
    return create_airport(request)

@app.route('/registration', methods=["POST"])
def registration():
    return register_user(request)

@app.route('/login', methods=["POST"])
def login():
    return login_user(request)

@app.route('/verifycation/<email>/<hash>')
def verify(email, hash):
    return verify_user(request, email, hash)