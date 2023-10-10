from flask import render_template, url_for, request, Blueprint
from fly_app import app
from fly_app.controllers import create_airport, get_all_account_passengers, get_all_airports, get_all_users, register_user, login_user, verify_user, create_flight, create_product, manage_flight, manage_product, manage_airport, get_all_flights, get_all_products, create_passenger, create_ticket, get_tickets, logout_user, get_user_info, is_admin, is_authenticated, get_needed_flight
from fly_app import helpers
from fly_app.nationalities import NATIONALITIES_list


airports_bp = Blueprint('airports_bp', __name__)
passengers_bp = Blueprint('passengers_bp', __name__)
flights_bp = Blueprint('flights_bp', __name__)

@app.route('/')
def main_page():
    return render_template("index.html")
    
@app.route('/registration_page')
def registration_page():
    return render_template("register.html")

@app.route('/login_page')
def login_page():
    return render_template("login.html")

@app.route('/account_page')
def account_page():
    if is_authenticated:
        all_passengers = get_all_account_passengers(request)
        nationalities = NATIONALITIES_list
        return render_template('account.html', passengers=all_passengers, nationalities=nationalities)
    else:
        return url_for('login_page')

@app.route('/admin_page')
@helpers.admin
def admin_page():
    all_users = get_all_users(request)
    all_airports = get_all_airports(request)
    all_flights = get_all_flights(request)
    all_products = get_all_products(request)
    return render_template('admin.html', airports=all_airports, flights=all_flights, products=all_products, users=all_users)


@app.route('/register', methods=["POST"])
def register():
    return register_user(request)

@app.route('/login', methods=["POST"])
def login():
    return login_user(request)

@app.route('/logout')
def logout():
    return logout_user(request)

@app.route('/user_info/')
def user_info():
    return get_user_info()

@app.route('/verifycation/<email>/<hash>')
def verify(email, hash):
    return verify_user(request, email, hash)

#Airports

@airports_bp.route('/airports', methods=["GET"])
def all_airports():
    return get_all_airports(request)

@airports_bp.route('/airports/add', methods=["POST"])
@helpers.admin
def add_airport():
    return create_airport(request)

@airports_bp.route('/airports/manage', methods=["GET", "DELETE"])
@helpers.admin
def manage_airports():
    return manage_airport(request)

#Passengers

@passengers_bp.route('/passengers/add', methods=["POST"])
@helpers.auth_required
def add_passenger():
    return create_passenger(request)

@passengers_bp.route('/passengers/get_account', methods=["GET", "POST"])
def get_passengers_by_id():
    return get_all_account_passengers(request)

#Flights

@flights_bp.route('/flights/add', methods=["GET", "POST"])
@helpers.admin
def add_flight():
    return create_flight(request)

@flights_bp.route('/flights', methods=["GET"])
def get_flights():
    return get_all_flights(request)

@flights_bp.route('/flights/<id>', methods=["GET", "POST"])
def get_flight():
    return get_needed_flight(request)

@flights_bp.route('/flights/manage', methods=["GET", "DELETE"])
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