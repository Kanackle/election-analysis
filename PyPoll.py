#Data we need to retrieve
#1) Total number of votes counted
#2) List of all candidates who received a vote
#3) Percentage of votes each candidate received
#4) Total number of votes per candidate
#5) Winner of the popular vote


#METHOD 1 TO OPEN/READ FILE
# election_data = open(file_to_load, 'r')
# print(election_data)
# election_data.close()

#METHOD 2 TO OPEN/READ FILE
# with open(file_to_load) as election_data:
# print(election_data)

import os
import csv
#variable for load file(indirect path)  
file_to_load = os.path.join('resources', 'election_results.csv')
#variable for write file(direct path)
file_to_save = 'analysis/election_analysis.txt'

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)