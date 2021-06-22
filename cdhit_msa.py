"""Cuts existing MSA down to cluster representatives as identified by cd-hit.

Usage: python cdhit_msa.py <big msa> <.clstr file from cdhit> <outfile>"""

import sys

infilename = sys.argv[1]
clustfilename = sys.argv[2]
outfilename = sys.argv[3]

seqfile = open(infilename).read().split(">")[1:]
reps = []
clusters = open(clustfilename).read().split(">Cluster")[1:]
for cluster in clusters:
    cluster = cluster.split("\n")
    for i in cluster:
        if "*" in i:
            rep = i
    reps.append(rep)
newaccs = [r.split()[2] for r in reps]

newfile = open(outfilename,'w')
accs = [n[1:-3] for n in newaccs]
for acc in accs:
    for seq in seqfile:
        if acc in seq:
            newfile.write(">"+seq)
newfile.close()
