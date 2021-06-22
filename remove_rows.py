"""Removes sequences from MSA if those sequences are more than X% gaps.

Usage: python remove_rows.py <in-msa> <threshold> <out-msa>"""

import sys

infile = sys.argv[1]
threshold = float(sys.argv[2])
outfile = sys.argv[3]

seqcounter = 0

outmsa = open(outfile,'w')
inmsa = open(infile,'r').read().split(">")[1:]
for line in inmsa:
    line = line.split("\n")
    title = line[0]
    seq = "".join(line[1:])
    pos = len(seq)
    gaps = seq.count("-")
    if gaps/pos < threshold:
        outmsa.write(">"+title+"\n"+seq+"\n")
        seqcounter += 1

print("Complete: %d sequences remaining"%seqcounter)
        
    
    
    
