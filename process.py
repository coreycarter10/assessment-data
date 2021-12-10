log_file = open("um-server-01.txt")
# Creating a variable to save the open file function for the provided csv file

def sales_reports(log_file):  #defining a function called sales_reports that is taking in the saved variable that opens your csv file
    for line in log_file:  #creating a loop to loop over all the lines in the csv file
        line = line.rstrip()  #striping whitespace from the lines in the file
        day = line[0:3]  #finding the day of the week that is in the line
        if day == "Mon":    #creating a conditional to find monday deliveries and then printing that line in your console  
            print(line)


sales_reports(log_file) #running the defined function

def print_melons(log_file):
    for line in log_file:
        values = line.split('')
        total_melons = int(values[2])
        if total_melons > 10:
            print(total_melons)
