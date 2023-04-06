#load the libraries need for this challenge
import os
import csv

#create a file path to access data
csvpath = os.path.join("Resources", "election_data.csv")

#initialize variables to store values
total_votes = 0
candidate_list = []
candidate_names = []
candidate_votes = {}
votepercent_list = []
decider_value = 0
key = {}


#open and read csv file
with open(csvpath) as csvfile:
    csvreader =csv.reader (csvfile, delimiter = ",")

    #skip header
    csvheader = next(csvfile)

    #iterate through each row in data
    for row in csvreader:

        #count the total votes
        total_votes += 1

        #list of candidates
        candidate_list.append(row[2])

    #iterate through the list of candidates
    for i in range(len(candidate_list)):
        
        #create a key for each candidate to store votes casted
        if (candidate_list[i]) not in candidate_names:
            candidate_names.append(candidate_list[i])
            
            #assign a value of zero to each key (i.e., candidate)
            candidate_votes[candidate_list[i]] = 0

        #add a value of 1 to each vote counted
        candidate_votes[candidate_list[i]] = candidate_votes[candidate_list[i]] + 1  
    
    #iterate through element in the dictionary-candidate_votes
    for i in candidate_votes:

        #grep each candidate's total votes
        #find the percentage of each candidate's votes
        votecount = (candidate_votes[i])
        votePercent = round((int(votecount) / int(total_votes)*100),3)
        votepercent_list.append(votePercent)

        #declare the winner
        if votecount > decider_value:
            decider_value = votecount
            winner_vote = decider_value
            winner_name = i
    #print winner's name
    print(f'{winner_name} is the winner with {winner_vote} votes')

print("Election Results")
print("---------------------------------------------------")
# The total number of months included in the dataset
print(f'Total Votes: {total_votes}')

print("---------------------------------------------------")

#simultaneously iterate each through candidate votes and percentage 
for (candidate,votepercent) in zip(candidate_votes,votepercent_list):
    
    #print each unique candidate, their votes and vote percent
    print(f'{candidate}: {votepercent}% ({candidate_votes[candidate]})')

print("---------------------------------------------------")
# The winner of the election based on popular vote
print(f'Winner: {winner_name}')

print("---------------------------------------------------")

#text file with results from analysis
with open(os.path.join("analysis", "Summary.txt"), "w") as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("-------------------------------------" + "\n")
    txtfile.write("Total Votes:" + " " + str(total_votes) + "\n")
    txtfile.write("-------------------------------------" + "\n")
    
    #simultaneously iterate each through candidate votes and percentage
    for (candidate,votepercent) in zip(candidate_votes,votepercent_list):
        
        #print each unique candidate, their votes and vote percent
        txtfile.write(str(candidate)+":" + " "+ str(votepercent) + "%" + " "+ "("+ str(candidate_votes[candidate]) + ")" + "\n")
    
    #write to text file the winner
    txtfile.write("-------------------------------------" + "\n")
    txtfile.write("Winner:" + " " + str(winner_name) + "\n")
    txtfile.write("-------------------------------------" + "\n")