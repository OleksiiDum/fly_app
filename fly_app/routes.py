from flask import render_template, url_for, request, Blueprint
from fly_app import app
from fly_app.controllers import create_airport, get_all_passengers, delete_passenger, get_all_account_passengers, get_all_airports, get_all_users, register_user, login_user, verify_user, create_flight, manage_flight, manage_airport, get_all_flights, create_passenger, create_ticket, get_tickets, logout_user, get_user_info, is_admin, is_authenticated, get_needed_flight
from fly_app import helpers
from fly_app.nationalities import NATIONALITIES_list
from fly_app.forms import AddAirportForm, DeleteAirportForm, AddFlightForm, DeleteFlightForm, DeletePassengerForm


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
    form = AddAirportForm()
    form_2 = DeleteAirportForm()
    form_3 = AddFlightForm()
    form_4 = DeleteFlightForm()
    form_5 = DeletePassengerForm()
    if form_5.validate_on_submit():
        selected_account_id = int(form.user_account.data)
        form.set_passenger_choices(selected_account_id)
    users = get_all_users(request)
    passengers = get_all_passengers(request)
    return render_template('admin.html', form=form, form_2=form_2, form_3=form_3, form_4=form_4,form_5=form_5, users=users, passengers=passengers)


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

@airports_bp.route('/airports/manage', methods=["POST"])
@helpers.admin
def manage_airports():
    return manage_airport(request)

#Passengers

@passengers_bp.route('/passengers/add', methods=["POST"])
@helpers.auth_required
def add_passenger():
    return create_passenger(request)

@passengers_bp.route('/passengers/delete', methods=["POST"])
@helpers.auth_required
def delete_passenger():
    return delete_passenger(request)

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

@flights_bp.route('/get_flight', methods=["GET", "POST"]) #for JS request
def get_flight():
    return get_needed_flight(request)

@flights_bp.route('/flights/manage', methods=["POST"])
@helpers.admin
def manage_flights():
    return manage_flight(request)

@app.route('/add_ticket', methods=["POST"])
def add_ticket():
    return create_ticket(request)

@app.route('/get_all_tickets')
def get_all_tickets():
    return get_tickets(request)
