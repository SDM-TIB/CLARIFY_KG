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

    ##### First I convert "-1" float values in csv file to "40" manually ######
    schema_df = pd.read_csv("/mnt/e/CLARIFY-KG-pipeline/data/bc_clinical_notes_HUPHM/chemoterapy_cycle.csv", low_memory=False)
    meanDict = dict()
    mean_df = pd.read_csv("/mnt/e/Script/CLARIFY/drugs_bc_clinical_notes.csv", low_memory=False) ## This csv is exported from the table "chemotherapy_schema" by replacing the "+" with "_"    for i in range(0, len(mean_df)):
        if mean_df['id_schema'][i] not in meanDict.keys():
            meanDict.update({mean_df['id_schema'][i]:mean_df['drugs'][i]})

    drug1 = schema_df['id_schema'].values.astype(str)
    drug1 = list(map(lambda x : str(meanDict.get(eval(x))).split("_")[0] if "_" in str(meanDict.get(eval(x))) else str(meanDict.get(eval(x))), drug1))

    drug2 = schema_df['id_schema'].values.astype(str)
    drug2 = list(map(lambda x : str(meanDict.get(eval(x))).split("_")[1] if "_" in str(meanDict.get(eval(x))) and len(str(meanDict.get(eval(x))).split("_"))>1 else "", drug2))

    drug3 = schema_df['id_schema'].astype(str)
    drug3 = list(map(lambda x : str(meanDict.get(eval(x))).split("_")[2] if "_" in str(meanDict.get(eval(x))) and len(str(meanDict.get(eval(x))).split("_"))>2 else "", drug3))

    drug4 = schema_df['id_schema'].astype(str)
    drug4 = list(map(lambda x : str(meanDict.get(eval(x))).split("_")[3] if "_" in str(meanDict.get(eval(x))) and len(str(meanDict.get(eval(x))).split("_"))>3 else "", drug4))

    drug1Series = pd.Series(drug1, name="drug1")
    drug2Series = pd.Series(drug2, name="drug2")
    drug3Series = pd.Series(drug3, name="drug3")
    drug4Series = pd.Series(drug4, name="drug4")

    drugs_df = pd.concat([schema_df, drug1Series, drug2Series, drug3Series, drug4Series],axis=1)
    drugs_df.to_csv("/mnt/e/CLARIFY-KG-pipeline/data/bc_clinical_notes_HUPHM/chemoterapy_cycle_preprocessed.csv")


if __name__ == "__main__":
        handler()