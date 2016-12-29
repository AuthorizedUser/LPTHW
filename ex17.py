from sys import argv
from os.path import exists #OS.PATH include some filename manipulations. OS module provides some OS dependent functionality

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file) #Treats file objects as strings when used with no method

# we could do these two on one line too, how?
#in_file = open(from_file)
#indata = in_file.read() #combined on line 20

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file) Test: If the file does not exist an error is returned OS.PATH.EXISTS is a function of the operating system and will look at that path to see if the file exists.
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()
open(to_file, 'w').write(open(from_file).read()) #trying to shorten this as much as possible
#out_file = open(to_file, 'w'); out_file.write(in_file.read())
#out_file.write(indata) #Combined on line 19

#print "Alright, all done."

#out_file.close()
#in_file.close()

# Study Drill
# 1 Python import "statement". import searches for a module, then binds the results to a name. It uses some interpretter functions to do so. Search strategies that python uses can be modified and extended using 'hooks'. Python contains "Packages" (containers) of modules. Packages are considered a module as well (and subpackages). Packages are seperated by dots, e.g. "os.path". All modules previously imported are kept in the module cache, sys.modules. This is the first location checked in search. Python uses a  'finder' to find the modules then a 'loader' to load them.
# Can use ">import module.module as modulename" to assign a name to a module. If the module is not a top level module, then the name of the top level package is bound in the local namespace
# Can use ">from module.submodule import identifier" will import the identifier or submodule with that name. Can also include an 'as' to rename the identifier. This means we can type 'argv' in the script rather than 'sys.argv' after importing the sys module. Can include a wildcard '*' to import all names from the submodule. Can use "..." to move up one module level when importing. For instance, ">from ..subpkg2 import mod" from within pkg.subpkg1 will import pkg.subpkg2.mod.
# 2 Remove annoying features by commenting out
# 3 Shortened some of the lines. Line 17 combined the read and writes.
# 4 cat is the same as "Get-content" in powershell. It can combine multiple file outputs.
# 5 man and cat both exist in the new version of powershell. gci is the original for cat; help or get-help for man.
# 6 You don't need to close the files. The OS will do this for you when the python script is done. However, you can run into issues with re-using the filename, or with writing/reading simultaneously to the same file. close() is more of a good habit than anything. For persistently-running processes (server), an open file can eat up resources.