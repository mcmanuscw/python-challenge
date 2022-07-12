# Dependencies
from optparse import Values
import os
import csv

from numpy import average, double, int0

csvpath = os.path.join('Resources', 'budget_data.csv')



# --------------------Initialize Lists-------------

# Initialize List for Investments
Investments = []

# Initialize Investment Change (Difference List
diff_list = []

# --------------------------------------------------


# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    for index, row in enumerate(csvreader):
        # print(index, row[1]) #Prints element 1 aka first column
        Investments.append(int(row[1]))
        Investments.append(row[0],int(row[1]))

    # print inital list
    print(Investments)
 
    for x, y in zip(Investments[0::], Investments[1::]):
       diff_list.append(y-x) 

    # print difference list
    #print(diff_list)

 
RoundedAverage = round(average(diff_list),2)

print("")
print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("")
print(f"Total # Months: {len(Investments)}")
print(f"Net Total PnL:  ${sum(Investments)}")
print(f"Average Change: ${RoundedAverage}")
print(f"Average Change: (${min(diff_list)})")
print(f"Greatest Increaes in Profits: $({max(diff_list)})")

 # Write to File
    L_Desc = ["Total number of months:", "Net Total PnL:", "Average Change:", "Greatst Increaes in Profits:", "Greatest Decrease in Profits:"]
    L_Values = [len(Investments), sum(Investments), average(diff_list), max(diff_list), min(diff_list)]


# Stagging

# git add .
# git commit -m "add_message"
# git push

# Optional
# git status