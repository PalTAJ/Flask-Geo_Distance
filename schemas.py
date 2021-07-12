from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow
# from flask import jsonify, request

from app import app

ma = Marshmallow(app)


class GetDistanceSchema(Schema):

    # name = fields.String(required=False)
    location = fields.List(fields.Float(), required=True)

