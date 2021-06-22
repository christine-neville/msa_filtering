#!/bin/bash
# Workflow to reduce size/redundancy of MSA prior to use with neural network

python unalign.py PF00520_rp55.txt PF00520_rp55_unaligned.txt			                        #unalign prior to using cdhit
cdhit -i PF00520_rp55_unaligned.txt -o PF00520_95id -c 0.95 -T 6 -n 5 -g 1		                #run cdhit
python cdhit_msa.py PF00520_rp55.txt PF00520_95id.clstr PF00520_95id.fa		                    #cut msa down to cdhit cluster reps
python remove_rows.py PF00520_95id.fa 0.9 PF00520_95id_0.9rows.fa			                    #remove sequences that are more than 90% gaps
python remove_cols.py PF00520_95id_0.9rows.fa 0.9 PF00520_95id_0.9rows_0.9cols.fa	            #remove columns that are more than 10% gaps
python replace_chars.py PF00520_95id_0.9rows_0.9cols.fa XZB > PF00520_pfam_filtered_cleaned.fa  #replace any X, Z, or B characters in seqs with gaps
                                                                                                # Replacing unwanted characters with gaps is arguably not the best idea.
                                                                                                # Consider removing sequences with unwanted characters instead.
