########################################################################
 ######## Additional csv generated from the HUPHM LC RDB ##############
########################################################################

SELECT `tnm_stadification`.*, `diagnosis`.`date`,`diagnosis`.`stage`
FROM `diagnosis`,`tnm_stadification`

SELECT `tumor_histology`.*, `diagnosis`.`date`
FROM `diagnosis`,`tumor_histology`
-> tumor_histology_join_diagnosis_date