from flask import Flask, make_response
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))