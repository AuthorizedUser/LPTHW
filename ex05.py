name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Drill 1 - used find and replace to remove my_ from variables
# Drill 2 - using %r will print the variable/string with quotes around it
# Drill 3 - d,i-Signed integer decimal; o-unsigned octal; u-unsigned decimal; x,X-unsigned hexadecimal, lowercase and uppercase; e,E-floating point exponential format lowercase and uppercase; f,F-floating point decimal format lower and uppercase; g,G-exponent greaters than -4 or less than precision; c-single character or integer; r-string, converted using repr(); s-string, converted using str(); %, no argument converted, results in the "%" character
# Drill 4 - cent = inches * .393701; kilo = pounds * .453592; pounds = 2; inches = 5; print "%d inches is %.3f centimeters. %d pounds is %.3f kilos" % (inches, cent, pounds, kilo). Also, the round(variable, decimals) function can be used to round to a specific decimal place.