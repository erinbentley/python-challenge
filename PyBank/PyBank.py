#Erin Bentley
#Data Viz Boot Camp
#Python Homework
import os
import csv

csvpath = os.path.join("../","budget_data.csv")
#if it was in PyBank folder: os.path.join("../PyBank","budget_data.csv")
#The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
total_profit = 0
# The average of the changes in "Profit/Losses" over the entire period
previous_revenue = 0
#revenue_diff = 0
# We have to define revenue_change_list as a list so that the output can be added up and an average can be found
# [] in Python means that all these values are going to be a list. 
revenue_change_list = []
change_dates = []

#open budget csv file
with open(csvpath,"r") as Financial_Details:
    csvreader = csv.reader(Financial_Details)
    next(csvreader)
    for row in csvreader:
        
        #print(row)
        total_months = total_months + 1
        #tells the code to count the rows and keep a tally
        #print(total_months)

        total_profit = total_profit + int(row[1])
        #tells the code to calculate 0 + the row (converted into an integer)
        #print(total_profit)

        revenue_diff = float(row[1]) - previous_revenue
        #print(row[0])
        dates = row [0]
        previous_revenue = float(row[1])
        revenue_change_list.append(revenue_diff)
        change_dates.append(dates)

    #print(len(revenue_change_list))
    #print(len(change_dates))
 
    average_revenue = round(sum(revenue_change_list[1:])/len(revenue_change_list[1:]), 2)
    #print(average_revenue)
        #update the variable "previous_revenue"; previous_revenue = float(row[1]) to show that now previous revenue = previous month
        

max_change = max(revenue_change_list)
max_change_index = revenue_change_list.index(max_change)
max_date = change_dates [max_change_index]

#max is the 25th postition from the revenue change list 

#print(max_change_index)
#print(max_date)
#print(revenue_diff)
#print (max_change)

min_change = min(revenue_change_list)
min_change_index = revenue_change_list.index(min_change)
min_date = change_dates [min_change_index]
        
#print (min_change_index)
#print (min_date)
#min is the 44th position (or index) 
#print (min_change)

output_file = os.path.join("Financial Details")
print("Financial_Details")
print("________")
print("Total Months: " + str(total_months))
print("Average Revenue: " + str(average_revenue))
print("Greatest Increase in Profits: " + str(max_date) +": " + str(max_change))
print ("Greatest Decrease in Profits: " + str(min_date) +": "+ str(min_change))
print("________")
    