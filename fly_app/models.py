from fly_app import app, db
from fly_app.controllers import location


class Airports(db.Model):

    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    city = db.Column(db.String)
    airport_name = db.Column(db.String)
    coordinate = db.Column(db.Float)
    timezone = db.Column(db.Integer)
    airport = db.relationship('Flights', backref='airport')

    def get_location(self):
        loc = location(self.city)
        return loc

    def __repr__(self):
        return f'Airport: {self.airport_name}, {self.city} {self.country}. UTC {self.timezone}'


class Flights(db.Model):

    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    from_airport = db.Column(db.Integer, db.ForeignKey('airport.id')) #airports city
    to_airport = db.Column(db.Integer, db.ForeignKey('airport.id')) #airports city
    departure_time = db.Column(db.String)
    arrivals_time = db.Column(db.String)
    duration = db.Column(db.String)
    seats = db.Column(db.Integer)
    base_price = db.Column(db.Integer)
    date = db.Column(db.String)
    passengers = db.Column(db.String)
    tickets = db.relationship('Tickets', backref='flight')

    def __repr__(self):
        return f'Flight from {self.from_airport} to {self.to_airport}. Date: {self.date}'


class Tickets(db.Model):

    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    passenger = db.Column(db.Integer, db.ForeignKey('user.id')) #users id
    flight = db.Column(db.Integer, db.ForeignKey('flight.id')) #flight id
    price = db.Column(db.Integer, db.ForeignKey('flight.base_price'))
    additional_price = db.Column(db.Integer, db.ForeignKey('product.price'))
    seat = db.Column(db.String)
    baggage = db.Column(db.Integer, max=100)

    def get_price(self):
        baggage_payment = self.baggage * 10
        price = self.price + baggage_payment + self.additional_price
        return price
    
    def __repr__(self):
        return f'Ticket: {self.id}. Passenger: {self.passenger}. Flight: {self.flight}. Price: {self.get_price}'


class Users(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    passport = db.Column(db.String)
    age = db.Column(db.Integer)
    tickets = db.relationship('Tickets', backref='user')

    def __repr__(self):
        return f'{self.first_name} {self.last_name}. Email: {self.email}. Id:{self.id}'


class Products(db.Model):
    
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    product = db.relationship('Tickets', backref='product')

    def __repr__(self):
        return f'{self.product_name}: {self.price}'