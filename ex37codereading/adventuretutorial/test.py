print __name__
print "main module name above"

class firstclass():
	nameclass = __name__
	print "this is in the class %s" % nameclass
	def firstfunction(self):
		print "in the function printing it's name %s" % __name__
		print self.nameclass
		global nameclass2
		nameclass2 = __name__
		
obj = firstclass()

obj.firstfunction()

print nameclass2