import geocoder
from geopy.geocoders import Nominatim

class Location:
    def my_location():
        my_location = geocoder.ip('me').latlng
        return my_location

    def get_location_by_address(address):
        app = Nominatim(user_agent="tutorial")
        try:
            return app.geocode(address).raw
        except:
            return get_location_by_address(address)
