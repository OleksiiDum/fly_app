from fly_app.models import  Airport, Flight, Product, Ticket, Account
from fly_app import db
import fly_app.helpers as helpers
from flask import render_template, flash, Response



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
    if request.method == "POST":
        email = request.form["email"]
        user_password = request.form["password"]
        db_user = Account.query.filter_by(email=email).first()
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
            db.session.add(user)
            db.session.commit()
    return "Done"
