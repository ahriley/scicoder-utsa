#!/usr/bin/env python

'''
Write a script that:

• reads the data file "sdss_spectra_links.txt"
• prints a random selection of URLs to the command line without duplicates

by providing the data file and number of URLs by command line (argparse).
'''

import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f")
parser.add_argument("-n")
args = parser.parse_args()

filename = args.f
randnum = int(args.n)

with open(filename) as spectra_links:
	lines = spectra_links.readlines()

links = [line.strip() for line in lines]
links_c = links.copy()

subset = [links_c.pop(np.random.randint(0, len(links_c))) for i in range(randnum)]

assert len(set(subset)) == len(subset)
printing = [print(link) for link in subset]
