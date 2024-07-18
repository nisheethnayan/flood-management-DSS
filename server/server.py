from flask import Flask,jsonify
from flask_cors import CORS
import json
import os

cwd = os.getcwd()

app = Flask(__name__)
CORS(app)

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

@app.route("/api/home",methods=['GET'])
# def return_home():
    # return jsonify({
    #     "message":"Hello world!"
    # })
    # return 
def get_json_data():
    file_path = cwd+'/exceed_count_data.json'  # Adjust the path if necessary
    json_data = read_json_file(file_path)
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True,port=8080)