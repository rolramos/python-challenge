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
T1 = ("Financial Analysis")
T2 = ("---------------------")
T3 = ("Total months: " + str(months))

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        total_list.append(int(row[1]))
    
T4 = ("Total: $" + str(sum(total_list)))

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        average_change_list.append(int(row[1])-avch)
        avch = int(row[1])
average_change_list.pop(0)
T5 = ("Average Change: " + str('{:.2f}'.format((sum(average_change_list)/len(average_change_list)))))

T6 = ("Greatest Increase in Profits: " + str(max(average_change_list)))
T7 = ("Greatest Decrease in Profits: " + str(min(average_change_list)))
T8 = ("-------------------------")

Output = [T1,T2,T3,T4,T5,T6,T7,T8]

print(Output)

output_file = "analysis/financial_analysis.csv"

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow([T1,T2,T3,T4,T5,T6,T7,T8])
