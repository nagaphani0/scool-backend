from flask import Flask, request, jsonify
from extomo import DatabaseClass

app = Flask(__name__)

@app.route('/get_all_records', methods=['GET'])
def get_all_records():
    return jsonify(DatabaseClass().get_all_records())

@app.route('/get_record', methods=['POST'])
def get_record():
    data = request.get_json()
    return jsonify(DatabaseClass().get_profile(data))

@app.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    return jsonify(DatabaseClass().reset_password(data))

if __name__ == '__main__':
    app.run(debug=True)