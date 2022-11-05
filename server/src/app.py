import imp
from flask import Flask, jsonify, make_response, request
from services.routeOptimizer import optimizer
from services.distanceMatrix import create_distance_matrix
from services.demoData import create_demo_distance_matrix
from services.navigation import Navigation
import os
import time


app = Flask(__name__)

@app.route('/api/demo', methods=['GET'])
def demo():
    data = create_demo_distance_matrix()
    optimized_data = optimizer(data)
    if (type(optimized_data) is str ): 
        response = make_response(jsonify(optimized_data), 500)
    else: 
        response = make_response(jsonify(optimized_data), 200)
    return response


@app.route('/api/optimize', methods=['POST'])
def optimize():
    try: 
        data = request.get_json()
        # get the data from the request body and create repsonse from route_optimizer
        distance_matrix = create_distance_matrix(data)
        routes = optimizer(distance_matrix)
        #Get directions from Navigation class
        directions = Navigation().find_vehicle_directions(routes, data['addresses'])
        return make_response(jsonify(routes), 200)
    except Exception as ex:
        return make_response(jsonify({'Error': ex}), 500)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))