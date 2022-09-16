import os

#file_to_save = os.path.join("analysis","election_analysis.txt")
file_to_save = 'resources/election_analysis.txt'
outFile = open(file_to_save,'w')
outFile.write("Counties in the Election\n-----------\n")
outFile.write("Arapahoe\nDenver\nJefferson")

outFile.close()