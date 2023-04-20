from flask import render_template, url_for, request
from fly_app import app
from fly_app.controllers import create_airport, get_all_airports, get_all_users, register_user, login_user, verify_user, create_flight, create_product, manage_flight, manage_product, manage_airport, get_all_flights, get_all_products, create_passenger, create_ticket, get_tickets, get_all_passengers, logout_user
from fly_app import helpers

@app.route('/')
def main_page():   
    all_flights = get_all_flights(request)
    all_tickets = get_tickets(request)
    all_passengers = get_all_passengers(request)
    return render_template('index.html', flights=all_flights, tickets=all_tickets, passengers=all_passengers)

@app.route('/account')
def account_page():
    return render_template('account.html')

@app.route('/admin')
@helpers.admin
def admin():
    all_users = get_all_users(request)
    all_airports = get_all_airports(request)
    all_flights = get_all_flights(request)
    all_products = get_all_products(request)
    return render_template('admin.html', airports=all_airports, flights=all_flights, products=all_products, users=all_users)

@app.route('/add_airport', methods=["POST"])
@helpers.admin
def add_airport():
    return create_airport(request)

@app.route('/manage_airports', methods=["GET", "DELETE"])
@helpers.admin
def manage_airports():
    return manage_airport(request)

@app.route('/registration', methods=["POST"])
def registration():
    return register_user(request)

@app.route('/login', methods=["POST"])
def login():
    return login_user(request)

@app.route('/logout')
def logout():
    return logout_user(request)

@app.route('/add_passenger', methods=["POST"])
@helpers.auth_required
def add_passenger():
    return create_passenger(request)

@app.route('/verifycation/<email>/<hash>')
def verify(email, hash):
    return verify_user(request, email, hash)

@app.route('/add_flight', methods=["GET", "POST"])
@helpers.admin
def add_flight():
    return create_flight(request)

@app.route('/get_flights', methods=["GET"])
def get_flights():
    return get_all_flights(request)

@app.route('/manage_flights', methods=["GET", "DELETE"])
@helpers.admin
def manage_flights():
    return manage_flight(request)

@app.route('/add_ticket', methods=["POST"])
def add_ticket():
    return create_ticket(request)

@app.route('/get_all_tickets')
def get_all_tickets():
    return get_tickets(request)

@app.route('/add_product', methods=["GET", "POST"])
@helpers.admin
def add_product():
    return create_product(request)

@app.route('/manage_products', methods=["GET", "DELETE"])
@helpers.admin
def manage_products():
    return manage_product(request)