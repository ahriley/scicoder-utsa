#!/usr/bin/env python

'''
Write a script that:

• reads the data file "sdss_spectra_links.txt"
• prints a random selection of URLs to the command line without duplicates
'''

import numpy as np

filename = 'data/sdss_spectra_links.txt'
randnum = 100

with open(filename) as spectra_links:
	lines = spectra_links.readlines()

links = [line.strip() for line in lines]
links_c = links.copy()

subset = [links_c.pop(np.random.randint(0, len(links_c))) for i in range(randnum)]

assert len(set(subset)) == len(subset)
printing = [print(link) for link in subset]
