from fly_app import db


class Airport(db.Model):

    __tablename__ = 'airports'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    airport_name = db.Column(db.String, nullable=False)
    timezone = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Airport: {self.airport_name}, {self.city} {self.country}. UTC +{self.timezone}'


class Flight(db.Model):

    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    from_airport = db.Column(db.Integer, db.ForeignKey('airports.id'), nullable=False)
    to_airport = db.Column(db.Integer, db.ForeignKey('airports.id'), nullable=False)
    departure_time = db.Column(db.String, nullable=False)
    arrivals_time = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Flight from {self.from_airport} to {self.to_airport}. Date: {self.date}'


class Ticket(db.Model):

    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    passenger = db.Column(db.Integer, db.ForeignKey('users.id')) #users id
    flight = db.Column(db.Integer, db.ForeignKey('flights.id')) #flight id
    price = db.Column(db.Integer, db.ForeignKey('flights.base_price'))
    additional_price = db.Column(db.Integer, db.ForeignKey('products.price')) #???
    seat = db.Column(db.String, nullable=False)
    baggage = db.Column(db.Integer)
    
    def __repr__(self):
        return f'Ticket: {self.id}. Passenger: {self.passenger}. Flight: {self.flight}. Price: {self.get_price}'


class Passanger(db.Model):

    __tablename__ = 'passengers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False) 
    passport = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}. Email: {self.email}. Id:{self.id}'
    

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    verified = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'{self.email} Password: {self.password}. Verified: {self.verified}'


class Authcode(db.Model):

    __tablename__ = 'code'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    userid = db.Column(db.Integer, db.ForeignKey('accounts.id'))


class Product(db.Model):
    
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.product_name}: {self.price}'
    
