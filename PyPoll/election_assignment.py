#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os

import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)

    total_votes = 0

    candidates = []
    unique_candidate = []
    unique_votes = []
    votes_percent = []
    
    for row in csvreader:
        total_votes = total_votes + 1
        candidates.append(row[2])

    for x in set(candidates):
        unique_candidate.append(x)

        y = candidates.count(x)
        unique_votes.append(y)

        z = (y/total_votes)*100
        z = round(z, 2)
        votes_percent.append(z)

    
    winning_votes = max(unique_votes)
    

    print("Election Results: ")
    print("Total votes: " + str(total_votes))

    winner = ""
    for i in range(len(unique_candidate)):
            print (unique_candidate[i] + ": " + str(votes_percent[i]) + "% (" + str(unique_votes[i]) + ")") 
            if winning_votes == unique_votes[i]:
                winner = unique_candidate[i]
    print("Winner: " + winner)

#Export to text file

with open("output.txt", "w") as f:
    f.write("Election Results\n")
    f.write("Total votes: " + str(total_votes) + "\n")
    for i in range(len(unique_candidate)):
            f.write (unique_candidate[i] + ": " + str(votes_percent[i]) + "% (" + str(unique_votes[i]) + ")" + "\n")
    f.write("Winner: " + winner + "\n")

