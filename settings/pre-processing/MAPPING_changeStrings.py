'''
@auther: Samaneh
'''
import glob

#################################################################################

for inFile in glob.glob("/mnt/e/CLARIFY-KG-Pipeline/output/Dragoman/bc_clinical_notes_HUPHM/*.ttl"):
	print (inFile)
	# Read in the file
	with open(inFile, 'r') as file :
	  filedata = file.read()
	# Replace the target string
	filedata = filedata.replace("/mnt/e/CLARIFY-KG-pipeline/output/Dragoman/bc_clinical_notes_HUPHM/","/data/bc_clinical_notes_HUPHM/")
	#filedata = filedata.replace("http://clarify2020.eu/entity/","http://research.tib.eu/clarify2020/entity/")

	# Write the file out again
	with open(inFile, 'w') as file:
	  file.write(filedata)
