integ = raw_input("Enter an integer or test a string\n> ")

try:
	integint = int(integ)
	print "%d is an integer for sure" % integint
except ValueError:
	print "%r is not an integer" % integ
	#names declared within the loop do not exist outside it
	
test_var_outside = "Outside test var"

try:
	test_var_inside = "Inside test var"	
	print """-----
Inside loop:
test_var_outside: %r
test_var_inside: %r
-----""" % (test_var_outside, test_var_inside)
	integtest = int(test_var_outside)
except:
	print "except line to end loop. test %r %r" % (test_var_outside, test_var_inside)

print """\n-----
Outside loop:
test_var_outside: %r
test_var_inside: %r
-----""" % (test_var_outside, test_var_inside)

# Testing if formats work in triple quotes. Testing if variables created inside a loop survive outside the loop. Variables do count inside loops per test.