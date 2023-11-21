from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, FloatField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired
from fly_app.models import  Airport, Flight, Product


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

class AddProductForm(FlaskForm):
    name = StringField('Products', validators=[DataRequired()])
    description = StringField('Description')
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteProductForm(FlaskForm):
    name = SelectField(u'Products')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(DeleteProductForm, self).__init__(*args, **kwargs)
        self.name.choices = [(str(prod.id), prod.product_name + ' ' + str(prod.price)) for prod in Product.query.all()]
