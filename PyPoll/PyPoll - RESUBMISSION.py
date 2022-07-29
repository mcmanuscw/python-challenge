
# Reworked with the help of tutoring and the solution

# Incorporated the csv module
import csv
import os

# Files to load
# To test on small dataset
# file_to_load = os.path.join('Resources','election_data_sm.csv')
file_to_load = os.path.join('Resources','election_data.csv')

# Files output
file_to_output = os.path.join('Analysis','election_analysis.txt')

# Initialize the count to capture the total number of votes cast
total_votes = 0

# Initialize list to capture distinct list of candidates
candidate_options = []

# Initialize dictionary to capture candidates and thier vote counts
# CONCEPT NOTES >> dictionary can not have duplicates; is being used to store values in pairs>>  Candidate : VoteCount?
candidate_votes = {} 

# Initialize placeholder variables to capture who the winning candidate is
# and winning vote count
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row do the following
    for row in reader:

        # # Print runtime animation - a marker that action is being taken on each row
        # print(" - ", end="")

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2] # Refers to the second column; the second data element of the data that is being read 

        # List Comprehension
        # If the candidate does not match any existing candidate...add it to the list of candidate options
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            
            
            # And begin tracking that candidate's voter count
            # IS THE THE ESTABLISHMENT OF THE PAIRED DICTIONARY VALUES
            candidate_votes[candidate_name] = 0

            #print(candidate_votes) #CWM

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate) # vote number 
        vote_percentage = float(votes) / float(total_votes) * 100   

        #print(candidate) #cwm
        print(votes) #cwm

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
