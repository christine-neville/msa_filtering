"""Replaces unwanted characters in MSA with gaps.
Usage: python <msafile> <unwanted characters, e.g. XZB> > outfile"""

import sys

infile = sys.argv[1]
badchars = sys.argv[2]

inmsa = open(infile,'r').read().split(">")[1:]
for line in inmsa:
    line = line.split("\n")
    title = line[0]
    seq = "".join(line[1:])
    for c in badchars:
        seq = seq.replace(c,"-")
    print(">"+title)
    print(seq)
