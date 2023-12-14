import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")

TotalVotes = 0
CandidateList = []
CandidateVotes = {}


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        TotalVotes = TotalVotes + 1
        if row[2] not in CandidateList:
            CandidateList.append(row[2])
            CandidateVotes[row[2]] = 0
        CandidateVotes[row[2]] = CandidateVotes[row[2]] +1




    #   print(row)
print("Election Results")
print("----------------------------")
print(f"Total Votes: {TotalVotes}")
print("----------------------------")
for Candidate in CandidateList:
    VotePercent = round((CandidateVotes[Candidate]/TotalVotes)*100, 3)
    print(f"{Candidate}: {VotePercent}% ({CandidateVotes[Candidate]})")
print("----------------------------")
print(f"Winner: {max(CandidateVotes, key=CandidateVotes.get)}")
print("----------------------------")



with open("Analysis/Analysis.txt", "w") as f:
    print("Election Results", file=f)
    print("----------------------------", file=f)
    print(f"Total Votes: {TotalVotes}", file=f)
    print("----------------------------", file=f)
    for Candidate in CandidateList:
        VotePercent = round((CandidateVotes[Candidate]/TotalVotes)*100, 3)
        print(f"{Candidate}: {VotePercent}% ({CandidateVotes[Candidate]})", file=f)
    print("----------------------------", file=f)
    print(f"Winner: {max(CandidateVotes, key=CandidateVotes.get)}", file=f)
    print("----------------------------", file=f)