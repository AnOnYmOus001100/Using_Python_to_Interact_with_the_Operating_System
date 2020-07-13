#!/usr/bin/env python3

def charcter_frequency(filename):
	"""Counts the frequency of each character in the given file."""
	# first try to open the file
	try:
		f = open(filename)
	except OSError:
		return None

	# Now process the file
	characters = {}
	for line in f:
		for char in line:
			characters[char] = characters.get(char,0) + 1
	f.close()()
	return characters
