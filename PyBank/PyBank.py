#Erin Bentley
#Data Viz Boot Camp
#Python Homework
import os
import csv

csvpath = os.path.join("../PyBank","budget_data.csv")
#The total number of months included in the dataset
total_months = 0


#open budget csv file
with open(csvpath,"r") as Financial_Details:
    csvreader = csv.DictReader(Financial_Details)
    for row in csvreader:
        total_months = total_months + 1
#print(total_months)


#output_file = os.path.join("Financial Details")
    