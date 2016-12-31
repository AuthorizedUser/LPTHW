people = 50 #30
cars = 35 #40
buses = 5 #15


if cars > people:
	print "We should take the cars."
elif cars < people: #looks like an else-if statement. Will only be evaluated if first if statement is false. (making it independent would make it be evaluated seperately, first if statement MUST be false for it to be evaluated.
	print "We should not take the cars."
else: #this will occur in the case cars == people. The else code runs if previous if and elif statements both turn out to be false. Making it an independent line means it would run either way, using an else means it will run if both preceding conditions are false.
	print "We can't decide" 
	
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses: #this is broken since it is run independently of the previous ifs.
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

if (cars + buses) < people: #determines if combined resources can transport everyone
	print "There's not enough total for each person to have a personal vehicle"
elif ((cars + buses) >= people and cars >= people): #determines if there are ample cars for everyone to use their own. The statement before the and statement is actually already evaluated in the if statement so it really wasn't necessary..
	print "Everyone can take a personal car"
else: # if there are enough cars (evaluated in first statement), but the elif was not True, we know buses will be necessary.
	print "Buses will be needed, cars are not sufficient"
	
# Study Drill
# 1 elif - evaluates if the first if is False as a new if statement. else - evaluates if previous if and elif statements are all False.
# 2 Changed all to 50. It will run all the else: statements. Tested... correct.
# 3 Added lines 25 to 30 to determine if we can make it and if everyone can have a personal car or if buses will employed.
# 4 Descriptions written for what each line does