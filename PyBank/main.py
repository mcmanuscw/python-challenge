# Dependencies
from optparse import Values
import os
import csv

from numpy import average, double, int0

# --------------------Initialize Lists-------------

# Initialize List for Investments
Investments = []

# Initialize Investment Change (Difference List
diff_list = []

# --------------------------------------------------

csvpath = os.path.join('Resources', 'budget_data.csv')

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header and read them into a list
    for index, row in enumerate(csvreader):
        # print(index, row[1]) #Prints element 1 aka first column
        Investments.append(int(row[1]))
        
    

    # print inital list
    #print(Investments)
 
    for x, y in zip(Investments[0::], Investments[1::]):
       diff_list.append(y-x) 

    # print difference list
    #print(diff_list)

 
    RoundedAverage = round(average(diff_list),2)

    

# Print Results to Terminal

print("")
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("")
print(f"Total # Months: {len(Investments)}")
print(f"Net Total PnL:  ${sum(Investments)}")
print(f"Average Change: ${RoundedAverage}")
print(f"Greatest Decrease: (${min(diff_list)})")
print(f"Greatest Increase in Profits: $({max(diff_list)})")

# I ran out of time and couldn't successfully figure out how to write the results to an output file I am 


