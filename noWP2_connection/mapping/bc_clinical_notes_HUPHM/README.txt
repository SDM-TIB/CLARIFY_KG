####################################################################################
######################### Data Pre-processing is performed: ########################
####################################################################################

First we create "chemotherapy_cycle_preprocessed" by preprocessing both tables "chemotherapy_cycle" and "chemotherapy_schema" using "bc_notes_drugs.py" script.

####################################################################################
The table "drug", and "drug_chemotherapy_schema" are already considered through the function "findSemantic_HUPHM_BreastCancer.py" via "HUPHM_BreastCancer_dictionary.csv" applied in mapping "chemotherapy_cycle_bc_clinical_notes_HUPHM.ttl", so only ONE mapping is needed for the four tables "chemotherapy_cycle", "chemotherapy_schema", "drug", and "drug_chemotherapy_schema".

########################################################################
  ########### Data cleaning performed directly on RDB ################
########################################################################


########## this one is NOT needed anymore since UPM cleaned the data #############
UPDATE `patient` SET `neoadjuvant`="yes" 
WHERE `patient`.`ehr` in (
SELECT `tumor_tnm`.`ehr` FROM `tumor_tnm`,`patient_temp` WHERE `tumor_tnm`.`ehr` = `patient_temp`.`ehr` AND `tumor_tnm`.`stage_after_neo` != "NULL" AND `patient_temp`.`neoadjuvant` LIKE "%no%"
)


########################################################################
 ########## Additional Table added to the HUPHM BC RDB ##############
########################################################################
CREATE TABLE tumor_tnm_join_diagnosis_and_neoadjuvant_date
AS
SELECT `tumor_tnm`.*, `patient`.`diagnosis_date`,`patient`.`first_treatment_date` as `neoadjuvant_derived_date`, `patient`.`neoadjuvant`
FROM `patient`,`tumor_tnm`
WHERE `tumor_tnm`.`ehr` = `patient`.`ehr`


UPDATE `tumor_tnm_join_diagnosis_and_neoadjuvant_date` SET `neoadjuvant_derived_date`= NULL 
WHERE `neoadjuvant` LIKE "%no%"
