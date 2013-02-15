#!/usr/bin/env python

import json, sys, unicodecsv

__author__ = "alexrockt"
__credits__ = ["StackOverflow"]
__version__ = "1.0"
__maintainer__ = "alexrockt"
__email__ = "alex@dfghj.de"


# Thanks to StackOverflow
# http://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

# get the filename from the arguments
filename = sys.argv[1]

# open the file and skip first line to get correct json entry point, due to special twitter format of the js file
input = open(filename)
input.readline()
data = json.load(input)
input.close()

# create a output file 
out = open(filename[:-2]+"csv","wb")

output = unicodecsv.writer(out, encoding='utf-8')
output.writerow(["id"]+["timestamp"]+["tweet"])
for row in data:
	output.writerow([row["id"],row["created_at"],row["text"].replace("\n"," ")])

out.close()
