#Erin Bentley
#Data Viz Boot Camp
#Python Homework
import os
import csv

csvpath = os.path.join("../PyBank","budget_data.csv")
#The total number of months included in the dataset
total_months = 0
# The net total amount of "Profit/Losses" over the entire period
total_profit = 0


#open budget csv file
with open(csvpath,"r") as Financial_Details:
    csvreader = csv.DictReader(Financial_Details)
    for row in csvreader:
        total_months = total_months + 1
        #tells the code to count the rows and keep a tally
        total_profit = total_profit + int(row["Profit/Losses"])
        #tells the code to calculate 0 + the row (converted into an integer)

#print(total_months)
#print(total_profit)


#output_file = os.path.join("Financial Details")
    