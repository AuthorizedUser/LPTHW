from sys import argv

nameof, first, second = argv #apparently does not matter what string you used for the 'script' name. It can be any word.

print "The script is called:", nameof
print "Your first variable is:", first
print "Your second variable is:", second
third = raw_input("What would a third variable be named? ")
print "Your third variable is:", third

# Study Drill
# 1 the argv argument variable seems to require the script to receive all of it's arguments at runtime. All arguments need to be specified for it to unpack.
# 2 removed the third. It works fine now.
# 3 add a raw_input
# 4 Modules give you features. Modules like sys.