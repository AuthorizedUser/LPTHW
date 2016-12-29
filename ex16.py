from sys import argv #import argument variable argv from sys module

script, filename = argv #assign script name to argv[0] and filename (command line argument) to argv[1] 

print "We're going to erase %r." % filename #some printed lines
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") #raw input with no string stored to a name. Gives a user an opportunity to terminate the script

print "Opening the file..."
target = open(filename, 'w') #open the file with write priviledges	

# print target.read() does not work in 'w' mode.

#print "Truncating the file. Goodbye!"
#target.truncate() #truncates the file completely since the file is currently at the starting position

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") #inputs lines of string into names
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1) #uses the file.write() method to write lines to the file. Could have simply used writelines()
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

writetarget = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(writetarget)

# target.writelines(line1 + "\n" + line2 + "\n")

print "And finally, we close it."
target.close()

# Study Drills
# 1 Comment on lines above
# 2 Script that reads the previous exercise is ex16a.py
# 3 Lines 32-33 combine lines 25 through 30 and uses the write() command and formats instead of writelines
# 4 w was passed as an extra parameter to open since we wanted to write to the file. w is a 'mode'. There are modes 'r', 'U' (terminates line where \n (unix) \r\n (windows), \r (mac) exist), 'w', 'a' (appending) and can add modes 'b' (binary mode) or '+' (updating). The '+' is best to use since it opens for both reading and writing.
# 5 Python already truncated the file since it was opened with 'w' mode. 'a' would append to the end of the file