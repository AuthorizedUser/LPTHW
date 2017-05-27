from nose.tools import *
from ex48 import lexicon
# TYLER - Lowered all cases in tests to match functionality


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("North south east west up down")
    assert_equal(result, [('direction', 'north'),
                         ('direction', 'south'),
                         ('direction', 'east'),
                         ('direction', 'west'),
                         ('direction', 'up'),
                         ('direction', 'down')])
    #direction is a token then contains north, south, east, west
    #lexicon is a class that contains the scan function
    #scan takes a sentence string as it's parameter

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat punch slash")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat'),
                          ('verb', 'punch'),
                          ('verb', 'slash')])
    #verb is a token that contains words go, kill, and eat

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                         ('stop', 'in'),
                         ('stop', 'of')])
    # stop is a token that contains the, in, of

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess face")
    assert_equal(result, [('noun', 'bear'),
                         ('noun', 'princess'),
                         ('noun', 'face')])
    # noun is a token that contains words bear and princess

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                         ('number', 91234)])
    #number is a token that contains integers
    #the scan function converts strings that contain integers
    #probably by using the convert numbers function

def test_errors():
    assert_equal(lexicon.scan("asdfadfasdf"),
                             [('error', 'asdfadfasdf')])
    result = lexicon.scan("bear ias princess baer")
    assert_equal(result, [('noun', 'bear'),
                         ('error', 'ias'),
                         ('noun', 'princess'),
                         ('error', 'baer')])
    #token error is for unrecognized text.
