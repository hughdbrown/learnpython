"""
Given a file in the following format:

GATAGGAGTAGTGAGT
GTAGTAGAGTATGATAGTGTA
GATTAGATGATGATG
GATATATAGATATATTAGAT
GATAGATAGT
GATTAAGATATGATAGTAG
GATTAGATAGTAGTAGT
GTATAGATAGTAGTAGTGATGA
GTAGATGATGATAGTAGTAGT
GAAGTAGTGATGAGTAG

For every position in the string, find the breakdown (in percentage) for each symbol encountered. The goal of this exercise is to calculate the population percentages for each symbol in each position, i.e.: what percentage of times do I see symbol X in position Y? From the example input data, we would arrive at the following percentages:
 
Position: 1 (A: 0%,  C: 0%, G: 100%, T: 0%)
"""
from __future__ import division
from collections import Counter
from itertools import izip_longest

def summarize(c):
	remove_none = {k: v for k, v in c.items() if k is not None}
	total = sum(remove_none.values())
	return {k: v / total for k, v in remove_none.items()}

def gattaca(d):
	transpose = izip_longest(*d)
	counters = [Counter(t) for t in transpose]
	return [summarize(c) for c in counters]

def gattaca_file(filename):
	with open(filename) as f:
		d = [line.strip() for line in f]
	return gattaca(d)

if __name__ == '__main__':
	from pprint import pprint
	data = [
		"GATAGGAGTAGTGAGT",
		"GTAGTAGAGTATGATAGTGTA",
		"GATTAGATGATGATG",
		"GATATATAGATATATTAGAT",
		"GATAGATAGT",
		"GATTAAGATATGATAGTAG",
		"GATTAGATAGTAGTAGT",
		"GTATAGATAGTAGTAGTGATGA",
		"GTAGATGATGATAGTAGTAGT",
		"GAAGTAGTGATGAGTAG",
	]
	g = gattaca(data)
	pprint(g)
