print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
# Study drill
# 1 raw_input() allows for a prompt in the argument. It gives the use a cursor to input data into the variable.
# 2 Can be included in a variable.... as below

quiz = raw_input("Who goes there? ")
print "%s. You may pass" % quiz

# 3 Above
# 4 The raw_input line needs to escape the quote so it does not enter the output and escape the string. Of course, this is only because %r is used, not %s