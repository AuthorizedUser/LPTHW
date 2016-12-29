def cheese_and_crackers(cheese_count, boxes_of_crackers): #creates the crackers and cheese function
	print "You have %d cheeses!" % cheese_count #prints text with an argument as a format
	print "You have %d boxes of crackers!" % boxes_of_crackers # text with argument as format
	print "Man that's enough for a party!" #prints text
	print "Get a blanket. \n" # prints text
	
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) #places arguments directly into function when called


print "OR, we can use variables from our script:"
amount_of_cheese = 10 # define names to be passed into function
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #calls function with names as arguments

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #uses expressions as arguments when calling the function


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #uses names and expressions as arguments when calling the function

# Study Drills
# 1 Comments on each line
# 2 Read lines backwards
# 3 

def giantmonkey(size, attitude):
	print "The %s monkey tends to act %s" % (size, attitude)

giantmonkey("large", "mean") #1

size = "large"
attitude = "ferocious"

giantmonkey(size,attitude) #2

size_monkey = size
attitude_monkey = attitude
giantmonkey(size_monkey, attitude_monkey) #3

giantmonkey("big" + " old", "friendly") #4

giantmonkey("integer-like", 10 + 5) #5

giantmonkey("%s" % "format", "nice") #6

def appendfile(file, newdata):
	raw_input("This function will append \"%s\" to \"%s\". Hit enter to continue or CTRL-C to exit" % (newdata, file))
	writable = open(file, 'a+')
	writable.writelines("\n" + newdata)

#filename = raw_input("Enter the file to append to: ")
#newdataname = raw_input("Enter the new line to append: ")
#appendfile(filename, newdataname) #7

#appendfile("ex19_sample.txt", "Append string") #8

#appendfile("ex19_sample.txt", "append format %s" % "format") #9

#integer = 10 + 5

#appendfile("ex19_sample.txt", str(integer)) #10 CANNOT CONCATENATE INT OBJECTS WITHOUT FIRST USING STR()

appendfile("ex19_sample.txt", raw_input("Enter a string: ")) #can include a raw input for the arguments to a function