
from app import app

import flask_unittest

class TestFoo(flask_unittest.ClientTestCase):
    # Assign the `Flask` app object
    app = app




    def test_status_with_client(self, client):
        rv = client.get('/')
        assert rv.status_code == 200

    def test_reply_with_client(self, client):
        rv = client.get('/')
        self.assertInResponse(rv, 'Welcome to my Secure Distance Calculator API!!')
