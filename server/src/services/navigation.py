import googlemaps
from dotenv import load_dotenv
import os

class Navigation:

    def __init__(self) -> None:
        load_dotenv()
        self.gm = googlemaps.Client(os.getenv('GCP_API_Key'))

    def get_direction(self, addresses: list):
        """Utilizes Google Maps API to get directions for Vehicles

        Args:
            addresses (list): List of Addresses (First index is the origin)

        Returns:
            routes: list
        """
        origin = addresses.pop(0)
        routes = self.gm.directions(origin=origin, destination=origin, waypoints=addresses)
        return routes
        
    def find_vehicle_directions(self, optimized_routes: dict, addresses: list):
        """Finds directions of vehicles based on the optimized route given
        
        Args:
            optimized_routes (dict),
            addresses (list)
        """
        #Separate the vehicles with no destinations
        for route in optimized_routes:
            if optimized_routes[route] != [0,0]:
                for dest in optimized_routes[route]:
                    #Put the address based on the index of addresses in oprimized routes
                    optimized_routes[route][optimized_routes[route].index(dest)] = addresses[dest]
                #Get directions
                optimized_routes[route] = self.get_direction(optimized_routes[route])
            else:
                optimized_routes[route] = None
        return optimized_routes    

            
            