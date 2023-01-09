'''
@auther: Samaneh
'''
import pandas as pd
import numpy as np
import math
import csv
import re

#################################################################################

def handler():

    a_df = pd.read_csv("/mnt/e/CLARIFY-KG-pipeline/data/publication/Semrep_Annotations_notCleaned.csv", low_memory=False)
    index_List = list(i for i in range (0, len(a_df)) if "C" not in str(a_df["subject_cui"][i]) or "|" in str(a_df["subject_cui"][i]) or "C" not in str(a_df["object_cui"][i]) or "|" in str(a_df["object_cui"][i]))
    a_df = a_df.drop(index_List)

    a_df.to_csv("/mnt/e/CLARIFY-KG-pipeline/data/publication/Semrep_Annotations.csv")       

if __name__ == "__main__":
        handler()