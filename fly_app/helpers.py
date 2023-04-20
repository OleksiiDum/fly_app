import math
import hashlib
from random import getrandbits as randbit
from functools import wraps
from flask import session


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



def get_price(dist, k, baggage, additional_price):
    baggage_payment = baggage * 10
    price = dist * k + baggage_payment + additional_price
    return price


def hashed(data):
    salt = "saltedhash"
    data = str(data) + salt
    return hashlib.md5(data.encode()).hexdigest()


def randome_code():
    hash = randbit(128)
    return str(hash)


def html_template():
    template = "<h1>Hello</h1>"
    return template

# Seats

def generate_seats():
    rows_econom = 25
    rows_business = 5
    seats_list = []
    current_letter = 0
    current_row = 1
    seats_letters = "ABCDEF"
    for i in range(rows_business):
        for j in range(4):
            t = str(current_row) + seats_letters[current_letter]
            current_letter += 1
            seats_list.append((t, 'business'))
        current_row += 1
        current_letter = 0
    for i in range(rows_econom):
        for j in range(6):
            t = str(current_row) + seats_letters[current_letter]
            current_letter += 1
            seats_list.append((t, 'econom'))
        current_row += 1
        current_letter = 0
    

    return seats_list

def is_logged_in():
    if session.get('email'):
        return True

def auth_required(func):
    @wraps(func)
    def wraper():
        if is_logged_in:
            return func()
        else:
            return "Login first"
    return wraper

def is_admin():
    if session.get('admin'):
        return True

def admin(func):
    @wraps(func)
    def new_wraper():
        if is_admin:
            return func()
        else:
            return "Access Denied"
    return new_wraper