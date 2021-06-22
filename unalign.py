"""Generates plain fasta file of aligned sequences for realignment; 
filters out sequences that are all gaps in the region considered.

Usage: python unalign.py <msa> <outfile>"""
import sys

alifile = sys.argv[1]
newfile = sys.argv[2]
afile = open(alifile).read().split(">")[1:]
outfile = open(newfile,'w')
for e in afile:
    e = e.split("\n")
    title = e[0]
    seq = "".join(e[1:])
    seq2 = ""
    for c in seq:
        if c != "-":
            seq2 = seq2 + c
    if len(seq2) > 1:
        outfile.write(">"+title+"\n"+seq2+"\n")
