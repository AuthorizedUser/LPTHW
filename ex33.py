#i = 0
#numbers = []

def createrangelist(max_num, istep):
	"""\nCreates a list that contains numbers leading up to the value of argument 1.\nArgument 2 specifies the step interval between numbers. Returns a list"""
	
	i = 0
	numbers = []
	#istep = int(raw_input("What step interval would you like in the list?\nThe list begins at 0\n> "))
	
	while i < (max_num + istep):
		print "At the top i is %d" % i
		
		numbers.append(i) 
		i = i + istep
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i 
	
	return numbers

def createrangelist2(max_num, istep):
	
	i = 0
	numbers = []
	
	for i in range(0, max_num + istep, istep):
		
		print "At the top i is %d" % i
		numbers.append(i)
		
		# i += istep #just a test
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i # There is no top and bottom in the for-loop
		
	return numbers
	
#numbersext = createrangelist(int(raw_input("Enter a maximum value to end the list\n> ")),\
 #int(raw_input("What step interval would you like in the list?\nThe list begins at 0\n> ")))

 
 
numbersext = createrangelist2(int(raw_input("Enter a maximum value to end the list\n> ")),\
 int(raw_input("What step interval would you like in the list?\nThe list begins at 0\n> ")))
 
print "The numbers: "

for num in numbersext:
	print num #will print every value in numbers on a seperate line

# Study Drills
# 1 Learned that you cannot place the int() function inside raw_input. Need to place it around the raw_input method.
# Since the variables are now contained in a method, you need a way to extract the list 'numbers' from the function. I stored it in a name called 'numbersext' and used a return to get it out of the function
# was able to add a + 1 to the boolean statement in the while loop. Also added a descriptor for the method
# 2 In the last drill, the script was re-written to try various numbers from user input
# 3 Added the step interval question in the method
# 4 Script has been rewritten to use this function
# 5 For loop was added as second function. Manipulating i increments the function by that ammount if it is performed BEFORE the append. i seems to reset in each for-loop. so there is no 'loop bottom' number difference. The range() function never prints the last value so the less than statement in the while-loop is equivalent.