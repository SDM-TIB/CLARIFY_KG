#############################################################################################
########################################################################
Tables "chemotherapy_cycle", "chemotherapy_schema", "drug", and "drug_chemotherapy_schema" are included in "chemotherapy_cycle_bc_clinical_notes_HUPHM.ttl", function "findSemantic_HUPHM_BreastCancer.py", "HUPHM_BreastCancer_dictionary.csv".


########################################################################
  ########### Data cleaning performed directly on RDB ################
########################################################################

UPDATE `patient` SET `neoadjuvant`="yes" 
WHERE `patient`.`ehr` in (
SELECT `tumor_tnm`.`ehr` FROM `tumor_tnm`,`patient_temp` WHERE `tumor_tnm`.`ehr` = `patient_temp`.`ehr` AND `tumor_tnm`.`stage_after_neo` != "NULL" AND `patient_temp`.`neoadjuvant` LIKE "%no%"
)

########################################################################
########### Additional csv generated from the BC RDB #################
########################################################################
SELECT `surgery`.*, `patient`.`surgery_date`
FROM `surgery`,`patient`
WHERE `surgery`.`ehr` = `patient`.`ehr`
--> patient_join_surgery_date
