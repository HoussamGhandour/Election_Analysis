# Read File

##Import csv to read and write csv files; import os to assist with folder and file directory
import csv
import os
##Change Directory to main folder
os.chdir('C:\\Users\\GHANDOURH\\Desktop\\Data_Analytics_Projects\\Analysis Projects\\Election_Analysis\\module')
## Initialize Variables
Total_Votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate =""
winning_count = 0
winning_percentage = 0.00
## Read orignal input file
file_to_load='Resources/election_results.csv'
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:

        Total_Votes = Total_Votes + 1

        candidate_name = row[2]

        # if candidate_name not in candidate_options:
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #initialize candidate voltes to zero for each key or candidate
            candidate_votes[candidate_name]=0
        # Calculate number of votes for each candidate
        candidate_votes[candidate_name] += 1
    #print (candidate_options)
    #print(Total_Votes)
    #print(candidate_votes)
    #Calculate Vote Percentage

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_Percentage = float(votes)/float(Total_Votes)*100
        candidate_summary = (f"{candidate_name}: {vote_Percentage:.1f}% of the Vote ({votes:,})\n")
        if(votes>winning_count) and (vote_Percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_Percentage
            winning_candidate = candidate_name

    winner_candidate_summary = (f"-------------------------\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count:,}\nWinning Percentage: {winning_percentage:.1f}\n-------------------------")
    print(winner_candidate_summary)
##create and save new output file
file_to_save= os.path.join("Analysis","election_analysis.txt")
with open (file_to_save,"w") as txt_file:
    txt_file.write(f"Election Results\n-------------------------\nTotal Votes: {Total_Votes:,}\n-------------------------\n")
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_Percentage = float(votes)/float(Total_Votes)*100
        candidate_summary = (f"{candidate_name}: {vote_Percentage:.1f}% of the Vote ({votes:,})\n")
        txt_file.write(f"{candidate_summary}")
        if(votes>winning_count) and (vote_Percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_Percentage
            winning_candidate = candidate_name
    
    txt_file.write(f"{winner_candidate_summary}")
