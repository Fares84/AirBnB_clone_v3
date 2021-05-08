#!/usr/bin/python3
""" Module for Flask REST application """

from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views
from os import getenv
from flas import make_response


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """ close databse session """
    storage.close()


@app.teardown_errorhandler(404)
def not_found(exception):
    """ page not found """
    return make_response({'error': 'Not found'}, 404)


if __name__ == "__main__":
    """ main fucntion """
    app.run(host=getenv('HBNB_API_HOST', default='0.0.0.0'),
            port=getenv('HBNB_API_PORT', default=5000), threaded=True)
