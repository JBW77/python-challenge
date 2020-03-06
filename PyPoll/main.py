import os
import csv

# Path to  folder
csvpath = os.path.join("Downloads", "election_data.csv")

# Open the CSV
with open(csvpath,newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    print("Election Results")
    print("------------------")

    #get totals
    total_votes = 0
    khan = 0
    correy = 0
    li = 0
    otool = 0
    
    for row in csvreader:
    
        if row[2] == "Khan":
            khan += 1
        if row[2] == "Correy":
            correy += 1
        if row[2] == "Li":
            li += 1
        if row[2] == "O'Tooley":
            otool += 1

        total_votes +=1

    khan_pct = (khan/total_votes)*100
    correy_pct = (correy/total_votes)*100
    li_pct = (li/total_votes)*100
    otool_pct = (otool/total_votes)*100

    winner = max(khan,correy,li,otool)
    
    print(f'Total Votes: {total_votes}')
    print("------------------")
    print(f'Total Votes Khan: {khan_pct:.3f}% {khan}')
    print(f'Total Votes Correy: {correy_pct:.3f}% {correy}')
    print(f'Total Votes Li: {li_pct:.3f}% {li}')
    print(f"Total Votes O'Toole: {otool_pct:.3f}% {otool}")
    print("------------------")
  
    if winner == khan:
        print("Winner: Khan")
    if winner == correy:
        print("Winner: Correy")
    if winner == li:
        print("Winner: Li")
    if winner == otool:
        print("Winner: O'Toole")
        print("------------------")

    print("------------------")