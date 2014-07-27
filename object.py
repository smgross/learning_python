#!/bin/env python
import sys
import re
import os.path


class Animal(object):
	"""
	THis is an example from Treading on Python Volume 1
	"""
	
	def __init__(self,name):
		self.name = name
		
	def talk(self):
		"""
		Make the beast talk
		"""
		print "Generic animal sound!"
	
	### How do I print the name passed into the object constructor?
	
	#Following code does not work!
	#def printname(name):
	#	print "Name is %s" % name
	#	print name
	#	print "self.name is %s " % self.name
		
	
	def printself(self):
		#print "Self is %s" % self
		#print self
		print "self.name is %s " % self.name
		

# The following is a subclass

class Dog(Animal):
	def talk(self):
		print "%s says 'Bark, bark!'" % self.name
		
class Cat(Animal):
	def talk(self):
		print "%s says 'Meow, meow!'" % self.name



print "\nInvoking Animal, a creature called 'Thing1'"
creature = Animal("Thing1")

creature.talk()

creature.printself()


print "\nIvoking Animal, an iguana named 'Freddy'"

iguana = Animal("Freddy")

iguana.printself()


print "\nInvoking Dog, a dog named 'Zephyr'"

zephyr = Dog("Zephyr")
zephyr.talk()
zephyr.printself()


print "\nInvoking Cat, a cat name 'Kitty'"

kitty = Cat("Kitty")
kitty.talk()
kitty.printself()




