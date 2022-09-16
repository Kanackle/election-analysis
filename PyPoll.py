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

#initialize votes variable
total_votes = 0
#initialize candidates list
candidate_options = []
#initialize dictionary
candidate_votes = {}
#winning variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    # print(headers)
    for row in file_reader:
        total_votes +=1
        candidate_name=row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes/ total_votes * 100)
        #print(f'{candidate_name} received {vote_percentage:.1f}% of total votes')

        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
    winning_candidate_summary = (
        f"----------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------\n"
    )
    print(winning_candidate_summary)
# print(total_votes)
# print(candidate_votes)

    
    