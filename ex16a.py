from sys import argv

script, filename = argv
contents = open(filename)

print "Below are the contents of %s." % filename,
raw_input("Press enter to continue")

print ("\n%s: " + "\n") % filename

print contents.read()

