from fly_app.models import  Airport, Flight, Product, Ticket, Account, Authcode, Passanger
from fly_app import db
import fly_app.helpers as helpers
from flask import render_template, flash, Response, url_for
from fly_app.send_mail import Mailer



# Geolocation and Path
# geolocator = Nominatim(user_agent="MyApp")

# kyiv_location = geolocator.geocode("Kyiv")
# berlin_location = geolocator.geocode("Berlin")

# path = distance((kyiv_location.latitude, kyiv_location.longitude), (berlin_location.latitude, berlin_location.longitude))

# #Price
# base_price = path * 0.25


#DB
def create_airport(request):
    if request.method == "POST":
        country = request.form.get("country")
        city = request.form.get("city")
        airport_name = request.form.get("airport_name")
        timezone = request.form.get("timezone")
        
        airport = Airport(country=country, city=city, airport_name=airport_name, timezone=timezone)
        db.session.add(airport)
        db.session.commit()
    return "Done"

def manage_airport(request):
    airport_id = request.form.get('id')
    if request.method == "GET":
        airport = Airport.query.filter_by(id=airport_id).first()
        return airport
    elif request.method == "DELETE":
        airport_to_delete = Airport.query.filter_by(id=airport_id).first()
        db.session.delete(airport_to_delete)
        db.session.commit()
        return "Deleted"
    else:
        return "Wrong method"

def get_all_airports(request):
    if request.method == "GET":
        all_airports = Airport.query.all()
        return all_airports

def get_all_users(request):
    if request.method == "GET":
        all_users = Account.query.all()
        return all_users

# login controller
def login_user(request):
    print("Login")
    if request.method == "POST":
        email = request.form["email"]
        user_password = request.form["password"]
        db_user = Account.query.filter_by(email=email).first()
        print(db_user)
        if db_user:
            print("Ok")
            if helpers.hashed(user_password) == db_user.password:
                return render_template('index.html')
            else:
                print("password")
                return "password incorrect"
        else:
            print("user")
            return "User not found"

# registration controller
def register_user(request):
    if request.method == "POST":
        users = Account.query.all()
        email = request.form.get("email")
        password = request.form.get("password")
        if not email in users:
            user = Account(email=email, password=helpers.hashed(password))
            hash = helpers.randome_code()
            db.session.add(user)
            db.session.commit()
            authcode = Authcode(code=hash, userid = user.id)
            db.session.add(authcode)
            db.session.commit()
            url = url_for('verify', email=email, hash=hash)
            Mailer(user.email, url, 'Test').send_text_mail()
    return "Done"

def verify_user(request, email, hash):
    user = Account.query.filter_by(email=email).first()
    code = Authcode.query.filter_by(userid = user.id).first().code
    print(type(hash))
    print(type(code))
    print(hash)
    print(code)
    if hash == code:
        user.verified = True
        db.session.add(user)
        db.session.commit()
        return "Verified"
    else:
        return "Error"

def create_passenger(request):
    if  request.method == "POST":
        first_name = request.form.get('first')
        last_name = request.form.get('last')
        nationality = request.form.get('nationality')
        passport = request.form.get('passport')
        age = request.form.get('age')
        passenger = Passanger(first_name==first_name, last_name=last_name, nationality=nationality, passport=passport, age=age)
        db.session.add(passenger)
        db.session.commit()
        return "Done"
    else:
        return "Wrong method"

def create_flight(request):
    if  request.method == "POST":
        from_airport = request.form.get('from-airport')
        to_airport = request.form.get('to-airport')
        departure = request.form.get('dep-time')
        arrivals = request.form.get('arr-time')
        flight = Flight(from_airport=from_airport, to_airport=to_airport, departure_time=departure, arrivals_time=arrivals)
        db.session.add(flight)
        db.session.commit()
        for seat, type in helpers.generate_seats():
            ticket = Ticket(flight=flight.id, seat=seat, type=type)
            db.session.add(ticket)
        db.session.commit()
        return "Done"
    else:
        return "Wrong Request Method"
    
def get_all_flights(request):
    if request.method =="GET":
        flights = Flight.query.all()
        return flights
    
def manage_flight(request):
    if request.method == "GET":
        flight = Flight.query.filter_by(id=request.form.get('id')).first()
        return flight
    elif request.method == "DELETE":
        flight_to_delete = Flight.query.filter_by(id=request.form.get('id')).first()
        db.session.delete(flight_to_delete)
        db.session.commit()
        return "Deleted"
    else:
        return "Wrong Request Method"
    
def create_ticket(request):
    passenger = request.passenger
    flight = request.flight
    price = 100
    seat = request.seat
    baggage = request.baggage or 0
    ticket = Ticket(passenger=passenger, flight=flight, price=price, seat=seat, baggage = baggage)
    db.session.add(ticket)
    db.session.commit()
    return "Done"

def create_product(request):
    if request.method == "POST":
        product_name = request.form.get('product-name')
        description = request.form.get('description')
        price = request.form.get('price')
        product = Product(product_name=product_name, description=description, price=price)
        db.session.add(product)
        db.session.commit()
        return "Done"
    else:
        return "Wrong Request Method"

def get_all_products(request):
    if request.method == "GET":
        products = Product.query.all()
        return products
    
def manage_product(request):
    if request.method =="GET":
        product = Product.query.filter_by(id=request.form.get('id')).first()
        return product
    elif request.method == "DELETE":
        product_to_delete = Product.query.filter_by(id=request.form.get('id')).first()
        db.session.delete(product_to_delete)
        db.session.commit()
        return "Deleted"
    else:
        return "Wrong Request Method"
