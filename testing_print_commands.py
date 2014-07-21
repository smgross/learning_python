#!/usr/bin/env python
import sys

letters = ["a","b","c"]


# the default is to print a space before the value, even when a comma is used to prevent line breaks

for s in letters:
	print s,

print "\nTHat was wrong!\nI didn't want any spaces there."

#using the sys module to print without confounding spaces

for s in letters:
	sys.stdout.write(s),

sys.stdout.write("\n")




