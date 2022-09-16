# election-analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election. The purpose of this audit is to serve as a small scale experiment. This audit process being done via Python is to make sure the process can be automated in the first place. If this process is successful, then it can implemented to senatorial and other local elections. 

## Steps to be completed
1) Calculate the total number of votes cast
2) Get a complete list of candidates who received votes
3) Calculate the total number of votes each candidate received
4) Calculate the percentage of total votes for each candidate
5) Determine the winner based on popular vote
6) Get a complete list of all counties in which a vote was submitted
7) Calculate total number of votes per county
8) Calculate percentage of votes per county
9) Determine county with highest voter turnout

## Resources
Data Source: election_results.csv
Software: Python 3.6.1

## Summary
The analysis of election can be shown below, and also in the attached text file
There were 369,711 total votes cast

There were 3 candidates who were running. They are:
  Charles Casper Stockham
  Diana DeGette
  Raymon Anthony Doane
  ----------------
The results are also follows:
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
  ----------------
The winner is:
  Winner: Diana DeGette
  Winning Vote Count: 272,892
  Winning Percentage: 73.8%
  ----------------
There were 3 counties with voter turnout. They are:
  Jefferson
  Denever
  Arapahoe
  ----------------
Information per county is as follows:
  Jefferson: 10.5% (38,855)
  Denver: 82.8% (306,055)
  Arapahoe: 6.7% (24,801)
  ----------------
The county with the largest voter turnout is Denver


## Further Uses
A more complete version of this script can be used for state elections, such as governor or senator races. In the case of either race, you will have to include every county. Therefore, the only difference between this data and this hypothetical data would be the size of the data. 
Another use of this data could be to filter out any election fraud. Although, statistically highly unlikely, there can be ballots counted twice, or submitted twice. To make sure that doesn't happen, you can use the script that checks for unique values. However, in this case, since duplicate values are already highly unlikely, we don't want to be checking for unique values; we want to be checking for duplicate values and populating the list with those values. So as long as the ballot ID is connected to the voter, rather than being a unique ID per ballot, we can then filter out any duplicate values - if there are any. 
