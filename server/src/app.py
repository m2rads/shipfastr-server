from flask import Flask, jsonify
from route_optimizer import optimizer, create_demo_distance_matrix
import os
import time

app = Flask(__name__)

@app.route('/api/demo')
def demo():
    data = create_demo_distance_matrix()
    res = optimizer(data)
    # jsonResult = json.loads(res)
    print(jsonify(res))
    return res



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))