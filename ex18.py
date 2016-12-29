# this one is like your scripts with argv
def print_two(*args): #does not accept infinite arguments! It will name the arguments on the next line
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#This one takes no arguments
def print_none():
	print "I got nothin'."

	
print_two("Zed","Shaw")
print_two_again("Zed",  "Shaw") #testing if space is allowed. SPACE IS OK
print_one("First!%s" % "firstlytest") # Testing formats. FORMATS ARE OK IN ARGUMENTS
print_none()

# Study Drills
# None, only remember function syntax