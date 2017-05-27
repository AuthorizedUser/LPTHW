"""ex48 package. lexicon module"""
from decimal import *

def convert_number(s): # used for study drill 4
    try:
        return Decimal(s)
    except InvalidOperation:
        return None

def scan(input_string):
    """Takes a sentence parameter and returns a list of tuples.
    Each tuple contains (token, word) where the token is the
    type of word in the sentence
    """
    direction = [
        'north', 'south', 'west', 'east',
        'up', 'down', 'left', 'right',
        'back'
        ]
    verb = ['go', 'stop', 'kill', 'eat', 'punch', 'slash']
    stop = ['the', 'in', 'of', 'from', 'at', 'it']
    noun = ['bear', 'door', 'cabinet', 'princess', 'face']
    tokendict = {}

    for token, wordlist in zip(["direction", "verb", "stop", "noun"],
                               [direction, verb, stop, noun]):
        tokendict.update({(word, token) for word in wordlist})

    input_words = input_string.lower().split(' ')
    final_tuples = [("number", convert_number(word)) for word in \
                     input_words if convert_number(word)]
    final_tuples += [(tokendict.get(word, "error"), word) for word in
                    input_words if not convert_number(word)]

    return final_tuples



	# number will be used as final elif func
	# error will be used for else

	# tuplelist = []
    #
	# for word in stringlist:
	# 	if word.lower() in direction:
	# 		tuplelist.append(('direction', word))
	# 	elif word.lower() in verb:
	# 		tuplelist.append(('verb', word))
	# 	elif word.lower() in stop:
	# 		tuplelist.append(('stop', word))
	# 	elif word.lower() in noun:
	# 		tuplelist.append(('noun', word))
	# 	elif convert_number(word) != None:
	# 		tuplelist.append(('number', convert_number(word)))
	# 	else:
	# 		tuplelist.append(('error', word))
    #
	# return tuplelist

if __name__ == "__main__":
    # TEST
    print scan("north eat princess 15")
