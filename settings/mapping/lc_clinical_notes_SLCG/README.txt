########################################################################
###### SLCG tables that couldn't be integrated into the current KG #####
########################################################################

1. metastasis_location_treatmentline
2. other_metastasis_locations_progression_relapse
3. other_mutations_treatment_line
4. other_mutations -> (type and result are all NULL)

########################################################################
########### Additional csv generated from the SLCG RDB #################
########################################################################

SELECT `tnm_stadification`.*, `diagnosis`.`date`
FROM `diagnosis`,`tnm_stadification`
WHERE `tnm_stadification`.`EHR` = `diagnosis`.`EHR`
-> tnm_stadification_join_diagnosis_date

SELECT `tumor_histology`.*, `diagnosis`.`date`
FROM `diagnosis`,`tumor_histology`
WHERE `tumor_histology`.`EHR` = `diagnosis`.`EHR`
-> tumor_histology_join_diagnosis_date

#######################################################
############ Pre-processing: on csv data ##############
#######################################################

1. For the two records in SLCG with family_member="Padre o hermano" and "Madre y tia", an extra record is added:

> egrep "Padre o hermano" family_antecedents_treatment_line.csv > new_record_1.csv
> egrep "Madre y tia" family_antecedents_treatment_line.csv > new_record_2.csv
> sed 's/Padre o hermano/Hermano/g' new_record_1.csv > to_be_added_record_1.csv
> sed 's/Madre y tia/Tia/g' new_record_2.csv > to_be_added_record_2.csv
> sed 's/Padre o hermano/Padre/g' family_antecedents_treatment_line.csv > family_antecedents_treatment_line_modified_1.csv
> sed 's/Madre y tia/Madre/g' family_antecedents_treatment_line_modified_1.csv > family_antecedents_treatment_line_modified_2.csv
> rm family_antecedents_treatment_line.csv
> cat family_antecedents_treatment_line_modified_2.csv to_be_added_record_1.csv to_be_added_record_2.csv > family_antecedents_treatment_line.csv
> rm family_antecedents_treatment_line_modified_1.csv
> rm family_antecedents_treatment_line_modified_2.csv
> rm new_record_1.csv
> rm new_record_2.csv

So the four records' values for family_member are "Padre", "Hermano", "Madre", and "Tia" respectively
