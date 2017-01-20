"""ex48 package. lexicon module"""
from decimal import *

def convert_number(s): # used for study drill 4
	try:
		return Decimal(s)
	except InvalidOperation:
		return None

def convert_number_bak(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(input_string):
	"""Takes a sentence parameter and returns a list of tuples.
	Each tuple contains (token, word) where the token is the
	type of word in the sentence"""

	stringlist = input_string.split(' ')
	direction = ['north', 'south', 'west', 'east', 'up', 'down']
	verb = ['go', 'kill', 'eat', 'punch']
	stop = ['the', 'in', 'of']
	noun = ['bear', 'princess', 'face']
	# number will be used as final elif func
	# error will be used for else

	tuplelist = []

	for word in stringlist:
		if word.lower() in direction:
			tuplelist.append(('direction', word))
		elif word.lower() in verb:
			tuplelist.append(('verb', word))
		elif word.lower() in stop:
			tuplelist.append(('stop', word))
		elif word.lower() in noun:
			tuplelist.append(('noun', word))
		elif convert_number(word) != None:
			tuplelist.append(('number', convert_number(word)))
		else:
			tuplelist.append(('error', word))

	return tuplelist
