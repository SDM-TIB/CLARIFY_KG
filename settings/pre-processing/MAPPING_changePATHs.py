'''
@auther: Samaneh
'''
import glob

#################################################################################

for inFile in glob.glob("/mnt/e/GitHub/CLARIFY_KG/settings/mapping/publication/*.ttl"):
	print (inFile)
	# Read in the file
	with open(inFile, 'r') as file :
	  filedata = file.read()
	# Replace the target string
	filedata = filedata.replace("/mnt/e/data/data/publication/","/mnt/e/CLARIFY-KG-pipeline/data/publication/")
	# Write the file out again
	with open(inFile, 'w') as file:
	  file.write(filedata)
