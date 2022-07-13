# Dependencies
from calendar import c
from locale import currency
from optparse import Values
import os
import csv
from typing import Counter

from numpy import average, double, int0

# --------------------Initialize Lists-------------

# # Initialize Lists
votes = []
candidates = []

# --------------------------------------------------

csvpath = os.path.join('Resources', 'election_data.csv')

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header and read them into a list
    for row in csvreader:
        votes.append(row[2])

    for row in csvreader:
        candidates.append(row[1])

print(candidates)

# Candidates = [votes[2]]
# CandidatesUnique = []
    
# for element in Candidates:
#     if element not in Candidates:
#         CandidatesUnique.append

# print("Unique Candidates",Candidates)



            
# print(Counter)

TotalVotes = (len(votes))

# CWM Notes
    # List to get unique values candidates
        # Find unique candidates
        #get count of votes, grouped by candidates; divide by total # votes to get Pct
    # Create list of candidates and percentage won
    # Determine the winner by max(percent_won)

    #Print out result set





# Assignment Requirements:

        # The total number of votes cast
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won
        # The total number of votes each candidate won
        # The winner of the election based on popular vote
        # Your analysis should align with the following results:

        # Election Results
        # -------------------------
        # Total Votes: 369711
        # -------------------------
        # Charles Casper Stockham: 23.049% (85213)
        # Diana DeGette: 73.812% (272892)
        # Raymon Anthony Doane: 3.139% (11606)
        # -------------------------
        # Winner: Diana DeGette
        # -------------------------
        # In addition, your final script should both print the analysis to the terminal and export a text file with the results.


