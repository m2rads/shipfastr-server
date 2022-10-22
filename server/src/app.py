from flask import Flask, jsonify, make_response
from route_optimizer import optimizer
from demo_data import create_demo_distance_matrix
import os
import time


app = Flask(__name__)

@app.route('/api/demo')
def demo():
    data = create_demo_distance_matrix()
    optimized_data = optimizer(data)
    response = make_response(jsonify(optimized_data), 200)
    return response



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))