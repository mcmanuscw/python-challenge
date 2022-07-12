# Dependencies
import os
import csv

from numpy import average, double

csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading using CSV module

# --------------------Initialize Lists-------------

# Initialize List for Investments
Investments = []

# Initialize Investment Change (Difference List
diff_list = []

# --------------------------------------------------

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    for index, row in enumerate(csvreader):
        # print(index, row[1]) #Prints element 1 aka first column
        Investments.append(float(row[1]))

    # print inital list
    # print(Investments)
 
    for x, y in zip(Investments[0::], Investments[1::]):
       diff_list.append(y-x) 

    # print difference list
    #  print(diff_list)

print(average(diff_list))
print(min(diff_list))
print(max(diff_list))
print(len(Investments))



#     # Assignment Instructions ref 03-python 12-Stu-CencusZip
# # Your task is to create a Python script that analyzes the records to calculate each of the following values:

# # Lists t store data
# NumberOfMonths = []
# NetProfitLoss = []
# GreatestIncrease = []
# GreatestDecrease = []
# functin

# The total number of months included in the dataset
# cwmcomments >>>>> month number of the latest (max) date and subtract the month number of the earliest (min) date




        
        # The net total amount of "Profit/Losses" over the entire period

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes

        # The greatest increase in profits (date and amount) over the entire period

        # The greatest decrease in profits (date and amount) over the entire period
# Stagging

# git add .
# git commit -m "add_message"
# git push

# Optional
# git status