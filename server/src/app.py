from flask import Flask, jsonify, make_response
from route_optimizer import optimizer
from demo_data import create_demo_distance_matrix
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


@app.route('/api/optimize', methods=['GET'])
def optimize(request): 
    data = request.get_json()
    # get the data from the request body and create repsonse from route_optiomzer
    return "hello"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))