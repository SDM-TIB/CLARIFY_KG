'''
@auther: Samaneh
'''
import glob

#################################################################################

for inFile in glob.glob("/mnt/e/GitHub/CLARIFY-Pipeline/KGC-DIS/CSV2RDF-RMLMappingRules/wp2/*.ttl"):
	# Read in the file
	with open(inFile, 'r') as file :
	  filedata = file.read()
	# Replace the target string
	filedata = filedata.replace("/mnt/e/CLARIFY-KG-pipeline/data/wp2/","/data/wp2/")
	filedata = filedata.replace("http://clarify2020.eu/entity/","http://research.tib.eu/clarify2020/entity/")
	filedata = filedata.replace("http://clarify2020.eu/vocab/","http://research.tib.eu/clarify2020/vocab/")

	# Write the file out again
	with open(inFile, 'w') as file:
	  file.write(filedata)
