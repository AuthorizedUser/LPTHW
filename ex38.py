ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') #accidentally used an underscore before split
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # will count the length of the ten_things... which is only 6
	# condition is that it must not be equal to 10... so if it is more or less it keeps popping
	# off of the more_stuff list
	next_one = more_stuff.pop() #pops the last item off list.. starting with "Boy"
	print "Adding: ", next_one 
	stuff.append(next_one) # adds "Boy" to the end of the stuff list that has 6 things
	print "There's %d items now." % len(stuff) # returns current length, last will be 10
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] #prints 2nd item of stuff... oranges
print stuff[-1] #prints last item of stuff
print stuff.pop() #pops the last off of stuff[] and prints it
print ' '.join(stuff) #new function in string type. Looks like it will join
#the list together with spaces in the center
print '#'.join(stuff[3:5]) #looks like it will join the list together with #'s
# in the center. The actual list object 'stuff' has not bee modified
# except for the pop statement, which will actually modify the object
# stuff[3:5] is a range from 3 to 5, not including 5.... be careful with max of range

# Study Drills

# 1 stuff = ten_things.split(' '). Python looks up the stuff name, sees that it
# is empty. Python sees the equals and knows it will be assigned the value on
# the right side of the sign. It sees the ten_things list object. At the
# period, it knows an attribute of list() will be called, so it looks those up
# it matches the split() method as a list() attribute. It takes the argument ' '
# and uses it alongside split on the ten_things list instance.
# Other iterable type methods... pop, append
# other string type methods. join
# built-in non type methods... len

# 2 ten_things.split(' ') is a way to say... split the ten things list using a
# space as the seperator

# 3 Have done ample reading on OOP. There is alot to learn... basically class >
# object > instance. I am still learning the nuances and wrapping my head
# around the whole concept

# 4 Have read the python documentation on what a class is. Classes contain attributes
# aka. methods and names. These attributes can be part of the object when a
# class is instantiated. Classes can use the __init__ function to self-initialize
# when they are assigned as an object instance and can be passed arguments.
# objects/instances follow the 'blueprint' of the class.

# 5 dir(object) will provide all the attributes of that object and of it's base
# type. It is showing the methods and attributes of the base class as well as the
# instance itself.

# 6 Looking up functional programming... assuming it is non-OOP... probably
# use on very specific applications and spaceships, etc
# Read up on functional programming. I'm never going to complain about OOP
# again