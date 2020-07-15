#!/usr/bin/env python3

import re
import csv
import operator
import sys

per_user = {}
errors ={}

logfile = 'syslog.log'
file = open(logfile, 'r')

errorfile = 'error_message.csv'
userfile = 'user_statistics.csv'

for log in file:
	result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]? ?\((.*)\)$", log)
	if result.group(2) not in errors.keys():
		errors[result.group(2)] = 0
	errors[result.group(2)] += 1
	if result.group(3) not in per_user.keys():
		per_user[result.group(3)] = {}
		per_user[result.group(3)]["INFO"] = 0
		per_user[result.group(3)]["ERROR"] = 0

	if result.group(1) == "INFO":
		per_user[result.group(3)]["INFO"] += 1
	elif result.group(1) == "ERROR":
		per_user[result.group(3)]["ERROR"] += 1

errors = sorted(errors.items(), key = operator.itemgetter(1), reverse  = True)
per_user = sorted(per_user.items())

file.close()
errors.insert(0, ('Error', 'Count'))

file = open(errorfile, 'w')
for error in errors:
	a,b = error
	file.write(str(a)+','+str(b)+'\n')
file.close()

file = open(userfile, 'w')
file.write("Username,INFO,ERROR\n")
for stats in per_user:
	a, b = stats
	file.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')
file.close()

