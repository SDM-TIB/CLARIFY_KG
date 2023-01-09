
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


#######################################################
########## Database of Patient Identifiers ############
#######################################################
The identifiers related to tables that are created based 
on the provided data are required to be updated each time 
that the data sources are updated by UPM.


#######################################################
############# Pre-processing: WP2 data ################
#######################################################

1) The first batch that they sent as json file was not 
correct in terms of the json format and SDM-RDFizer 
could not be run over. So the format is fixed.

2) The second batch that they sent on December 2022 was
in TSV so needed to be converted to csv using the script
"wp2.py" in "pre-processing" directory on GitHub. Also
the columns names were missing which is added based on 
https://github.com/pminervini/clarify-wp2-relationships/blob/main/13122022/gold/README.md
as mentioned by wp2.