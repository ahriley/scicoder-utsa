#!/usr/bin/env python

'''
Regular Expressions Exercise 2:

Read email list file (data/random_name_list.txt), write a new file with the
data in this format (spaces between) using regular expressions:

<email> first_name last_name
'''

import re

infile = 'data/random_name_list.txt'
outfile = 'output/random_name_list2.txt'

with open(infile) as data, open(outfile,'w+') as out:
    for line in data:
        if line[0] == "#":
            continue
        m = re.match("([a-zA-Z]+\s)([a-zA-Z\-]+\s*)([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", line)
        assert m is not None, "The pattern was not matched"

        first = m.group(1).strip()
        last = m.group(2).strip()
        email = m.group(3).strip()

        out.write(email+" "+first+" "+last+"\n")
