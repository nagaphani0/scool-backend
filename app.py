from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello from Flask API!"}

@app.route('/api/hello')
def hello():
    return {"message": "Hello from Flask API!"}

if __name__ == '__main__':
    app.run(debug=True)
