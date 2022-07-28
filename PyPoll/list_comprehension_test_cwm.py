from nbformat import current_nbformat
import os

file_to_output = os.path.join('fruit_purchase_analysis.txt')

total_num_fruits = 0

#Placeholders for winning candidate and winning count tracker
winning_fruit = ""
winning_count = 0


# Fruit LIst
fruits = ["apple","apple","apple","apple","apple", "peach","peach","peach","peach","peach","peach", "cherry","cherry","cherry", "pumpkin", "pumpkin", "pumpkin"]

# Unique list of the fruits that appear in the list
fruit_options = []
fruit_votes = {}
fruit_counter = 0
fruit_name = ""

#Goal is to append a new list item if it is not in the list and to add the count to the list


for row in fruits:
    
    # Run the load animation
    print("*  ", end="")
    
    #Total number of fruits
    total_num_fruits = total_num_fruits + 1

    # Extract the fruit name from each row
    fruit_name = row

    # If the fruit name is not does not match any existing fruit, add it to the list    
    if fruit_name not in fruit_options:
            
        # Add it to the list of fruit options
        fruit_options.append(fruit_name)

        # And begin tracking that fruit's count
        fruit_votes[fruit_name] = 0
    
    # Then add a vote to that fruit's count
    fruit_votes[fruit_name] = fruit_votes[fruit_name] + 1 # HELP >> IS LIKE A VLOOKUP TO THE VOTE COUNT VALUE THAT SHOULD BE INCREMENTED WITH A VOTE?
    

# Print the results to terminal and export the data to text file
with open(file_to_output, "w") as txt_file:

    # Print the final vote count to the terminal
    preference_results = (
        f"\n\nFruit Preference Results\n"
        f"**********************************\n"
        f"Total Fruits: {total_num_fruits}\n"
        f"**********************************\n")
        
    #Print 
    print(preference_results, end="")
    
    # Save the final vote count to the text file
    txt_file.write(preference_results)
    
    #Determine winner by looping through the fruit counts
    for fruit_name in fruit_votes:
        #print(fruit_name) #cwm

        # Retrieve vote count and percentage
        votes = fruit_votes.get(fruit_name)
        vote_percentage = float(votes) / float(total_num_fruits) * 100

        # print(votes) #cwm
        # print(vote_percentage) #cwm

        if(votes > winning_count):
            winning_count = votes
            winning_fruit = fruit_name

           # Print each candidate's voter count and percentage (to terminal)
            sales_output = f"{fruit_name}: {vote_percentage:.3f}% ({votes})\n"
            print(sales_output, end="")

            # Save each fruit's preference count and percentage to the text file
            txt_file.write(sales_output)

    # Print the winning candidate (to terminal)
    winning_fruit_summary =(
        f"**********************************\n"
        f"Most Popular: {winning_fruit}\n"
        f"**********************************\n")
    print(winning_fruit_summary)

    #Save the winning fruit to the text file_to_output
    txt_file.write(winning_fruit_summary)
    
