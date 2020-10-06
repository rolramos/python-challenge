#Import helpful modules
import os
import csv

#Remember to define variables in your code: months(1), total_amount(2), average_change(3), new_list(4 and 5), 
total_list = []
average_change_list =[]
avch = 0
value = 0
#Define path for file (using the force)
path = os.path.join('Resources', 'budget_data.csv')
#Open file
with open(path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	for row in csv_reader:

		months = csv_reader.line_num

months = months - 1
print("Financial Analysis")
print("---------------------")
print("Total months: " + str(months))

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        total_list.append(int(row[1]))
    
print("Total: $" + str(sum(total_list)))

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        average_change_list.append(int(row[1])-avch)
        avch = int(row[1])
average_change_list.pop(0)
print("Average Change: " + str('{:.2f}'.format((sum(average_change_list)/len(average_change_list)))))

print("Greatest Increase in Profits: " + str(max(average_change_list)))
print("Greatest Decrease in Profits: " + str(min(average_change_list)))
print("-------------------------")