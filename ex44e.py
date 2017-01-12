#
class Other(object):

	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object): #no longer a subclass

	def __init__(self):
		self.other = Other() #an instance of Other() is-a attribute of Child
		#Child has-a instance of Other()
		
	def implicit(self):
		self.other.implicit()

	def override(self): #is-a function of Child(). a similar function is in Other()
		print "CHILD override()"

	def altered(self): #a child function that calls another object function
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

	
son = Child()

son.implicit()
son.override()
son.altered()

# Study drill - read pep-0008