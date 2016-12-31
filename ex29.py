people = 20
cats = 20 #original was 30
dogs = 15


if people < cats: #This will run with original variable
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs: #This will run with original variables
	print "The world is dry!"
	
	
dogs += 5 #one of our new shorthand increment operators

if people >= dogs: #This will run
	print "People are greater than or equal to dogs."
	
if people <= dogs: #this will run
	print "People are less than or equal to dogs."
	

if people == dogs: #This line will accompany BOTH of the above lines since they are 'or equal to' booleans.
	print "People are dogs."
	
if not (people == dogs and people == cats):
	print "People are not equal in numbers to both animals"

favar = False
if favar:
	print "This will never print"
	
# Study Drills
# 1 The if statement gives a false or true boolean. If the boolean is True, the indented code will run.
# 2 The code needs to be indented to demonstrate that it is the resulting code of a true if statement... to differentiate it from seperate code that comes later in the script
# 3 If it is not indented, it is run independently of the if statement. It will be run whether the if statement is true or false
# 4 Added final if statement on lines 31-32 to try out 'not' and 'and' statements.
# 5 Different values on the original variables will trigger seperate if statements... and different print lines will be output