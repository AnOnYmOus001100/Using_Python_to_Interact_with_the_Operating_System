#!/usr/bin/env python3

#imorting necessary modules
import sys
import subprocess

#opening file from  first command line argument as oldFiles.txt is stored in sys.argv[1]
file = open(sys.argv[1], "r")
for line in file.readlines():
	old_name = line.strip()
	#replacing jane by jdoe in string
	new_name = old_name.replace("jane", "jdoe")
	#renaming file by invoking run function of subprocess and passing as arguments, mv source destination passed as list and the old and new names
	subprocess.run(["mv",old_name,new_name])
file.close()

