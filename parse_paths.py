#!/bin/python

import sys

try:
       fname = sys.argv[1]
except:
       sys.stderr.write("Usage: \n")
       sys.exit(1)

f = open(fname)
for line in f:
	sys.stdout.write('\t'.join([str(line.split("/")[-1])]))



