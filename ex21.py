def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) #-4391

print "That becomes: ", what, "Can you do it by hand?"

# Study Drills
# 1 Write a return function

def favcolorlength(favcolor):
	print "You favorite color is %s\nThis function will calculate it's string length." % favcolor,
	raw_input("Hit Enter")
	return len(favcolor)
	
favlength = favcolorlength(raw_input("Enter your favorite color: "))

print "The string length of your favorite color is %d" % favlength

# 2 Normal formula that would calculate what the nest of functions does as an expression

what2 = age + (height - (weight * (iq / 2)))
print "Using a normal expression, what calculates to %d" % what2

# 3 modifying the functions will give a different return and therefore a different final value

# 4 inverse of the function

what3 = multiply(divide(add(height, subtract(age, what2)), weight), 2)

print "Inverse function returns %d" % what3