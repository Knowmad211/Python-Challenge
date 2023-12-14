import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

TotalMonths = 0
TotalValue = 0
OpeningMonth = 0
ClosingMonth = 0
TotalDifference = []
DateList = []


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
        DateList.append (row[0])


TotalDifference.pop(0)

MaxIndex = TotalDifference.index(max(TotalDifference))
MinIndex = TotalDifference.index(min(TotalDifference))

DateList.pop(0)

    #   print(row)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalValue}")
print(f"Average Change: ${round(sum(TotalDifference)/(TotalMonths-1),2)}")
print(f"Greatest Increase in Profits: {DateList[MaxIndex]} (${max(TotalDifference)})")
print(f"Greatest Decrease in Profits: {DateList[MinIndex]} (${min(TotalDifference)})")

with open("Analysis/Analysis.txt", "w") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f"Total Months: {TotalMonths}", file=f)
    print(f"Total: ${TotalValue}", file=f)
    print(f"Average Change: ${round(sum(TotalDifference)/(TotalMonths-1),2)}", file=f)
    print(f"Greatest Increase in Profits: {DateList[MaxIndex]} (${max(TotalDifference)})", file=f)
    print(f"Greatest Decrease in Profits: {DateList[MinIndex]} (${min(TotalDifference)})", file=f)