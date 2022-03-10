from crypt import methods
from selectors import DefaultSelector
from flask import Flask, send_from_directory
from flask_restful import Resource, Api
#from flask_cors import CORS

from api.RandomUserApi import RandomUserApi

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
#CORS(app) #comment this out on deployment
api = Api(app)

@app.route("/")
def serve():
    return send_from_directory(app.static_folder, 'index.html')

api.add_resource(RandomUserApi, '/random-user')

