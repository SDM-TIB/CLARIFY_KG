'''
@auther: Samaneh
'''
import glob

#################################################################################

for inFile in glob.glob("/mnt/e/mapping/annotation/*.ttl"):
	print (inFile)
	# Read in the file
	with open(inFile, 'r') as file :
	  filedata = file.read()
	# Replace the target string
	filedata = filedata.replace("http://clarify2020.eu/vocab/","http://research.tib.eu/clarify2020/vocab/")
	filedata = filedata.replace("http://clarify2020.eu/entity/","http://research.tib.eu/clarify2020/entity/")

	# Write the file out again
	with open(inFile, 'w') as file:
	  file.write(filedata)
