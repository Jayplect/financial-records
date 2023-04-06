#load the libraries need for this challenge
import os
import csv

#create a file path to access data
csvpath = os.path.join("Resources", "budget_data.csv")

#initialize variables to store values
total_months = 0
profit_losses = []
date = []
total_revenue = 0
max = 0
min = 0
revenue_change = []

#open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip csv header
    csvheader = next(csvfile)

    #iterate through each row in data
    for row in csvreader:

        #count the total number of months by... 
        # adding 1 to the variable "total_months" for each iteration
        total_months += 1

        #total amount of "Profit/Losses" over the entire period
        total_revenue = total_revenue + int(row[1])  
   
        #grab the list of dates
        date.append(row[0])

        #grab the lists of profit/losses
        profit_losses.append(row[1])
    
    # Iterate through the list of profit/losses to calculate...
    # the average changes in profit over the entire period
    #The range for the iteration begins from 1 so that the difference between the 1st and 0th element can be performed
    for i in range (1, len(profit_losses)):
        revenue_change.append(int(profit_losses[i])-int(profit_losses[i-1]))

        #Average revenue change
        ## subtract 1 from the length of the revenue
        ### round to 2 significant figure
        average_change = round(sum(revenue_change)/(len(profit_losses)-1), 2)
        
        #greatest increase in profits
        #subtract 1 from the index 
        if revenue_change[i-1] > max:
            max = revenue_change[i-1]
        #add 1 to the date index 
            date_max = date [i]

        #greatest decrease in profits
        #subtract 1 from the index 
        if revenue_change[i-1] < min:
            min = revenue_change[i-1]
        #add 1 to the date index
            date_min = date [i]

print("Financial Analysis")
print("---------------------------------------------------")
# The total number of months included in the dataset
print(f'Total Months: {total_months}')
# The net total amount of "Profit/Losses" over the entire period
print(f'Total: ${total_revenue}')
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print(f'Average Change: ${average_change}')
# The greatest increase in profits (date and amount) over the entire period
print(f'Greatest increase in Profits: {date_max} (${max})')
# # # The greatest decrease in profits (date and amount) over the entire period
print(f'Greatest Decrease in Profits: {date_min} (${min})')

#text file with results from analysis
with open(os.path.join("analysis","textfile.txt"), "w") as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("-------------------------------------" + "\n")
    txtfile.write("Total Months:" + " " + str(total_months) + "\n")
    txtfile.write("Total:" + " " + "$" + str(total_revenue) + "\n")
    txtfile.write("Average Change:" + " " +  "$" + str(average_change) + "\n")
    txtfile.write("Greatest increase in Profits:" + " " + str(date_max)+ " " + "("+ "$" +  str(max) + ")" + "\n")
    txtfile.write("Greatest decrease in Profits:" + " " + str(date_min)+ " " + "("+ "$" +  str(min) + ")" + "\n")
    txtfile.close()