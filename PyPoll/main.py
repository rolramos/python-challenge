import os
import csv

path = os.path.join("Resources","election_data.csv")

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        votes = csv_reader.line_num

votes = int(votes - 1)


candidates = []

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        candidates.append(row[2])

candidates = list(dict.fromkeys(candidates))
candidates.pop(0)


Khan_list = []
Correy_list = []
Li_list = []
OTooley_list = []

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        if row[2] == "Khan":
            Khan_list.append(row[0])
        elif row[2] == "Correy":
            Correy_list.append(row[0])
        elif row[2] == "Li":
            Li_list.append(row[0])
        elif row[2] == "O'Tooley":
            OTooley_list.append(row[0])
    
total_K = int(len(Khan_list))
total_C = int(len(Correy_list))
total_L = int(len(Li_list))
total_O = int(len(OTooley_list))

T1 = ("Election Results")
T2 = ("-----------------")
T3 = ("Total Votes: " + str(votes))
T4 = ("------------------")
T5 = (str(candidates[0]) + ": " + str("{:.0%}".format((total_K/votes))) + " (" + str(total_K) + ")")
T6 = (str(candidates[1]) + ": " + str("{:.0%}".format((total_C/votes))) + " (" + str(total_C) + ")")
T7 = (str(candidates[2]) + ": " + str("{:.0%}".format((total_L/votes))) + " (" + str(total_L) + ")")
T8 = (str(candidates[3]) + ": " + str("{:.0%}".format((total_O/votes))) + " (" + str(total_O) + ")")

print(T1)
print(T2)
print(T3)
print(T4)
print(T5)
print(T6)
print(T7)
print(T8)


