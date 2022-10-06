from flask import Flask, make_response
import pydaisi as pyd
import os
import time

app = Flask(__name__)

vehicle_routing_problem_ = pyd.Daisi("soul0101/Vehicle Routing Problem ")

input_locations, vehicle_capacities = []

vehicle_routing_problem_.vrp_calculator(input_locations, vehicle_capacities, carryforward_penalty=1000, search_timeout=10, first_sol_strategy="AUTOMATIC", ls_metaheuristic="AUTOMATIC").value

@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))