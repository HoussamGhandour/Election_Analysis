# Read File

##Import csv to read and write csv files; import os to assist with folder and file directory
import csv
import os
##Change Directory to main folder
os.chdir('C:\\Users\\GHANDOURH\\Desktop\\Data_Analytics_Projects\\Analysis Projects\\Election_Analysis\\module')
##Read orignal input file
file_to_load='Resources/election_results.csv'
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
        #print(row[0])
##create and save new output file
file_to_save= os.path.join("Analysis","election_analysis.txt")
with open (file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nArapahow\nDenver\nJefferson")

# Summarize data into dictionaries
# Get unique number of candidates
# Get unique names of counties
# Summarize names of candidates who received votes
# Add total number of votes cast
# use if statement to count number of votes for each candidate
# use percentage of votes to for each candidate
# announce winner of election based on highest number of votes
