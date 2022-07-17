
# Dependencies
from decimal import Rounded
from optparse import Values
import os
import csv
from numpy import average, double, int0

# Path for reading csv files
csvpath = os.path.join("Resources", "budget_data.csv")

# Variables
# Sticky Notes used for saving bits of information as the routine reads the csv file


TotalNumberMonths = 0       # * The total number of months included in the dataset; running total of the number of monthly periods
NetTotalProfits = 0         # * The net total amount of "Profit/Losses" over the entire period
ChangeInPnL = 0             # * The changes in "Profit/Losses" over the entire period, and then the average of those changes
AverageChangeInPnL = 0      #   Place saver for running total of changes to calc Average
GreatestIncrease = 0        # * The greatest increase in profits (date and amount) over the entire period
GreatestIncreaseDate = ""   #
GreatestDecrease=0          # * The greatest decrease in profits (date and amount) over the entire period
GreatestDecreaseDate = ""   #


#open the file in “read” mode (‘r’) and store the contents in the variable “text”
with open(csvpath) as csvfile:
    #This stores a reference to a file stream
    csvreader = csv.reader(csvfile, delimiter=",")
    #Read the header row first
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        
        CurrentMonth = float(row[1])
        
        # Increment to the next month
        TotalNumberMonths += 1
        
        #Set the values for the first period; since there is no previous period, set previous month value to 0
        
        if TotalNumberMonths == 1:
            
            PreviousMonth = 0
            ChangeInPnL = 0     # In the first period there is PreviousPeriod; no change in pnl
            GreatestIncrease = 0
            GreatestDecrease = 0
            GreatestIncreaseDate = row[0]
            GreatestDecreaseDate = row[0]
            
            

        else:
            


            if ChangeInPnL > GreatestIncrease:
                    GreatestIncrease = ChangeInPnL
                    GreatestIncreaseDate = row[0]
            elif ChangeInPnL < GreatestDecrease:
                    GreatestDecrease = ChangeInPnL
                    GreatestDecreaseDate = row[0]
        
            # #Capture the greatest increase/decrease dates
            # GreatestIncreaseDate = row[0]
            # GreatestDecreaseDate = row[0]

            # Calculate the change in net profit from one month to the next
            ChangeInPnL = CurrentMonth - PreviousMonth

        # Increment NetTotalProfits
        NetTotalProfits += CurrentMonth
            
        # Increment running total of changes in pnl
        AverageChangeInPnL += ChangeInPnL 

        #The current month becomes the previous month at the end of the loop
        PreviousMonth = CurrentMonth


    #Calculate AvgerageChangeInPnL
    AverageChangeInPnL = AverageChangeInPnL/(TotalNumberMonths-1)


print(f"Financial Analyisis:")
print("-----------------------------------")
print(f"Total Months: {TotalNumberMonths}")
print(f"Net Total Profits: ${NetTotalProfits}")
print(f"Change in PnL: {ChangeInPnL}")
print(f"Average Change: ${AverageChangeInPnL}")
print(f"Greatest Increase in Profits: {GreatestIncreaseDate}: ${GreatestIncrease}")
print(f"Greatest Decrease in Profits: {GreatestDecreaseDate}: ${GreatestDecrease}")


# Write Summary to CSV File
# Specify the file to write to
output_path = os.path.join("analysis", "PyBankSummary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis","" ,"" ])

    # Write the second row 
    csvwriter.writerow(["-----------------------------------", "", ""])

   # Write the rows (column headers)
    csvwriter.writerow(["Total Number of Months:", "" , TotalNumberMonths])
    csvwriter.writerow(["Net Total PnL:", "" ,NetTotalProfits])
    csvwriter.writerow(["Average Change:", "", AverageChangeInPnL])
    csvwriter.writerow(["Greatest Decrease on Profits:", GreatestIncreaseDate, GreatestIncrease])
    csvwriter.writerow(["Greatest Increase in Profits:", GreatestDecreaseDate, GreatestDecrease])
    

print("-----------------------------------")
print(f"Written to {output_path}")



#Expected Result Set
#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)
#   ```

