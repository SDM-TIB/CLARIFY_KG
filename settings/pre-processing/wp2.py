'''
@auther: Samaneh
'''
import csv
import re

#################################################################################

with open("/mnt/e/CLARIFY-KG-pipeline/data/wp2/gold_triples_with_sources.tsv", 'r') as tsv_file: 
  with open("/mnt/e/CLARIFY-KG-pipeline/data/wp2/gold_triples_with_sources.csv", 'w') as csv_file:
    for line in tsv_file:
      new_format = re.sub("\t", ",", line)
      csv_file.write(new_format)