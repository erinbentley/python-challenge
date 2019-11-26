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
        previous_revenue = float(row[1])
        revenue_change_list.append(revenue_diff)
    #print(revenue_change_list)
    average_revenue = round(sum(revenue_change_list[1:])/len(revenue_change_list[1:]), 2)
    print(average_revenue)
        #update the variable "previous_revenue"; previous_revenue = float(row[1]) to show that now previous revenue = previous month

    #print(revenue_diff)
        





#output_file = os.path.join("Financial Details")
    