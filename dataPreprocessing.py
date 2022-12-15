import csv

dataset_1 = []
dataset_2 = []

with open('brightStars.csv','r') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        dataset_1.append(i)
        
with open('fieldBrownDwarves.csv','r') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        dataset_2.append(i)

h1 = dataset_1[0]
h2 = dataset_2[0]

p_d1 = dataset_1[1:]
p_d2 = dataset_2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
with open("allStars.csv",'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    