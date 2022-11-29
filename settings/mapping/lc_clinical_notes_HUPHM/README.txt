########################################################################
 ######## Additional csv generated from the HUPHM LC RDB ##############
########################################################################

SELECT `tnm_stadification`.*, `diagnosis`.`date`,`diagnosis`.`stage`
FROM `diagnosis`,`tnm_stadification`
WHERE `tnm_stadification`.`EHR` = `diagnosis`.`EHR`
-> tnm_stadification_join_diagnosis_date


SELECT `tumor_histology`.*, `diagnosis`.`date`
FROM `diagnosis`,`tumor_histology`
WHERE `tumor_histology`.`EHR` = `diagnosis`.`EHR`
-> tumor_histology_join_diagnosis_date


########################################################################
 ##### Not considered attribute from the HUPHM LC RDB #################
########################################################################

In family_antecedents_treatment_line, we consider the multi-valued composite attribute
of family history consisting of (patientId + familyRelation + cancertype).
We are NOT considering the treatment line in family history. 
