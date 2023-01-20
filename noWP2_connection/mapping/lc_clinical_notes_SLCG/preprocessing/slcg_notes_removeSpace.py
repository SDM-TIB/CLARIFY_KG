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

    a_df = pd.read_csv("/mnt/e/PROCESSING_DATA/original/clinical_trial.csv", low_memory=False)
    aList = list(str(a_df["trial_name"][i]).replace(" ", "_") for i in range (0, len(a_df)))
    aaList = list(aList[j].replace("nan", "") for j in range (0, len(aList)))
    a_df["trial_name"] = aaList
    a_df.to_csv("/mnt/e/PROCESSING_DATA/processed/clinical_trial_procssed.csv")

    b_df = pd.read_csv("/mnt/e/PROCESSING_DATA/original/targets_clinical_trial.csv", low_memory=False)
    bList = list(str(b_df["trial_name"][i]).replace(" ", "_") for i in range (0, len(b_df)))
    bbList = list(bList[j].replace("nan", "") for j in range (0, len(bList)))
    b_df["trial_name"] = bbList
    b_df.to_csv("/mnt/e/PROCESSING_DATA/processed/targets_clinical_trial_processed.csv")

    c_df = pd.read_csv("/mnt/e/PROCESSING_DATA/original/comorbidity.csv", low_memory=False)
    cList = list(str(c_df["name"][i]).replace(" ", "_") for i in range (0, len(c_df)))
    ccList = list(cList[j].replace("nan", "") for j in range (0, len(cList)))
    c_df["name"] = ccList
    c_df.to_csv("/mnt/e/PROCESSING_DATA/processed/comorbidity_processed.csv")       

if __name__ == "__main__":
        handler()