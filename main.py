import os
import csv

# Path to  folder
new_file = os.path.join("Downloads", "election_data.csv")

# Open the CSV
with open(new_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    print("Election Results")
    print("------------------")

    #get total months
    count = 0
    for row in csvreader:
        count += 1
        #total = int(row[1])
    print(f'Total Votes: {count}')

    
    
    #working on the rest
    #candidates = ["Khan", "Correy", "Li", "O'tooly"]
    #khan = 0
    #Correy = 0
    #Li = 0
    #Otool = 0

    #for vote in csvreader[2]:
     #   if vote = "Khan":
    #      khan += 1
       # if vote = "Correy":
        #    Correy +=1
        #if vote = "Li":
         #   Li +=1
        #if vote = "O'Tooley"
         #   Otool + =1
    
    percent_Khan = len(khan)/count
    percent_Correy =  len(Correy)/count
    percent_Li = len(Li)/count
    percent_Otool = len(Otool)/count

    Print(f'Khan: {percent_Khan}, len(khan)')
    Print(f'Correy: {percent_Correy}, len(Corey)')
    Print(f'Li: {percent_Li}, len(Li)')
    Print(f"O'Tooley: {percent_Otool}, len(Otool)")




    



