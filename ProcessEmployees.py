'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv', 'r')
reader = csv.reader(infile)
next(reader)




#create an empty dictionary
employee_dict = {}


#use a loop to iterate through the csv file
for row in reader:
    if row[3] == "Marketing":
        name = row[1] + ' ' + row[2]
        print("Manager Name: ", name, " Current Salary: $", row[5], sep='')
        #check if the employee fits the search criteria
        employee_dict[name] = round((float(row[5]) * 1.10),2)




print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for name in employee_dict:
    print("Manager Name: ", name, " New Salary: $", employee_dict[name], sep='')



          
        

        
    
