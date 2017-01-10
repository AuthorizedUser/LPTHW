# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	def func1(self):
		print "This function is in class Animal."
	
## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a attribute name that is initialized by function __init__
		self.name = name
		
	def func(self):
		print "This function is in class dog(animal)." #DOUBLE MISTAKE... LEFT OFF END QUOTE
		print "Name of the dog is %r" % self.name
		
		
## Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a attribute name
		self.name = name
		
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a attribute name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
	def func(self):
		print "This function is in class person"
		print "The person is named %r and their pet is %r" % (self.name, self.pet.name)
		
## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a name and a salary
		super(Employee, self).__init__(name)
		## Person has-a name
		self.salary = salary #salary is only part of the employee subclass
		
## Class Fish is-a object
class Fish(object):
	pass
	
## Class Salmon is-a fish
class Salmon(Fish):
	pass
	
## Class Halibut is-a fish
class Halibut(Fish):
	pass
	
## rover is-a dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## Mary has-a pet named satan
mary.pet = satan # so attribute is another object...

# Frank is-a employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## Frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon()
crouse = Salmon()

## harry is-a Halibut()
harry = Halibut()

# STUDY DRILLS

# 1 Why object class exists: New style classes inherit from object (for 2.7 and 3)
# New-Style classes can store slots and descriptors. __slots__ can be used to
# declare class attributes using only as much memory as needed. Normal
# objects will declare __dict__ for class attributes which has a
# standard  size that is much greater. There are many other features to
# new-style classes, but they must inherit from object to have those features.
# This allows old-style classes to still function

# 2 Yes. It creates a 'class' object rather than an instance object. This can be
# accomplished by setting a variable equal to Class without the ()

# 3 Functions in base class vs inherited class
print "-" * 5		
animalobj = Animal()
animalobj.func1()
print "-" * 5
dogobj = Dog("Fido")
dogobj.func()
print "-" * 5
personobj = Person("Joe")
personobj.pet = dogobj
personobj.func()
print "-" * 5
Animal().func1()
Dog("Fido").func1()

# All subclasses inherit the base class' function

# 4 Did this in exercise for ex41... for the tiles.py module

# 5 adding a list of pets
print "-" * 10
Alyssa = Person("Alyssa")
Winston = Dog("Winston")
Khloe = Cat("Khloe")
pets = [Winston, Khloe]
Alyssa.pet = pets
for entry in Alyssa.pet:

	print "Alyssa has a %r named %r." % (entry.__class__.__name__, entry.name)

#could have just used a list... I wanted to use the objects in the format

# 6 is-many may refer to a subclass that has inherited more than one parent class
# for instance class hybrid(cat, dog):. The problem with multiple inheritance
# is that it can cause conflicts with the python MRO (method resolution order).
# Particularly, when the inheritance crosses paths several times
# it can cause confusion about what __init__ to use. and how
# super() will pass arguments up

# super(Employee, self).__init__(name) is used to run the __init__ of the parent
# class for the arguments that pass to the parent class (first arguments).
# super can also run the parent's functions