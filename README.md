# msa_filtering
Code to filter MSA prior to use with neural network. This workflow performs phylogenetic filtering using cd-hit, then removes sequences from the MSA that have a gap percentage above a threshold, then reduces the MSA to columns that have a gap percentage below a threshold. 

See filtering_workflow.sh for commands to run entire workflow. See each individual script for usage instructions.

unalign.py: unaligns an MSA so that it can be run through cd-hit
cdhit_msa.py: cuts existing MSA down to cluster representatives as identified by cd-hit
remove_rows.py: removes sequences from MSA if those sequences are more than X% gaps
remove_cols.py: removes columns with less than X% occupancy from an MSA
replace_chars.py: replaces specified characters with gaps
