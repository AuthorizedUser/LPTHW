tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a %d\n line."
backslash_cat = "I'm \\ a \\ \r %s cat." #overwrote for study drill 3

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat % 10
print backslash_cat % tabby_cat
print fat_cat

# Study Drills
# 1 No flash cards, I'll come back and memorize them
# 2 ''' works as well as """. I cannot see a reason to use either one over the other
# 3 modified backslash cat to include carriage return and overwrite.
# 4 use %r (literal) format with double and single string escapes. See below

print "%r hello what's %r" % ('hi',"\"up\"\n")
print "%s hello what's %s" % ('hi',"\"up\"")