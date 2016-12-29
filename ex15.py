from sys import argv #imports argv argument variable from the sys module

script, filename = argv #names the script and filename names based on the arguments passed in the command line

txt = open(filename) #populates the text name by opening the file
txt.seek(20)
print txt.tell()
print "Here's your file %r:" % filename #Simple text line naming the file passed as an argument
print txt.read() #performs the read function() from the txt name (or object?)

print "Type the filename again:" # simple text line
file_again = raw_input("> ") #prompts the user for input

txt_again = open(file_again) #populates another name by opening the user-supplied file

print txt_again.read() #again reads the file that was entered

txt.close()
txt_again.close()

# Study Drills
# 1 Comments on what each line does
# 2 Open() returns an object of the "File" type. Clearly, the new names used in this script are now "objects" that contain functions. Option open() arguments include mode (read/write/append) and buffer. Read() contains an option size argument to limit the size to read.
# 3 Python official documents call read() a method of a file object. Open() is considered a built-in python function. sys module interacts with interpretter. One of it's "arguments" is the argv function. The sys module also contains many functions. argv[0] is the script name. So other argv arguments would be argv[1], argv[2], etc...
# 4 Commented out the second, user-input open and read
# 5 Commented out the command-line argument file input and ran script. python does not bug because of the arguments passed at the command line.
# 6 close() before the read command returned an error for trying to read a closed file. Fileno() returned file '3' integer. flush() returned 'none'. isatty() returned false. next() returned an error about mixing iteration and read methods. Readline() returned a line string then eliminated a line from the final output each time it was used. Readlines() read all lines literally and printed them to one line on the command line. seek(20) advanced the file by 20 characters - it only printed remaining characters after these 20. tell() told us what position the file had been read to (20). txt.truncate() did not work since the file has not been opened in write mode. I assume it would truncate the file to (20) if it was. write() and writelines() will probably also need write mode. xreadlines() is for backwards compatibility.
# 7 Running open() command in python prompt requires quotes around the sample filename.
# 8 Added a close() method.