from flask import Flask
import os
import time

app = Flask(__name__)


incomings = [

    {"source": "source address"},
    {"destinations": ['address 1', 'address 2', 'address 3', 'address 4', 'address 5'] } 

]

@app.route('api/distancematrix')
def index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))