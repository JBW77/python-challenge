import os
import csv

# Path to  folder
new_file = os.path.join("Downloads", "budget_data.csv")

# Open the CSV
with open(new_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    print("Financial Analysis")
    print("----------------------")


#get total months
    count = 0
    for row in csvreader:
        count += 1
        #total = int(row[1])
    print(f'Total Months: {count}')
   

def total(numbers):
    
    sum = 0
    for number in numbers:
        sum += number
    return sum


total = total([1,5,7])  # will be used to sum new profit changes list
print(f'Total: {total}')


# create empty list for monthly change

change = []

for row in csvreader:
    monthly_change = row[1] - row
    change.append(row)
avg = sum(change)/len(change)

print(f'Average Change: {avg}')

# greatest increase and decrease

for m in change:
    max = max(m)
    print(f'Greatest Increase in Profits: {max}')

for s in change:
    min = min(s)
    print(f'Greatest Decrease in Profits: {min}')









 












