
# Dependencies
from decimal import Rounded
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
 
    for x, y in zip(Investments[0::],   Investments[1::]):
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
print(f"Greatest Decrease: yy-mmm (${min(diff_list)})")
print(f"Greatest Increase in Profits: yy-mmm $({max(diff_list)})")


# Write Summary to CSV File
# Specify the file to write to
output_path = os.path.join("analysis", "PyBankSummary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis', ''])

    # Write the second row 
    csvwriter.writerow(['-----------------------------------', ''])

   # Write the rows (column headers)
    csvwriter.writerow(['Total Number of Months:', len(Investments)])
    csvwriter.writerow(['Net Total PnL:', sum(Investments)])
    csvwriter.writerow(['Average Change:', RoundedAverage])
    csvwriter.writerow(['Greatest Decrease on Profits:', f"yy-mmm {min(diff_list)}"])
    csvwriter.writerow(['Greatest Increase in Profits:', f"yy-mmm {max(diff_list)}"])
    
