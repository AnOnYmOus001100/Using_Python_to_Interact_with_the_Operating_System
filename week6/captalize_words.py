#!/usr/bin/env python3

import sys

for line in sys.stdin:
	words = line.strip().split()
	print (" ".join([word.capitalize() for word in words]))
