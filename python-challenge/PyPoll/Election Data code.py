import csv

def analyze_votes(filename):
    # declaing the 'votes' as variables
    total_votes = 0
    candidate_votes = {}
  
    # location of the csv file of 'election data' 
    filename = r"C:\Users\Wolfred\Documents\Data Analysis Boot Camp\Week 3\python-challenge\PyPoll\Resources\election_data.csv"
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skips the first row of the csv file which contain the  header
        next(csvreader)
        
        # Looping through each of th rows
        for row in csvreader:
            # calulating the total number of votes
            total_votes += 1
            
            # Get the elector's name from the row
            candidate_name = row[2]
            
            # Add the elector to the dictionary and update the vote total
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            else:
                candidate_votes[candidate_name] = 1
  
    # Calculating percentage of votes each candidate has won
    candidate_percentages = {}
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate] = round(percentage, 2)
  
    # Find the winner based on popular vote based on the max votings
    winner = max(candidate_votes, key=candidate_votes.get)
  
    # displaying the results as shown in the challenge. 
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = candidate_percentages[candidate]
        print(f"{candidate}: {percentage}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

analyze_votes('election_data.csv')
