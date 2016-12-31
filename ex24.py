print "Let's practice everything."
print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------"
print poem
print "------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	
start_point = 10000
beans, jars, crates = secret_formula(start_point) # apparently you can have multiple output returns. Some variables re-used outside the function here

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10 #could have used a shorthand operator here

print "we can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# Study Drills
# 1 Check for proper typing. Everything looks good so far...
# 2 Checking some errors.
# Remove a return variable: "Valueerror: too many values to unpack"
# Remove colon: Invalid syntax
# Remove a ending format: typeerror: not enough arguments for format string.
