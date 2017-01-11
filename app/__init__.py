from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS, cross_origin
from flask_restful import Api

# WSGI application object.
app = Flask(__name__)
CORS(app)

# Load configuration.
app.config.from_object('config')

# Database object.
db = MongoEngine(app)

# REST api interface.
api = Api(app)

# Routing
# Import blueprint modules
from app.Devices.views import DevicesView
from app.Information.views import InformationsView
# Register routes
api.add_resource(DevicesView, '/api/applications')
api.add_resource(InformationsView, '/api/information')


