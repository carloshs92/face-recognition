# Import flask and template operators
from flask import Flask
from flask_cors import CORS
import json
from .services.detector_service import detector_service

BLUEPRINTS = (detector_service, )


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    configure_blueprints(app, BLUEPRINTS)
    CORS(app, headers=['Content-Type', 'database'], resources=r'/api/*')
    return app


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def garbage():
    #@app.after_request
    #def after_request(response):
    #  response.headers.add('Access-Control-Allow-Origin', 'webapp')
    #  response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    #  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    #  return response
    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return json.dumps({"error": "error"})

