from geopy.geocoders import Nominatim
import math
from fly_app.models import  Airport, Flight, Product, Ticket
from flask import request
from fly_app import db


# Geolocation and Path
geolocator = Nominatim(user_agent="MyApp")

kyiv_location = geolocator.geocode("Kyiv")
berlin_location = geolocator.geocode("Berlin")

def distance(coord1, coord2):
    # Coordinates are given as (latitude, longitude) tuples
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = int(6371 * c)
    print(f"Distance:{km} km")

    return km

path = distance((kyiv_location.latitude, kyiv_location.longitude), (berlin_location.latitude, berlin_location.longitude))


#Price
base_price = path * 0.25

def get_price():
    baggage_payment = Ticket.baggage * 10
    price = base_price + baggage_payment + Ticket.additional_price
    return price


#DB
def create_airport():
    if request.method == "POST":
        country = request.form.get("country")
        city = request.form.get("city")
        airport_name = request.form.get("airport_name")
        timezone = request.form.get("timezone")
        
        airport = Airport(country=country, city=city, airport_name=airport_name, timezone=timezone)
        db.session.add(airport)
        db.session.commit()
    return "Done"

def get_all_airports():
    if request.method == "GET":
        all_airports = Airport.query.all()
        return all_airports
