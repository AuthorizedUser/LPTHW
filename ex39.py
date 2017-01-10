# create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
} # apparently can use this format to populate a dictionary... and maybe other 
# things as well
# create a basic set of states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10 # prints a big format bar
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']] #uses value from states as key for cities
print "Florida has: ", cities[states['Florida']]
print '-' * 10
for state, abbrev in states.items(): #returns a two level list object of dictionary items
	print "%s is abbreviated %s" % (state, abbrev) #order has changed...

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviate %s and has city %s" % (
		state, abbrev, cities[abbrev]) #uses the parentheses and city index tricks

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state: #state returns None, which evaluates to False
	print "Sorry, no Texas"
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist') #Returns the does not exist string
print "The city for the state 'TX' is: %s" % city

# Study Drills

# 1 
texas = {'Travis': 'Austin', 'Williams': 'Round Rock', 'Bastrop': 'Elgin'}

#2 
counties = texas.keys()
print "counties list : %s" % counties
cities = texas.values()
print "cities list : %s" % cities

texas2 = dict(zip(counties, cities))
print "texas2 from dict() and zipping: %s" % texas2
print '~' * 10
print "texas.items(): %s" % texas.items()
print '$' * 10
print "popping Williams county off dictionary: %s" % texas.pop('Williams')
print "checking for Bexar and setting default to \"San Antonio\"",
print "if it doesn't exist: %s" % texas.setdefault('Bexar', 'San Antonio')
print '~' * 10
popped = texas.popitem()
print "popitem() will randomly take an item off the dictionary: %r, %r" % (texas.popitem())
# provides two arguments, did not need to use #(popped[0], popped[1])
print '~' * 10
print "New Dictionary after popping and popiteming: %r" % texas


# 3 arbitrary order is one big issue with dictionaries. Cannot append or sort
# Can only sort returned lists. Cannot join or split. Can't use a range
print 'Exercise 3' + "~" * 10
print "Adding some new values"
texas['Houston'] = 'Crockett'
texas['Harris'] = 'Houston'
texas['Dallas'] = 'Dallas'
texas['Gillespie'] = 'Fredericksburg'
#texas[1] = 27
print "New dictionary %r" % texas
texaskeys = texas.keys()
texasvalues = texas.values()
texasviewkeys = texas.viewkeys()
print '~' * 15
print "Texas keys raw: \n %r" % texaskeys
print "Texas viewkeys version \n %r" % texasviewkeys
print "Texas values raw: \n %r" % texasvalues
texaskeys.sort() #MISTAKE tried adding this as a format... does not 'return' anything
texasvalues.sort() #only returns None
print "Texas keys sorted: \n %r" % texaskeys
print "Texas .viewkeys version: \n %r" % texasviewkeys
print "Texas values sorted: \n %r" % texasvalues
print "~" * 10 + "\n Now, to zip the list together...\n"
texaszipped = zip(texaskeys, texasvalues)
print "Zipped list: \n %r" % texaszipped
texaszippeddict = dict(texaszipped)
print "Zipped list as dictionary:\n %r" % texaszippeddict
print "~" * 10 #MISTAKE ABOVE. [1] NEEDS TO BE AFTER KEYS, NOT IN ARGUMENT
print "length of dict: %r" % len(texaszippeddict)
print "Now, deleting the key in the second value of texaszippeddict.keys().. %r" % texaszippeddict.keys()[1]
del texaszippeddict[texaszippeddict.keys()[1]] #returns the second key and deletes it
print "Again, printing the zipped list with the 2nd key deleted: \n %r" % texaszippeddict
print "new length of dict: %r" % len(texaszippeddict)
print "Checking if 'Bexar' is in dictionary: %r" % ('Bexar' in texaszippeddict)
print "printing dictionary again to check order after check statement: \n %r" % texaszippeddict
print "adding a value..."
texaszippeddict['McLennan'] = "Waco"
print "printing again to check order: \n %r" % texaszippeddict
#oddly, it transposed the last two dictionary items before appending the new one

