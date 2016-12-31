from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = int(raw_input("> "))
	if isinstance(next, int): #this doesn't make sense... some numbers contain neither. 999 for instance. It's asking for a string here as well... so I'm assuming it wants one digit in the name.
		how_much = int(next) #turn the input string into an integer
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0) #per python help, will exit the program with a 0 exit status.
	else:
		dead("You greedy bastard!") # Doesn't really end up making the player feel they died since the dead() method says "good job!"

		
def bear_room():
	print "\nThere is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True: #appears like a never-ending while loop. Will need to use the exit method to get out of the program from this one
		next = raw_input("\n1. take honey\n2. taunt bear\n3. open door\n\n> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved: #excellent way to use the not statement... after an and statement. Bear_moved must be false to keep the and statement true.
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True #skips the rest of the if statement since this condition was satisfied, and the while-loop restarts... the only difference being that the bear has now moved
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		elif next == "open door" and not bear_moved: #added this to help it make more sense
			print "The bear is in the way of the door."
		else:
			print "I got no idea what that means." #restarts the loop
	
	
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next: #good way to read the variable, it uses 'in' so you could have a space before or after or some other kind of minor spelling error
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room() #So it loops back by calling the function again


def dead(why):
	print why, "Good job!"
	exit(0) #no need to use sys.exit since we imported only exit from the sys module... not the entire sys module like "import sys" I need to test if import sys.exit would work. TEST: import sys.exit does NOT work.
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if "left" in next:
		bear_room()
	elif "right" in next:
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
		
start()

# Study Drills
# 1 map of game - ex35diagram.pdf
# 2 mistakes have been fixed except for a few formatting disagreements with the author
# 3 Comments have been made for unknown functions such as sys.exit. This was researched and added to notes. Exits the interpreter and returns a status
# 4 Added an elif statement for the bear being in the way of the door. Simplified some of the == if statements to have an "in" instead. Would be a good idea to add alternate answers in the bear room for the numbering system, but no need for this exercise.
# 5 It only accepts numbers below 50 with '0' or '1' present. I used the isintance() function to check if it is an integer, and went a step further by using int() on the raw_input line.

	