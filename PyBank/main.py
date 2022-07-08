# 05- ins read file as an example for reading a file

# Store the file path associated with the file (note the backslash may be os specific)
file = 'Resources/budget_data.csv'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file,'r') as text:
    
    # This stores a reference to a file name
    print(text)

    # Store all of the text inside a variable called "lines"
    lines = text.read()

    #print the contents of the  text file
    print(lines)




    # Assignment Instructions
# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset
# cwmcomments >>>>> month number of the latest (max) date and subtract the month number of the earliest (min) date

DateList = [lines]

print(DateList(1))

        # The net total amount of "Profit/Losses" over the entire period

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes

        # The greatest increase in profits (date and amount) over the entire period

        # The greatest decrease in profits (date and amount) over the entire period