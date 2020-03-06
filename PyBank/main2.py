import os
import csv

# Path to  folder
csvpath = os.path.join("Downloads", "budget_data.csv")

# Open the CSV
with open(csvpath,newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    months = []
    for row in csvreader:
        months.append(row[1])
    
    print(months)

    for i in months:
        mthly_chg = []
        x = int(months[i+1]) - int(months[i])
        mthly_chg.append(i)

def average(numbers):
    length = len(numbers)
    total = 0
    for number in numbers:
        total += int(number)
    return total / length

avg = (average(months))
print(f'Average Change: {avg}')

max = max(months)
min = min(months)
print(f'Greatest Increase in Profits: {max}')
print(f'Greatest Decrease in Profits: {min}')













