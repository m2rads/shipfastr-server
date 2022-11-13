import googlemaps
from dotenv import load_dotenv
import os

class Navigation:

    def __init__(self, optimized_routes: dict, addresses:dict) -> None:
        load_dotenv()
        self.gm = googlemaps.Client(os.getenv('GCP_API_Key'))
        self.optimized_routes = optimized_routes
        self.addresses = addresses

    def get_direction(self, route):
        """Utilizes Google Maps API to get directions for Vehicles

        Returns:
            routes: list
        """
        origin = route.pop(0)
        routes = self.gm.directions(origin=origin, destination=origin, waypoints=self.addresses)
        return routes
        
    def find_vehicle_directions(self):
        """Finds directions of vehicles based on the optimized route given
        
        """
        #Separate the vehicles with no destinations
        for route in self.optimized_routes:
            if self.optimized_routes[route] != [0,0]:
                for dest in self.optimized_routes[route]:
                    #Put the address based on the index of addresses in oprimized routes
                    self.optimized_routes[route][self.optimized_routes[route].index(dest)] = self.addresses[dest]
                #Get directions
                self.optimized_routes[route] = self.get_direction(self.optimized_routes[route])
            else:
                self.optimized_routes[route] = None
            
        
        return self.preprocess()
    def preprocess(self):
        """Cleans the response and only returns the required data, Overview Polyline.
        """
        processed_data = {}
        for vehicle_idx in self.optimized_routes:
            
            if self.optimized_routes[vehicle_idx] != None:
                processed_data[vehicle_idx] = {}
                processed_data[vehicle_idx]["overview_polyline"] = self.optimized_routes[vehicle_idx][0]["overview_polyline"]["points"]
                processed_data[vehicle_idx]["coordinates"] = self.extract_coordinates(self.optimized_routes[vehicle_idx])
            else:
                processed_data[vehicle_idx] = None
        return processed_data
                
    def extract_coordinates(self, vehicle_direction):
        processed = []
        for coordinates in vehicle_direction[0]["legs"]:
            processed.append(coordinates["end_location"])
        return processed
                
                
        
                
        

            
            