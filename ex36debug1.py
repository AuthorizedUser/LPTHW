inv = []

print "You stumble into a clear forest pond."
print "You gaze into the clear water."

if "ruby" not in inv:
	print "There is a shining ruby at the bottom of the pond."
	print "You can wade in and grab the ruby."
else:
	print "There is nothing in the pond."

print "To the west is the trail that returns to the glade."


commandpond = raw_input("> ")
rubycomm = ["ruby", "Ruby", "pond", "wade", "grab"]
trailcomm = ["west", "trail", "return"]

print commandpond
if commandpond in trailcomm:
	print "test %r" % commandpond
	#print "\nYou walk back down the overgrown forest trail."
	#glade(inv)
elif commandpond in rubycomm:
	print "\nYou reach into the crystal clear water and grab the ruby."
	inv.append("ruby")
	pond(inv)
else:
	print "\nThat makes no sense."
	pond(inv)