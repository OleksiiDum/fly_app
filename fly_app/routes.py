from flask import render_template, url_for, request
from fly_app import app
from fly_app.controllers import create_airport, get_all_airports, get_all_users, register_user, login_user, verify_user, create_flight, create_product, manage_flight, manage_product, manage_airport, get_all_flights, get_all_products, create_passenger, create_ticket


@app.route('/')
def main_page():
    all_airports = get_all_airports(request)
    all_users = get_all_users(request)
    all_flights = get_all_flights(request)
    return render_template('index.html', airports=all_airports, users=all_users, flights=all_flights)

@app.route('/admin')
def admin():
    all_airports = get_all_airports(request)
    all_flights = get_all_flights(request)
    all_products = get_all_products(request)
    return render_template('admin.html', airports=all_airports, flights=all_flights, products=all_products)

@app.route('/add_airport', methods=["POST"])
def add_airport():
    return create_airport(request)

@app.route('/manage_airports', methods=["GET", "DELETE"])
def manage_airports():
    return manage_airport(request)

@app.route('/registration', methods=["POST"])
def registration():
    return register_user(request)

@app.route('/login', methods=["POST"])
def login():
    return login_user(request)

@app.route('/add_passenger', methods=["POST"])
def add_passenger():
    return create_passenger(request)

@app.route('/verifycation/<email>/<hash>')
def verify(email, hash):
    return verify_user(request, email, hash)

@app.route('/add_flight', methods=["GET", "POST"])
def add_flight():
    return create_flight(request)

@app.route('/get_flights', methods=["GET"])
def get_flights():
    return get_all_flights(request)

@app.route('/manage_flights', methods=["GET", "DELETE"])
def manage_flights():
    return manage_flight(request)

@app.route('/add_ticket', methods=["POST"])
def add_ticket():
    return create_ticket(request)

@app.route('/add_product', methods=["GET", "POST"])
def add_product():
    return create_product(request)

@app.route('/manage_products', methods=["GET", "DELETE"])
def manage_products():
    return manage_product(request)