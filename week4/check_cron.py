#!/usr/bin/env python3

import re
import sys

logfile = sys.argv[1]i
usernames = {}
with open(logfile) as f:
	for line in f:
		if "CRON" not in line:
			continue
		pattern = r"USER \((\w+)\)$"
		result = re.search(pattern, line)	
		print (result[1])
		
		if result is None:
			continue
		name = result[1]
		usernames[name] = usernames.get(name,0) + 1
print (usrnames)
