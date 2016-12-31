def break_words(stuff):
    """This function will break up words for us from a string. Type: string. Returns list"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words. Argument type 'list'. Returns list"""
    return sorted(words)

def print_first_word(words): # error 3: missing a colon
    """Prints the first word after popping it off. Type: list"""
    word = words.pop(0) #error 1: mispelled pop as poop
    print word

def print_last_word(words):
    """Prints the last word after popping it off. Type: list"""
    word = words.pop(-1) # error 2: missing a parentheses
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words. Type: string"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence. Type: string"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one. Type: string"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6 # fixed to equal five
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #changed backslash to forward-slash for divide. Incidentally, discovered that backslash is a line-continuation character by reading the error code
    crates = jars / 100
    return jelly_beans, jars, crates

namestrin = "test a string out" # this was used to help troubleshoot the impossible-for-me-to-find error on what is now line 74 (where we call secret_formula() as a format)
start_point = 10000
beans, jars, crates = secret_formula(start_point) #remove extra equal signs since it isn't a boolean operator. Changed dash in name to an underscore

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates) #fixed a spelling error in the sentence

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point) #fixed name misspelling in the argument. ALSO, learned how to use a method. Too me FOREVER to figure out that a parenthese is missing since the word-wrap on my laptop put start_point on a new line. I didn't register that the name was an argument and needed a close parentheses. The interpreter returned an error on the line adding a value to the sentence name, which kept throwing me off... I finally noticed the real issue after placing some test strings around a file and trying to figure out what I was doing wrong.

sentence = "All good things come to those who wait."
#Fixed misspellings, although I really don't see the need to do so since this is a programming exercise
#(reminds me of missing a calculus problem for misspelling "Sandwich")

words = break_words(sentence) #removed the ex25 reference
sorted_words = sort_words(words) #removed the ex25 reference

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #removed the period before. Odd that these sometimes reference ex25 and sometimes don't
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) #removed ex25 module reference
print sorted_words #spelled print method correctly

print_first_and_last(sentence) #fixed misspelling in method call

print_first_and_last_sorted(sentence) #fixed argument mispelling of 'sentence' name and also removed the unneeded indent. Also, discovered a misspelling in the method call.


#NOTE: The last few errors were found by importing. It's an excellent way to check syntax and hunt for which line is broken. I learned that the line that is broken can be a line shortly BEFORE the line the interpreter is pointing to (the interpretter does not know what you are trying to do so it keeps advancing)