#Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" #\n is clearly a carriage return

print "Here are the days: ", days #the comma adds an extra space
print "Here are the months: ", months #the comma adds an extra space

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""" #clearly allows you to split a string accross multiple lines. The final carriage return on line 13 prints as a carriage return in the terminal output! Can include the termination quotes on line 13 to have no blank line at the end. The same at the beginning, a blank carriage return is included in output. MISTAKE 1: I accidentally capitalized print command. This was just after taking notes not to capitalize it...
	
# Study Drills
# 1 Mistakes noted
# NOTE: Carriage return escape character is \n
# NOTE: \n will not work when %r is used since it shows the literal string