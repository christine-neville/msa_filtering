"""Removes columns with less than X% occupancy from an msa.

Usage: python remove_cols.py <in-msa> <threshold> <out-msa>"""

import numpy as np
import sys

infile = sys.argv[1]
threshold = float(sys.argv[2])
outfile = sys.argv[3]

msa = open(infile).read().split(">")[1:]
seq1 = "".join(msa[0].split("\n")[1:])
nseqs = len(msa)
npos = len(seq1)
occmat = np.empty((nseqs,npos))
for i in range(len(msa)):
    seq = "".join(msa[i].split("\n")[1:])
    for j in range(len(seq)):
        if seq[j] == "-":
            occmat[i,j] = 0.0
        else:
            occmat[i,j] = 1.0
colsums = occmat.sum(axis=0)
percent_occ = colsums/nseqs
highocc = []
for x in range(len(percent_occ)):
    if percent_occ[x] > threshold:
        highocc.append(x)
        
outfile = open(outfile,'w')
for entry in msa:
    entry = entry.split("\n")
    title = ">"+entry[0]
    seqold = "".join(entry[1:])
    seqnew = ""
    for x in highocc:
        seqnew += seqold[x]
    nentry = title + "\n" + seqnew + "\n"
    outfile.write(nentry)
outfile.close()

print("Complete: %d columns remaining"%len(highocc))
