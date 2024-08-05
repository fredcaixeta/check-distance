from geopy.distance import geodesic
import geopy
import geopy.location
from geopy.geocoders import Nominatim

class Map:
    def __init__(self, endereco1: str, endereco2: str):
        self.endereco1 = endereco1
        self.endereco2 = endereco2

        self.dist = self.calcular()
        return self.dist
        
        
    def send_lat_long(self, loc1_lat, loc1_long, loc2_lat, loc2_long):
        if loc1_lat and loc2_lat:
            distancia = geodesic((loc1_lat, loc1_long), (loc2_lat, loc2_long)).km
            print(f"A distância entre {self.endereco1} e {self.endereco2} é de {distancia:.2f} km.")
            self.distancia = f"{distancia:.2f} km"
            
            
        else:
            raise(ValueError)
    
    def calcular(self):

        try:
            # Calcula a distância entre os endereços
            loc = geopy.Nominatim(user_agent="distance_calculator")
            
            loc1 = loc.geocode(self.endereco1)
            loc1_lat = loc1.latitude
            loc1_long = loc1.longitude
            
            loc2 = loc.geocode(self.endereco2)
            loc2_lat = loc2.latitude
            loc2_long = loc2.longitude
            
            dist = self.send_lat_long(loc1_lat, loc1_long, loc2_lat, loc2_long)
            
        except Exception as e:
            print(e)


