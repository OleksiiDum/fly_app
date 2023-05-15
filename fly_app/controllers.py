from fly_app.models import  Airport, Flight, Product, Ticket, Account, Authcode, Passanger
from fly_app import db
import fly_app.helpers as helpers
from flask import render_template, url_for, session, redirect, jsonify
from fly_app.send_mail import Mailer


#AIRPORT
def create_airport(request):
    if request.method == "POST":
        country = request.form.get("country")
        city = request.form.get("city")
        airport_name = request.form.get("airport_name")
        timezone = request.form.get("timezone")
        airport = Airport(country=country, city=city, airport_name=airport_name, timezone=timezone)
        db.session.add(airport)
        db.session.commit()
        return redirect(url_for('admin'))

def manage_airport(request):
    if request.method == "DELETE":
        airport_id = request.form.get('id')
        airport_to_delete = Airport.query.filter_by(id=airport_id).first()
        db.session.delete(airport_to_delete)
        db.session.commit()
        return redirect(url_for('admin'))
    elif request.method == "GET":
        airport_id = request.form.get('id')
        airport = Airport.query.filter_by(id=airport_id).first()
        return jsonify({"airport": airport})

def get_all_airports(request):
    if request.method == "GET":
        all_airports = Airport.query.all()
        return jsonify(all_airports)

#USER
def get_all_users(request):
    if request.method == "GET":
        all_users = Account.query.all()
        return all_users

def login_user(request):
    if request.method == "POST":
        email = request.form["email"]
        user_password = request.form["password"]
        db_user = Account.query.filter_by(email=email).first()
        if db_user:
            if email == 'admin@mail.com':
                if helpers.hashed(user_password) == db_user.password:
                    session["admin"] = True
            if helpers.hashed(user_password) == db_user.password:
                session['email']  = db_user.email
                return jsonify({"OK": True})
            else:
                return jsonify({"OK": False, "Status": "password incorrect"})
        else:
            return jsonify({"OK": False, "Status": "user not found"})
        

def logout_user(request):
    session.clear()
    return render_template('index.html')

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
    return jsonify({"message": "OK"})

def verify_user(request, email, hash):
    user = Account.query.filter_by(email=email).first()
    code = Authcode.query.filter_by(userid = user.id).first().code
    if hash == code:
        user.verified = True
        db.session.add(user)
        db.session.commit()
        return "Verified"
    else:
        return "Error"

#PASSENGER
def create_passenger(request):
    if  request.method == "POST":
        first_name = request.form.get('first')
        last_name = request.form.get('last')
        nationality = request.form.get('nationality')
        passport = request.form.get('passport')
        age = request.form.get('age')
        account_id = Account.query.filter_by(email=session["email"]).first().id
        passenger = Passanger(first_name=first_name, last_name=last_name, nationality=nationality, passport=passport, age=age, account_id=account_id)
        db.session.add(passenger)
        db.session.commit()
        return "Done"
    else:
        return "Wrong method"

def get_all_passengers(request):
    if request.method  == "GET":
        passengers = Passanger.query.all()
        return passengers
    else:
        return "Wrong method"

#FLIGHT
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
        return redirect(url_for('admin'))
    else:
        return "Wrong Request Method"
    
def get_all_flights(request):
    if request.method =="GET":
        flights = Flight.query.all()
        return flights
    
def manage_flight(request):
    if  request.method == "DELETE":
        flight_to_delete = Flight.query.filter_by(id=request.form.get('id')).first()
        db.session.delete(flight_to_delete)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        pass

#TICKET   
def create_ticket(request):
    passenger = request.passenger
    flight = request.flight
    seat = request.seat
    baggage = request.baggage or 0
    ticket = Ticket(passenger=passenger, flight=flight, seat=seat, baggage = baggage)
    db.session.add(ticket)
    db.session.commit()
    return "Done"

def get_tickets(request):
    if request.method == "GET":
        tickets = Ticket.query.all()
        return tickets


#PRODUCT
def create_product(request):
    if request.method == "POST":
        product_name = request.form.get('product-name')
        description = request.form.get('description')
        price = request.form.get('price')
        product = Product(product_name=product_name, description=description, price=price)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        pass

def get_all_products(request):
    if request.method == "GET":
        products = Product.query.all()
        return products
    
def manage_product(request):
    if  request.method == "DELETE":
        product_to_delete = Product.query.filter_by(id=request.form.get('id')).first()
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect(url_for('admin'))
    else:
        pass
