#!/usr/bin/env python

'''
Regular Expressions Exercise 3:

Given the spec-* files in the data/ directory, write a script that uses regular
expressions to list the three numbers in each filename to a new file where the
values are tab delimited, e.g.

4055 55359 0001

Hint: Look up the Python module "glob".
'''

import re
from glob import glob

files = glob('./data/spectra/spec*')
outfile = 'output/sdss_spec_regex.txt'

with open(outfile,'w+') as out:
    for fil in files:
        fil = fil.strip('./data/spectra/spec')
        m = re.match("-([0-9]+)-([0-9]+)-([0-9]+)\.",fil)
        assert m is not None, "The pattern was not matched"

        id = m.group(1), m.group(2), m.group(3)
        out.write(id[0]+"\t"+id[1]+"\t"+id[2]+'\n')
