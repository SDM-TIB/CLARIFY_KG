########################################################################
########### Additional csv generated from the SLCG RDB #################
########################################################################

SELECT `tnm_stadification`.*, `diagnosis`.`date`,`diagnosis`.`stage`
FROM `diagnosis`,`tnm_stadification`
