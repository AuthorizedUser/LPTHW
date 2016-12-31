the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
# elements = range(0,6) Can simply assign range to the variable instead of use the loop
# now we can print them out too
for i in elements:
	print "Element was: %d" % i
	
# Study Drills
# 1 Range(x, y) creates a list from x to y - 1. An optional third argument provides the step size from number to number.
# 2 Yes. Tested.
# 3 List data type has been added to my notes. There is append, count, pop, extend, sort, index, remove, insert, reverse... The details of these functions have been studied and added to my google docs notes. There is further documentation about using lists as a queue, but I stopped after the stack discussion.
# Student question: 2d list... a list inside a list [[1,2],[3,4]]. Looks like it could get messy...
# In some languages lists are called arrays. In others arrays are something entirely different.
