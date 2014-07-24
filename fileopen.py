#!/usr/bin/env python

import sys
import re
import os.path



####
# Testing some variables, putting them in a list
# opening a file
# reading the file, using regular expressions to find blank lines
# printing the file to screen.
# joining lists
####


sys.stdout.write("Hello\n")


# testing a few variables here

""" THis is a comment docstring. """
""" Don't ever use this again
	because it is really, really, ugly
	"""

firstname = "Stephen"
son = "Bubba"


namelist = [firstname, son]


for i in namelist:
	print "I see %s " % i 
	
for i in namelist:
	print "Testing comma in  a different spot %s " %i ,
	
print "\n"
print "I'm now on this line"

# Reading a file

filename = raw_input("Enter in a file: ")
filename  = filename.strip()
print "You entered in %s " % filename

if os.path.isfile(filename) != True:
	print "That file doesn't exist"
	#And this is the ugly Python exit command:
	sys.exit()

file = open(filename, 'r')

for i in file:
	print i,


# Loop through the file again, see if it is still open
print "Is the filehandle still open???"

for i in file:
	splitline = i.split()
	print splitline[0],


print "No, the filehandle closed automatically"

#Reopen file handle

file = open(filename, 'r')

for i in file:
	print i,
	# conditional: skip if line is blank
	match = re.search("^\s*\n", i) 
	if (match):
		print "FOUND a match to blank line"
		continue
	else:
		print "Match failed, line is not blank"
	splitline = i.split()
	print splitline,
	#print splitline[0],
	
#Try this again
# THe following will open the file, put each line into a list
# and print the list
# omitting blank and comment lines


file = open (filename, 'r')

for i in file:
	match = re.search("^\s*\n|^#",i)
	if (match):
		continue
	else:
		splitline = i.split()
		print splitline[0],
		#and print the rest of the line, but joined as a string
		# This is a really awkward way to join a list
		# there is no join function for lists, so it is "joiner".join.(list)
		# There should be a joiner function for lists!?
		print "--Perl is better at this than Python--".join(splitline)
		


	

	



