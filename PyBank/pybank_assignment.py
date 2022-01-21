#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os

import csv
from turtle import pd

csvpath= os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)

    total_months = 0
    total_profit_loss = 0

    profit_loss = []
    for row in csvreader:
        profit_loss.append(row)
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row[1])

    total_change_profit_loss = 0
    max_change_profit_loss = 0
    min_change_profit_loss = 0
    max_change_profit_month = min_change_profit_month = ''
    for x in range(1, len(profit_loss)):
        change_profit = int(profit_loss[x][1]) - int(profit_loss[x - 1][1])
        total_change_profit_loss = total_change_profit_loss + change_profit
        if change_profit >= max_change_profit_loss:
            max_change_profit_loss = change_profit
            max_change_profit_month = profit_loss[x][0]
        if change_profit <= min_change_profit_loss:
            min_change_profit_loss = change_profit
            min_change_profit_month = profit_loss[x][0]
    
    average_change_profit_loss = total_change_profit_loss / (total_months - 1)
    average_change_profit_loss = round(average_change_profit_loss, 2)
    
    print ("Total Months: " + str(total_months))
    print ("Total: $" + str(total_profit_loss))
    print ("Average  Change: " + str(average_change_profit_loss))
    print ("Greatest Increase in Profits: " + str(max_change_profit_month) + " ($" + str(max_change_profit_loss) + ")")
    print ("Greatest Decrease in Profits: " + str(min_change_profit_month) + " ($" + str(min_change_profit_loss) + ")")

with open("output.txt", "w") as f:
    f.write("\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write(("Total: $" + str(total_profit_loss) + "\n"))
    f.write(("Average  Change: " + str(average_change_profit_loss) + "\n"))
    f.write("Greatest Increase in Profits: " + str(max_change_profit_month) + " ($" + str(max_change_profit_loss) + ") + \n ")
    f.write("Greatest Decrease in Profits: " + str(min_change_profit_month) + " ($" + str(min_change_profit_loss) + ") + \n")










