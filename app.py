from __future__ import absolute_import

from flask import Flask

from flask import request, Blueprint

from yandex_geocoder import Client
import math
from schemas import *
import marshmallow




from flask import Blueprint
distance_finder = Blueprint("DF", __name__)   # flask blueprints

@distance_finder.route('/get-distance', methods=['POST','GET']) ## creating a service with blueprints
def getDistance():

    try:
        data = GetDistanceSchema().load(request.json)

    except marshmallow.exceptions.ValidationError as error:  ## only allows location coordinates to be passed, defined in schemas
        return {400: 'Bad Request'}
    if not request.json:
        return {404: 'not found'}


    client = Client("enter your code")
    default_coordinates = client.coordinates("Moscow Ring Road")  # get default coordinates (Moscow ring road)
    print(default_coordinates)

    max_lon = 55.917  ## MKAD Range coordinates
    min_lon = 55.503

    max_lat = 37.895
    min_lat = 37.329

    if (data['location'][0] > min_lon and data['location'][0] < max_lon) and (data['location'][1] > min_lat and data['location'][1] < max_lat): ## checks if given address is within mkad coordinates
        return {'Distance': 'input address is inside the MKAD'}

####################


    R = 6373.0 # earth Radius

    lat1 = math.radians(default_coordinates[1])   ##change Moscow Ring Road Coordinates into radians
    lon1 = math.radians(default_coordinates[0])

    lat2 = math.radians(data['location'][0])  # Input Coordinates
    lon2 = math.radians(data['location'][1])

    dlon = lon2 - lon1   # measure change in coordinates
    dlat = lat2 - lat1

    ## Haversine formula, which calculates the great-circle distance between two points.

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    print(distance)
    return {'Distance':distance}


app = Flask(__name__)
app.register_blueprint(distance_finder)  ## adding the blueprints to the flask app

@app.route('/')
def hello():
    return 'Welcome to my Secure Distance Calculator API!!'


if __name__ == '__main__':
    
    import logging
    logging.basicConfig(filename='logs.log',level=logging.DEBUG)
    app.run(debug=True)
