# use an assert raises

from nose.tools import *
import parser
from ex48.parser import Parse
from ex48.parser import ParserError



p = Parse()


# Existing lexicon
# direction = ['north', 'south', 'west', 'east', 'up', 'down']
# verb = ['go', 'kill', 'eat', 'punch']
# stop = ['the', 'in', 'of']
# noun = ['bear', 'princess', 'face']
# number will be used as final elif func
# error will be used for else


def peek_test():

    testlist101 = [('verb', 'eat'),
                   ('stop', 'the'),
                   ('noun', 'bear')]
    assert_equal(p.peek(testlist101),
                'verb')

def match_tests():

    testlist201 = [('verb', 'eat'),
                   ('stop', 'the'),
                   ('noun', 'bear')]
    assert_equal(p.match(testlist201, 'verb'),
                ('verb', 'eat'))
    assert_equal(p.match(testlist201, 'noun'),
                None)

def skip_tests():

    testlist301 = [('stop', 'the'),
                   ('stop', 'in'),
                   ('verb', 'eat'),
                   ('noun', 'bear')]

    assert_equal(p.skip(testlist301, 'stop'), None)
    assert_equal(p.match(testlist301, 'verb'),
                ('verb', 'eat'))

def parse_verb_tests():
    testlist311 = [('stop', 'the'),
                   ('stop', 'in'),
                   ('verb', 'eat'),
                   ('noun', 'bear')]
    assert_equal(p.parse_verb(testlist311), ('verb', 'eat'))
    testlist312 = [('stop', 'the'),
                   ('stop', 'in'),
                   ('noun', 'bear')]
    # with assert_raises(ParserError):
    #     p.parse_verb(testlist312)
    assert_raises(ParserError, p.parse_verb, testlist312)

def parse_number_tests():
    testlist321 = [
        ('stop', 'the'),
        ('number', '51'),
        ('verb', 'eat'),
        ('noun', 'bear')
        ]
    assert_equal(p.parse_number(testlist321), ('number', '51'))
    testlist322 = [
        ('stop', 'the'),
        ('error', '49jljfx'),
        ('verb', 'eat'),
        ('noun', 'bear')
        ]
    assert_equal(p.parse_number(testlist322), None)

def parse_object_tests():
    """Tyically will recieve a list with stop words
    and front nouns and verbs already parsed by other functions"""
    testlist401 = [('direction', 'south')]

    assert_equal(p.parse_object(testlist401),
                ('direction', 'south'))

def parse_subject_tests():
    """Tyically will recieve a list with stop words
    and front subject word missing, with subj argument"""
    testlist4501 = [('verb', 'eat'),
                   ('stop', 'the'),
                   ('noun', 'bear')]

    sentence4501 = (p.parse_subject(testlist4501,
                 ('noun', 'princess')))
    assert_equal(sentence4501.subject, 'princess')

def parse_sentence_tests():

    testlist501 = [('error', 'asd123'),
                   ('verb', 'kill'),
                   ('stop', 'the'),
                   ('number', '3'),
                   ('noun', 'bear')]
    assert_raises(ParserError,
                 p.parse_sentence, testlist501)
    # should raise error

    testlist502 = [('verb', 'kill'),
                   ('stop', 'the'),
                   ('noun', 'bear')]
    sentence502 = p.parse_sentence(testlist502)
    assert_equal(sentence502.subject,
                 'player')
    assert_equal(sentence502.object,
                 'bear')
    assert_equal(sentence502.verb,
                'kill')
