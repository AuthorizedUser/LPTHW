def break_words(stuff):
	"""This function will break up words for us.""" #have never seen this type of comment format before
	words = stuff.split(' ') # new function...
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
# Study Drills
# 1 The remaining lines use the last 3 functions. sorted_words name is given the value of ex25.sort_sentence(sentence). The sentence is entered into the function where it uses the break function and the sort function. It is returned and becomes the value of the sorted_words name. Essentially, it just combined the first two function we wrote. The second function combins the break_words function and the two pop functions to show the first and last words in the list. The last function does the same thing but uses the sort_sentence function instead of break_sentence. It becomes clear at this point that the functions to not store anything in the argument name (no return)
# 2 View module documentation by using help(module) or help(module.method). Module must be imported for this to work
# 3 Can directly run methods without writing the module before the period.
# 4 Trying to create an error caused python to find a syntax error when it first imported the module