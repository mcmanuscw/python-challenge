# Dependencies
import os
import csv


# --------------------------------------------------
# source data file
read_csvpath = os.path.join('Resources', 'election_data.csv')
# outputpath
write_csvpath = os.path.join('Analysis', 'election_data_analysis.csv')


# --------------------------------------------------
#Candidate Options
candidate_options = []
#Candidate vote counter
candidate_votes = {}

# Winning candidate tracker
winner = ""
winner_votes = 0

#Variables
total_votes =0 



# --------------------------------------------------
# source data file
read_csvpath = os.path.join('Resources', 'election_data.csv')
# outputpath
write_csvpath = os.path.join('Analysis', 'election_data_analysis.csv')



with open(read_csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    election_data = csv.reader(csvfile)

    # Read the header  (skip this step if there is now header)
    csv_header = next(election_data)
    
    #For reach row
    for row in election_data:

        # print("* ", end="")
        #Add tot he total vote count









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


