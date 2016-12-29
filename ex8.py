formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) #Prints decimals
print formatter % ("one", "two", "three", "four") #prints strings as literal with quotes around them
print formatter % (True, False, False, True) #prints booleans as literals with no quotes
print formatter % (formatter, formatter, formatter, formatter) #prints formatter name as a literal string, showing formatters, etc
print formatter % ( #appears to split the argument across multiple lines using tabs
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
 #I'm going to assume the tab means that these lines are on the 'same line'. The tab appears to be format-only and doesn't affect the print command. The parentheses can also be moved and doesn't seem to affect it. tab DOES seem to affect the output in an error when a command is tabbed forward

#Study Drills
# 1 no major mistakes
# 2 It appears that entering a single quote into a literal format will result in a double quote print output since python wants to distinguish which quotes are for the string itself. After testing, you CANNOT have both quote types within a string.