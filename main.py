import re
import json
import requests
from flask import Flask, Response, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=['POST'])
def get_json():
    data = json.loads(request.data)
    data['token'] = '4nRh)M>Rt63g]&<'
    url = "http://webappenglishuniverse.com.br/wp-json/api"
    end_point = url + data['path']
    response = requests.post(end_point, data)
    print(response.json())
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0" port=5000)
