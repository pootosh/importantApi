from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class Location:
    
    @staticmethod
    def get_location_by_address(address):
        if address!=None:
            address = address + ", India"
        # new_address = address  + ", India"
        app = Nominatim(user_agent="tutorial")
        try:
            return app.geocode(address).raw
        except:
            return Location.get_location_by_address(address)
    
    @staticmethod
    def my_location(address="275101, India"):
        
        return Location.get_location_by_address(address)

    def distance_from_my_Location(address):
        # print(Location.get_location_by_address(address).keys())
        dest_location_lat = Location.get_location_by_address(address)['lat']
        dest_location_lon = Location.get_location_by_address(address)['lon']
        dest_location = (dest_location_lat, dest_location_lon)


        m_location_lat = Location.my_location()['lat']
        m_location_lon = Location.my_location()['lon']
        m_location = (m_location_lat, m_location_lon)

        distance = geodesic(m_location, dest_location).km
        return distance
        


