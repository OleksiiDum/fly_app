from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, FloatField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from fly_app.models import  Airport, Flight, Passanger, Account


class AddAirportForm(FlaskForm):
    country = StringField('Countries', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    airport_name = StringField('Airport Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteAirportForm(FlaskForm):
    airport = SelectField(u'Airports')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(DeleteAirportForm, self).__init__(*args, **kwargs)
        self.airport.choices = [(str(airp.id), airp.airport_name + ' ' + airp.city) for airp in Airport.query.all()]


class AddFlightForm(FlaskForm):
    from_airport = SelectField(u'From Airport')
    to_airport = SelectField(u'To Airport')
    dep_time = DateTimeField(format='%Y-%m-%d %H:%M')
    arr_time = DateTimeField(format='%Y-%m-%d %H:%M')
    price = IntegerField()
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(AddFlightForm, self).__init__(*args, **kwargs)
        self.from_airport.choices = [(str(airp.id), airp.airport_name + ' ' + airp.city+ ' ' + airp.country) for airp in Airport.query.all()]
        self.to_airport.choices = [(str(airp.id), airp.airport_name + ' ' + airp.city+ ' ' + airp.country) for airp in Airport.query.all()]


class DeleteFlightForm(FlaskForm):
    flight = SelectField(u'Flights')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(DeleteFlightForm, self).__init__(*args, **kwargs)
        flights = Flight.query.all()
        choices = [(str(fl.id), f"{self.get_city_name(fl.from_airport)} to {self.get_city_name(fl.to_airport)} {fl.departure_time[:11]}") for fl in flights]
        self.flight.choices = choices

    def get_city_name(self, airport_id):
        airport = Airport.query.get(airport_id)
        return airport.city if airport else 'Unknown'


# class DeletePassengerForm(FlaskForm):
#     user_account = SelectField(u'Account')
#     passenger = SelectField(u'Passenger')
#     submit = SubmitField('Submit')

#     def __init__(self, *args, **kwargs):
#         super(DeletePassengerForm, self).__init__(*args, **kwargs)
#         accounts = Account.query.all()
#         passengers = 
#         choices = [(str(account.id), f"{account.email}") for account in accounts]
#         choices_2 = set_pa
#         self.user_account.choices = choices

#     def set_passenger_choices(self, account_id):
#         account = Account.query.get(account_id)
#         if account:
#             passengers = Passanger.query.filter_by(account_id=account.id).all()
#             choices = [(str(passenger.id), f"{passenger.first_name} {passenger.last_name}") for passenger in passengers]
#             self.passenger.choices = choices
#         else:
#             self.passenger.choices = []

#     def get_account_email(self, account_id):
#         account = Account.query.get(account_id)
#         return account.email if account else 'Unknown'
