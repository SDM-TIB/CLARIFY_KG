'''
@auther: Samaneh
'''
import csv
import re

#################################################################################

with open("/mnt/e/CLARIFY/wp2/batch2_processed/silver_triples.tsv", 'r') as tsv_file: 
  with open("/mnt/e/CLARIFY/wp2/batch2_processed/silver_triples.csv", 'w') as csv_file:
    for line in tsv_file:
      new_format = re.sub("\t", ",", line)
      csv_file.write(new_format)