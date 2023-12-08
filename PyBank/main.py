import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

TotalMonths = 0
TotalValue = 0
OpeningMonth = 0
ClosingMonth = 0
TotalDifference = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)


    # Read each row of data after the header
    for row in csvreader:
        TotalMonths = TotalMonths + 1
        TotalValue = TotalValue + int(row[1])
        ClosingMonth = int(row[1])
       
        TotalDifference.append (ClosingMonth - OpeningMonth)
        OpeningMonth = ClosingMonth
        TotalDifference.pop(0)


    #   print(row)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalValue}")
print(f"Average Change: ${sum(TotalDifference)/(TotalMonths-1)}")
print(f"Greatest Increase in Profits: **************** {max(TotalDifference)}")
print(f"Greatest Decrease in Profits: **************** {min(TotalDifference)}")