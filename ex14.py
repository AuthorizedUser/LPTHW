from sys import argv

script, user_name, favorite_color = argv
prompt = '????? >>> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
print "I know you like the color %s" % favorite_color
likes = raw_input (prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
And your favorite color is %s.
""" % (likes, lives, computer, favorite_color)

# Study Drills
# 1 I know what Zork is. I'm the zork master
# 2 Changed prompt
# 3 Added the favorite color command line argument
# 4 Makes sense to combine """ and a format activator. Clearly, it needs to be in the same line as the final """