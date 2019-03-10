#!/usr/bin/python

__author__ = "Donghoon Lee"
__copyright__ = "Copyright 2019, Gerstein Lab"
__credits__ = ["Donghoon Lee"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Donghoon Lee"
__email__ = "donghoon.lee@yale.edu"

import argparse
import core

### LOAD ARGs ###

parser = argparse.ArgumentParser(description='Make Bin in BED Format')

### required args
parser.add_argument('-c', '--chromsize', help='Chrom Sizes', required=True)
parser.add_argument('-x', '--blacklist', help='Blacklist Region in BED format', required=True)
parser.add_argument('-o', '--out', help='Output File', required=True)

### optional args
parser.add_argument('-l', '--length', help='Bin Length', required=False, default=500)
parser.add_argument('-s', '--step', help='Step Size', required=False, default=100)

args = parser.parse_args()

if __name__ == "__main__": core.make_bin(chromSize=args.chromsize,
                                         binLength=args.length,
                                         stepSize=args.step,
                                         blackList=args.blacklist,
                                         fileOut=args.out)
