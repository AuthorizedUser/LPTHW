x = "There are %d types of people." % 10 # format calls a decimal into the string
binary = "binary" #assigns a name
do_not = "don't" #assigns a name
y = "Those who know %s and those who %s." % (binary, do_not) #assigns a name that includes a string with two formats and two variable calls at the end

print x #prints variable x
print y #prints variable y

print "I said: %r." % x #will print with quotes around it
print "I also said: '%s'." % y # Will print as normal in quotes that are written

hilarious = False #assigns a variable with the false boolean
joke_evaluation = "Isn't that joke so funny?! %r" #Not sure what a un-named format will call (SEE BELOW)

print joke_evaluation % hilarious #looks like the format finally calls a name here

w = "This is the left side of..." #assigns a name with a string
e = "a string with a right side." #assigns a name with a string

print w + e #prints two names that have strings in them

# Study Drills
# 1 Comments on each line
# 2 Strings inside strings: line 4 (x2), line 9, line 10. Line 13 doesn't count since it's a boolean inside a string
# 3 Pretty sure... although line 14 does use a 'literal' string format to call a boolean value. Interestingly, the boolean does not have quotes around it. After testing, it is the same with decimals, even contained in a variable. Only strings get the quotes
# 4 The + sign is a concatenation function in the print() command. It combined the two names that have strings within them