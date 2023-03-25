from geopy.geocoders import Nominatim
from fly_app.models import Airports


city = Airports.city
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode(city)

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)