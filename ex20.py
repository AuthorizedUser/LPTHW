from sys import argv

script, input_file = argv

def print_all(f): #prints the argument file object using read()
	print f.read()
	
def rewind(f): #rewinds the I/O to the zero position in the file object argument
	f.seek(0)
	
def print_a_line(line_count, f): # print which line is being read, then runs a 'readline()' starting at the top.
	print line_count, f.readline(), #reads one line at a time, advancing the I/0. It begin after beind rewound. added a comma at the end to bring the lines together since readline is already adding an extra \n

current_file = open(input_file) #names the opened input file

print "First let's print the whole file: \n"

print_all(current_file)

print "\nNow let's rewind, kind of like a tape."

rewind(current_file)

print "\nLet's print three lines:\n"

current_line = 1 # assigns a current line name. This will be incremented. we know the first line is the first since we rewound the i/o to the first line
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# Study Drills
# 1 Write lines to explain what is going on
# 2 Explain in commments what current line and line count are.
# 3 Check function arguments.
# 4 Seeks a location in the file. The second argument can be a 'relative' argument that specifies where you are seeking from. You can use os.SEEK_CUR or 1 for the current position. Os.SEEK_END brings it to the end. file.tell() gives the current position. Seek in append mode will move to the end any time write is invoked.
# 5 Rewrite using shorthand notation +=