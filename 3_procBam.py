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

parser = argparse.ArgumentParser(description='Process BAM File(s)')

### required args
parser.add_argument('-c', '--chromsize', help='Chrom Sizes', required=True)
parser.add_argument('-a', '--aln', help='BAM Files', nargs='+', required=True)
parser.add_argument('-b', '--bed', help='Bin BED File', required=True)
parser.add_argument('-o', '--out', help='Output File', required=True)

### optional args
parser.add_argument('--min', help='Minimum Insert Size', required=False, default=100)
parser.add_argument('--max', help='Maximum Insert Size', required=False, default=1000)

args = parser.parse_args()

if __name__ == "__main__": core.proc_bam(bamFiles=args.aln,
                                         bedFile=args.bed,
                                         chromSize=args.chromsize,
                                         fileOut=args.out,
                                         minSize=args.min,
                                         maxSize=args.max)
