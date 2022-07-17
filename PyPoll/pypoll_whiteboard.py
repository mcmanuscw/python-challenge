# Dependencies
from calendar import c
from locale import currency
from optparse import Values
import os
import csv
from typing import Counter

from numpy import average, double, int0

# --------------------------------------------------
#Variables
candidate_options = []
#Declare count for votes as a number
vote_counter={}
winning_percentage = 0
county_votes ={}
total_votes =0 
county_percent=0 

# --------------------------------------------------
# Reading using CSV module
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #TotalVotes = (len(csvreader))  

    # # Read each row of data after the header and read them into a list
    for row in csvreader:
        total_votes = total_votes +1
        candidate_name =row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            vote_counter[candidate_name] =0
        vote_counter[candidate_name] += 1
    
    
    #TotalVotes = (len(csvreader))  
    
    print(vote_counter)

    for county in county_votes:
        county_vote = county_vote[county]
        county_percent = float(county_vote)/ float(total_votes) *100
    
    #print("print(county_percent)")
    print(county_percent)
    
    #print(vote_counter[2]) 
    
   # print("print(candidate_options)")
    #print(candidate_options)    

#1 How do I get a distinct list of candidates?

















# # print("Print Candidates")
# print(candidates)

# CandidatesUnique = []
    
# # # for element in Candidates:
# for element in candidates:
#      if element not in candidates:
#         CandidatesUnique.append

# print("Unique Candidates:")
# print("Unique Candidates",Candidates)



            
# # print(Counter)

# TotalVotes = (len(votes))

# # CWM Notes
#     # List to get unique values candidates
#         # Find unique candidates
#         #get count of votes, grouped by candidates; divide by total # votes to get Pct
#     # Create list of candidates and percentage won
#     # Determine the winner by max(percent_won)

#     #Print out result set





# # Assignment Requirements:

#         # The total number of votes cast
#         # A complete list of candidates who received votes
#         # The percentage of votes each candidate won
#         # The total number of votes each candidate won
#         # The winner of the election based on popular vote
#         # Your analysis should align with the following results:

#         # Election Results
#         # -------------------------
#         # Total Votes: 369711
#         # -------------------------
#         # Charles Casper Stockham: 23.049% (85213)
#         # Diana DeGette: 73.812% (272892)
#         # Raymon Anthony Doane: 3.139% (11606)
#         # -------------------------
#         # Winner: Diana DeGette
#         # -------------------------
#         # In addition, your final script should both print the analysis to the terminal and export a text file with the results.


