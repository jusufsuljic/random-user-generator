from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
import os

from api.RandomUserApi import RandomUserApi

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) #comment this out on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

api.add_resource(RandomUserApi, '/random-user')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))