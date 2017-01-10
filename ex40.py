class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics #Song.lyrics is lyrics argument

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line #looks like a for loop will decompose a string into characters

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
# Looks like we will be passing a list of strings into the argument
# so 'line' in the for loop will be individual strings
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
# these are both objects that are instances of the song class

happy_bday.sing_me_a_song() #uses the classes own function and attribute as
# an argument to that function

bulls_on_parade.sing_me_a_song()

# Study Drills

# 1 

Bearsonglist = ["He was a scary bear", "He was a hairy bear"]
Bear_song = Song(Bearsonglist)
Bear_song.sing_me_a_song()

# 2 Did in #1

# 3 
print "-" * 15
#adding a second list
Bearsongending = ["He was a beary bear"]

Bear_song_w_ending = Song(Bearsonglist + Bearsongending)
Bear_song_w_ending.sing_me_a_song()

# Learned I can pass multivariable arguments

print '-' * 15
# Using a string and dict
dict1 = {"bear": "Bearvalue"}
string1 = "BEAR!"

Bear_Song_Final = Song(dict1) #Dictionary in for loop will only print keys
Bear_Song_Final.sing_me_a_song()
print "-" * 5
Bearstring = Song(string1)
Bearstring.sing_me_a_song()

#4 Have read a ton on OOP so far and continue to...
