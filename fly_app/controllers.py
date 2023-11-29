from fly_app.models import  Airport, Flight, Ticket, Account, Authcode, Passanger
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
        airport = Airport(country=country, city=city, airport_name=airport_name)
        db.session.add(airport)
        db.session.commit()
        return redirect(url_for('admin_page'))

def manage_airport(request):
    if request.method == "POST":
        airport_id = int(request.form['airport'])
        airport_to_delete = Airport.query.filter_by(id=airport_id).first()
        db.session.delete(airport_to_delete)
        db.session.commit()
        return redirect(url_for('admin_page'))

def manage_flight(request):
    if  request.method == "POST":
        flight_id = int(request.form['flight'])
        flight_to_delete = Flight.query.filter_by(id=flight_id).first()
        db.session.delete(flight_to_delete)
        db.session.commit()
        return redirect(url_for('admin_page'))

def get_all_airports(request):
    if request.method == "GET":
        all_airports = Airport.query.all()
        airports_dict = []
        if all_airports:
            for airport in all_airports:
                airports_dict.append({"id": airport.id, "city": airport.city, "country": airport.country})
            print(airports_dict)    
            return jsonify(airports_dict)
        else:
            return[]

#USER
def get_all_users(request):
    if request.method == "GET":
        all_users = Account.query.all()
        return all_users

def get_all_passengers(request):
    if request.method == "GET":
        all_passengers = Passanger.query.all()
        return all_passengers

def is_admin():
    if session["admin"] == True:
        return True
    else:
        return False

def is_authenticated():
    if session['email']:
        return True
    else:
        return False

def delete_user(email):
    user = Account.query.filter_by(email=email).first()
    session.delete(user)
    session.commit()

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
                return jsonify({"status": True})
            else:
                return jsonify({"status": False, "message": "password incorrect"})
        else:
            return jsonify({"status": False, "message": "user not found"})
    else:
        return  jsonify({"message": "Wrong method"})

def logout_user(request):
    session.clear()
    return render_template('index.html')

def get_user_info():
    email = session.get("email")
    user = Account.query.filter_by(email=email).first()
    if not user:
        return jsonify({"message": "Not valid Request"})
    passengers = get_users_passengers(user.id)
    user_info = {"user": user.email, "passengers": passengers}
    return jsonify(user_info)

# registration controller
def register_user(request):
    if request.method == "POST":
        user = Account.query.filter_by(email=request.form.get("email")).first()
        email = request.form.get("email")
        password = request.form.get("password")
        if user:
            return jsonify({"message": "User exists"})
        else:
            new_user = Account(email=email, password=helpers.hashed(password))
            randcode = helpers.randome_code()
            db.session.add(new_user)
            db.session.commit()
            authcode = Authcode(code=randcode, userid=new_user.id)
            db.session.add(authcode)
            db.session.commit()
            url = url_for('verify', email=email, hash=randcode)
            Mailer(new_user.email, url, 'Test').send_text_mail()
    else:
        return  jsonify({"message": "Wrong method"})
    return jsonify({"message": "OK"})

def verify_user(request, email, randcode):
    user = Account.query.filter_by(email=email).first()
    code = Authcode.query.filter_by(userid = user.id).first().code
    if randcode == code:
        user.verified = True
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Verified"})
    else:
        return jsonify({"message": "Error"})

#PASSENGER
def create_passenger(request):
    if  request.method == "POST":
        first_name = request.form.get('first')
        last_name = request.form.get('last')
        nationality = request.form.get('nationality')
        passport = request.form.get('passport')
        age = request.form.get('age')
        email = session["email"]
        account_id = Account.query.filter_by(email=email).first().id
        passenger = Passanger(first_name=first_name, last_name=last_name, nationality=nationality, passport=passport, age=age, account_id=account_id)
        db.session.add(passenger)
        db.session.commit()
        passengers = get_users_passengers(account_id)
        return  jsonify(passengers)
    else:
        return  jsonify({"message": "Wrong method"})

def delete_passenger(request):
    if  request.method == "POST":
        id = request.form.get("id")
        passenger = Account.query.filter_by(id=id).first()
        session.delete(passenger)
        session.commit()

def get_all_account_passengers(request):
    if request.method  == "GET":
        email = session.get("email")
        id = Account.query.filter_by(email=email).first()
        passengers = get_users_passengers(id)
        return jsonify(passengers)
    else:
        return jsonify({"message": "Wrong method"})

def get_users_passengers(id):
    passengers = Passanger.query.filter_by(account_id=id)
    result = []
    for passenger in passengers:
        result.append({
            "id": passenger.id,
            "first_name": passenger.first_name,
            "last_name": passenger.last_name,
            "nationality": passenger.nationality,
            "passport": passenger.passport,
            "age": passenger.age
        })
    return result

#FLIGHT
def create_flight(request):
    if  request.method == "POST":
        from_airport = request.form.get('from_airport')
        to_airport = request.form.get('to_airport')
        departure = request.form.get('dep_time')
        arrivals = request.form.get('arr_time')
        price = request.form.get('price')
        flight = Flight(from_airport=from_airport, to_airport=to_airport, departure_time=departure, arrivals_time=arrivals, standard_price=price)
        db.session.add(flight)
        db.session.commit()
        for seat, type in helpers.generate_seats():
            ticket = Ticket(flight=flight.id, seat=seat, type=type)
            db.session.add(ticket)
        db.session.commit()
        return redirect(url_for('admin_page'))
    else:
        return jsonify({"message": "Wrong method"})
    
def get_all_flights(request):
    if request.method =="GET":
        flights = Flight.query.all()
        return flights

def get_needed_flight(request):
    if request.method =="POST":
        print(request.get_json()["from"])
        flight = Flight.query.filter_by(from_airport=request.get_json()["from"], to_airport=request.get_json()["to"]).all()
        if flight:
            all_flights = []
            for one_flight in flight:
                data = {"flight": [one_flight.from_airport, one_flight.to_airport, one_flight.departure_time, one_flight.arrivals_time]}
                all_flights.append(data)
            print(flight)
            return jsonify(all_flights)
        else:
            return jsonify({"flight": None, "error": "We have no flights in this direction"})
        

#TICKET   
def create_ticket(request):
    passenger = request.passenger
    flight = request.flight
    seat = request.seat
    baggage = request.baggage or 0
    ticket = Ticket(passenger=passenger, flight=flight, seat=seat, baggage = baggage)
    db.session.add(ticket)
    db.session.commit()
    return jsonify({"message": "Done"})

def get_tickets(request):
    if request.method == "GET":
        tickets = Ticket.query.all()
        return tickets
