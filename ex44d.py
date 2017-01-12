#
class Parent(object):

	def override(self):
		print "PARENT override()"
		
	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self): #over-writes the parent function
		print "CHILD override()"

	def altered(self): #a child function that calls a parent function
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

	
dad = Parent()
son = Child()

dad.implicit() #will evaluate the same in both. Son inherited the method
son.implicit()

dad.override() # will evaluate differently since son overrode the method
son.override()

dad.altered() # will evaluate altered, and internally evaluate the parent method
son.altered()
