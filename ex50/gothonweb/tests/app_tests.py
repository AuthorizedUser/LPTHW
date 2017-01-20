from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_Index():

    # check that we get a 303 - see other on the / URL
    resp = app.request("/") # should be valid URL
    assert_response(resp, status='303')

    # test our first GET request to /game
    resp = app.request("/game")
    assert_response(resp)


def test_GameEngine():


    # make sure default values work for the form
    resp = app.request("/game", method="GET")
    assert_response(resp, status="200")

    # test that we get expected values
    data = {'action': 'tell a joke'}
    resp = app.request("/game", method="POST", form="tell a joke")
    assert_response(resp, contains="Laser", status="303")
